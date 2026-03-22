"""Canonical ecosystem change sync helpers.

This module centralizes how runtime events are normalized, logged locally,
and mirrored into Notion when credentials are available.
"""

from __future__ import annotations

import json
import logging
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

BASE_DIR = Path('/Users/andy/my_too_test')
LOCAL_AUDIT_PATH = BASE_DIR / 'autonomous_operator' / 'state' / 'ecosystem_change_events.ndjson'
APO_SIGNATURE = '⟦APΩ:Σ⟧'
SIGMA_APOMEGA_COS = 'SIGMA_APOMEGA_COS'

try:
    from config import NOTION_TOKEN, NOTION_DB_ID
except Exception:
    NOTION_TOKEN = None
    NOTION_DB_ID = None

try:
    from notion_client import Client as NotionClient
except Exception:
    NotionClient = None

try:
    from kernel.connector_mesh import resolve_connector, connector_context
except Exception:
    resolve_connector = None
    connector_context = None

LOCAL_AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
_logger = logging.getLogger('EcosystemSync')


def _truncate(value: Any, limit: int = 1500) -> str:
    return str(value)[:limit]


def _resolve(label: str | None) -> str | None:
    if not label:
        return None
    if resolve_connector is None:
        return label
    try:
        return resolve_connector(label)
    except Exception:
        return label


def _build_local_row(
    event_type: str,
    category: str,
    message: str,
    priority: str = 'Medium',
    *,
    source: str = 'ecosystem',
    status: str = 'Operation Log',
    connector: str | None = None,
    surface: str | None = None,
    target: str | None = None,
    account: str | None = None,
    reason: str | None = None,
    snippet: str | None = None,
    arguments: str | None = None,
    sentiment: str | None = 'Neutral',
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    event_id = uuid.uuid4().hex
    connector = connector or _resolve(category or source or event_type)
    context = None
    if connector_context and connector:
        try:
            context = connector_context(connector, task_id=event_id)
        except Exception:
            context = None
    return {
        'signature': APO_SIGNATURE,
        'sigma_marker': SIGMA_APOMEGA_COS,
        'timestamp': datetime.now().isoformat(),
        'event_id': event_id,
        'event_type': event_type,
        'category': category,
        'message': message,
        'priority': priority,
        'source': source,
        'status': status,
        'connector': connector,
        'surface': surface,
        'target': target,
        'account': account,
        'reason': reason or event_type,
        'snippet': snippet or message,
        'arguments': arguments,
        'sentiment': sentiment,
        'metadata': metadata or {},
        'connector_context': context,
    }


def _append_local(row: dict[str, Any]) -> None:
    try:
        with LOCAL_AUDIT_PATH.open('a', encoding='utf-8') as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + '\n')
    except Exception as exc:
        _logger.debug('Local ecosystem audit append failed: %s', exc)


def _page_properties(row: dict[str, Any]) -> list[dict[str, Any]]:
    title = f"{APO_SIGNATURE} {row['event_type']}: {row['category']}"
    props: dict[str, Any] = {}

    props['Name'] = {'title': [{'text': {'content': title}}]}
    props['Command Name'] = {'title': [{'text': {'content': title}}]}
    props['Status'] = {'select': {'name': row['status']}}
    props['Category'] = {'select': {'name': row['category']}}
    props['Priority'] = {'select': {'name': row['priority']}}
    if row.get('sentiment'):
        props['Sentiment'] = {'select': {'name': row['sentiment']}}
    if row.get('connector'):
        props['Connector'] = {'select': {'name': row['connector']}}
    if row.get('source'):
        props['Source'] = {'select': {'name': row['source']}}
    if row.get('target'):
        props['Target'] = {'select': {'name': row['target']}}
    if row.get('account'):
        props['Account'] = {'select': {'name': row['account']}}
    if row.get('reason'):
        props['Reason'] = {'rich_text': [{'text': {'content': _truncate(row['reason'])}}]}
    if row.get('arguments'):
        props['Arguments'] = {'rich_text': [{'text': {'content': _truncate(row['arguments'])}}]}
    props['Snippet'] = {'rich_text': [{'text': {'content': _truncate(row['snippet'] or row['message'])}}]}
    if row.get('surface'):
        props['Surface'] = {'rich_text': [{'text': {'content': _truncate(row['surface'])}}]}
    props['Event ID'] = {'rich_text': [{'text': {'content': row['event_id']}}]}
    return [props]


def emit_ecosystem_change(
    event_type: str,
    category: str,
    message: str,
    priority: str = 'Medium',
    *,
    source: str = 'ecosystem',
    status: str = 'Operation Log',
    connector: str | None = None,
    surface: str | None = None,
    target: str | None = None,
    account: str | None = None,
    reason: str | None = None,
    snippet: str | None = None,
    arguments: str | None = None,
    sentiment: str | None = 'Neutral',
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    row = _build_local_row(
        event_type=event_type,
        category=category,
        message=message,
        priority=priority,
        source=source,
        status=status,
        connector=connector,
        surface=surface,
        target=target,
        account=account,
        reason=reason,
        snippet=snippet,
        arguments=arguments,
        sentiment=sentiment,
        metadata=metadata,
    )
    _append_local(row)

    if not NOTION_TOKEN or not NOTION_DB_ID or NotionClient is None:
        return row

    try:
        notion = NotionClient(auth=NOTION_TOKEN)
        for properties in _page_properties(row):
            try:
                notion.pages.create(
                    parent={'database_id': NOTION_DB_ID},
                    properties=properties,
                )
                break
            except Exception as page_exc:
                _logger.debug('Notion sync attempt failed: %s', page_exc)
    except Exception as exc:
        _logger.debug('Notion sync soft-fail: %s', exc)

    return row

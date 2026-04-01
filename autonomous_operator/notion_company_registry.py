"""Canonical Notion company registry for the ecosystem.

This module treats Notion as the shared company database:
- humans are staff records
- agents are employee/automation records
- services are external/internal operational surfaces
- events/tasks are the activity ledger

It is schema-aware when possible and falls back to safe local normalization.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any

BASE_DIR = Path("/Users/andy/my_too_test")

try:
    from config import NOTION_TOKEN, NOTION_DB_ID, APO_NET_NOTION_DB_ID
except Exception:
    NOTION_TOKEN = None
    NOTION_DB_ID = None
    APO_NET_NOTION_DB_ID = None

try:
    from notion_client import Client as NotionClient
except Exception:
    NotionClient = None

try:
    from kernel.connector_mesh import mesh_summary, resolve_connector
except Exception:
    mesh_summary = None
    resolve_connector = None


COMPANY_ENTITY_TYPES = (
    "human",
    "agent",
    "service",
    "team",
    "event",
    "task",
    "project",
)

COMPANY_STATUS_VALUES = (
    "active",
    "standby",
    "offline",
    "paused",
    "error",
    "complete",
    "open",
    "closed",
)

DEFAULT_PUBLIC_FACE_NAME = "Nguyễn Cường (APΩ)"
DEFAULT_CANONICAL_NAME = "Nguyễn Cường"
DEFAULT_CANONICAL_EMAIL = "nguyencuong.2509@gmail.com"
DEFAULT_PUBLIC_FACE_URL = "https://creators.contact/"
DEFAULT_PUBLIC_FACE_SOURCE = "creators.contact public profile"
DEFAULT_PUBLIC_PROFILE_ID = "gravatar:30227240a159d40d3b531bf7ef6904b6307b789738b0ef9c112d814cf1c267aa"
DEFAULT_PUBLIC_FACE_GITHUB = "https://github.com/NguyenCuong1989"
DEFAULT_PUBLIC_FACE_TAGS = (
    "public-face",
    "canonical-identity",
    "ecosystem",
    "creators.contact",
)


@dataclass
class CompanyRecord:
    name: str
    entity_type: str
    role: str = "staff"
    status: str = "active"
    connector: str | None = None
    owner: str | None = None
    source: str | None = None
    summary: str | None = None
    tags: list[str] | None = None
    external_id: str | None = None
    notes: str | None = None
    metadata: dict[str, Any] | None = None

    def to_payload(self) -> dict[str, Any]:
        payload = {
            "name": self.name,
            "entity_type": self.entity_type,
            "role": self.role,
            "status": self.status,
            "connector": self.connector,
            "owner": self.owner,
            "source": self.source,
            "summary": self.summary,
            "tags": self.tags or [],
            "external_id": self.external_id,
            "notes": self.notes,
            "metadata": self.metadata or {},
        }
        return payload

def _unique_tags(*groups: list[str] | tuple[str, ...] | None) -> list[str]:
    tags: list[str] = []
    seen: set[str] = set()
    for group in groups:
        if not group:
            continue
        for tag in group:
            if not tag or tag in seen:
                continue
            seen.add(tag)
            tags.append(tag)
    return tags



def build_public_face_record() -> CompanyRecord:
    return CompanyRecord(
        name=DEFAULT_PUBLIC_FACE_NAME,
        entity_type="human",
        role="staff",
        status="active",
        source=DEFAULT_PUBLIC_FACE_SOURCE,
        summary=(
            "Public-facing identity anchor for the ecosystem. "
            "Use this record when the outside world needs a stable human-facing name."
        ),
        tags=list(DEFAULT_PUBLIC_FACE_TAGS),
        external_id=DEFAULT_PUBLIC_PROFILE_ID,
        notes=(
            f"Public profile: {DEFAULT_PUBLIC_FACE_URL}\n"
            f"Canonical name: {DEFAULT_CANONICAL_NAME}\n"
            f"Canonical email: {DEFAULT_CANONICAL_EMAIL}\n"
            f"GitHub: {DEFAULT_PUBLIC_FACE_GITHUB}"
        ),
        metadata={
            "public_profile_url": DEFAULT_PUBLIC_FACE_URL,
            "canonical_name": DEFAULT_CANONICAL_NAME,
            "canonical_email": DEFAULT_CANONICAL_EMAIL,
            "public_aliases": ["NguyenCuong1989"],
        },
    )



def build_canonical_human_record() -> CompanyRecord:
    return CompanyRecord(
        name=DEFAULT_CANONICAL_NAME,
        entity_type="human",
        role="staff",
        status="active",
        source="canonical operator identity",
        summary="Primary human operator for the ecosystem control plane.",
        tags=_unique_tags(("canonical-operator", "internal-user"), DEFAULT_PUBLIC_FACE_TAGS),
        external_id=DEFAULT_CANONICAL_EMAIL,
        notes=(
            "Primary operator identity used for internal routing. "
            "This record should remain the stable source for human ownership."
        ),
        metadata={
            "primary_email": DEFAULT_CANONICAL_EMAIL,
            "public_face": DEFAULT_PUBLIC_FACE_NAME,
            "public_profile_url": DEFAULT_PUBLIC_FACE_URL,
        },
    )



def build_company_roster(
    *,
    agent_names: list[str] | None = None,
    service_names: list[str] | None = None,
    mesh_service_names: list[str] | None = None,
    include_public_face: bool = True,
) -> list[CompanyRecord]:
    roster: list[CompanyRecord] = []
    if include_public_face:
        roster.append(build_public_face_record())
    roster.append(build_canonical_human_record())

    for agent_name in agent_names or []:
        agent_name = agent_name.strip()
        if not agent_name:
            continue
        roster.append(
            CompanyRecord(
                name=agent_name,
                entity_type="agent",
                role="staff",
                status="active",
                source="internal agent registry",
                summary="Agent personnel record in the shared company database.",
                tags=["agent", "internal-personnel"],
                external_id=f"agent:{agent_name}",
                notes="Derived roster entry for agent synchronization.",
                metadata={"kind": "agent", "name": agent_name},
            )
        )

    merged_service_names = list(service_names or [])
    merged_service_names.extend(mesh_service_names or [])

    for service_name in merged_service_names:
        service_name = service_name.strip()
        if not service_name:
            continue
        canonical_service_name = resolve_connector(service_name) if resolve_connector else service_name
        roster.append(
            CompanyRecord(
                name=canonical_service_name,
                entity_type="service",
                role="staff",
                status="active",
                source="external or internal service surface",
                summary="Service connector mirrored into the shared company database.",
                tags=["service", "connector"],
                external_id=f"service:{canonical_service_name}",
                notes="Canonical service entry for ecosystem synchronization.",
                metadata={
                    "kind": "service",
                    "name": canonical_service_name,
                    "requested_name": service_name,
                },
            )
        )

    return roster



def preview_company_roster(
    *,
    agent_names: list[str] | None = None,
    service_names: list[str] | None = None,
    mesh_service_names: list[str] | None = None,
    include_public_face: bool = True,
) -> list[dict[str, Any]]:
    return [
        record.to_payload()
        for record in build_company_roster(
            agent_names=agent_names,
            service_names=service_names,
            mesh_service_names=mesh_service_names,
            include_public_face=include_public_face,
        )
    ]


def build_mesh_service_names(*, include_live: bool = True, include_declared: bool = True) -> list[str]:
    if mesh_summary is None:
        return []
    names: list[str] = []
    for route in mesh_summary():
        status = route.get("status")
        if status == "live" and not include_live:
            continue
        if status != "live" and not include_declared:
            continue
        canonical = route.get("canonical")
        if canonical and canonical not in names:
            names.append(canonical)
    return names


def build_creator_day_roster() -> list[CompanyRecord]:
    return build_company_roster(
        mesh_service_names=build_mesh_service_names(include_live=True, include_declared=True),
    )


def resolve_company_db_id(explicit_db_id: str | None = None) -> str | None:
    if explicit_db_id:
        return explicit_db_id.strip()
    return (
        os.environ.get("APO_NET_NOTION_DB_ID")
        or APO_NET_NOTION_DB_ID
        or os.environ.get("NOTION_DB_ID")
        or NOTION_DB_ID
    )


def notion_client() -> Any:
    token = os.environ.get("NOTION_TOKEN") or NOTION_TOKEN
    if not token or NotionClient is None:
        raise RuntimeError("Notion token unavailable")
    return NotionClient(auth=token)


def has_notion_access() -> bool:
    token = os.environ.get("NOTION_TOKEN") or NOTION_TOKEN
    return bool(token and NotionClient is not None)


def _truncate(value: Any, limit: int = 1500) -> str:
    return str(value)[:limit]


def _schema_keys(db_schema: dict[str, Any]) -> set[str]:
    return set(db_schema.get("properties", {}).keys())


def _select(name: str) -> dict[str, Any]:
    return {"select": {"name": name}}


def _rich_text(value: str) -> dict[str, Any]:
    return {"rich_text": [{"text": {"content": _truncate(value)}}]}


def _title(value: str) -> dict[str, Any]:
    return {"title": [{"text": {"content": _truncate(value)}}]}


def company_properties(record: CompanyRecord, db_schema: dict[str, Any] | None = None) -> dict[str, Any]:
    schema_keys = _schema_keys(db_schema or {}) if db_schema else set()
    props: dict[str, Any] = {}

    def put(key: str, value: dict[str, Any]) -> None:
        if not schema_keys or key in schema_keys:
            props[key] = value

    put("Name", _title(record.name))
    put("Title", _title(record.name))
    put("Record Name", _title(record.name))
    put("Entity Type", _select(record.entity_type))
    put("Type", _select(record.entity_type))
    put("Role", _select(record.role))
    put("Status", _select(record.status))

    if record.connector:
        put("Connector", _select(record.connector))
    if record.owner:
        put("Owner", _select(record.owner))
    if record.source:
        put("Source", _select(record.source))
    if record.summary:
        put("Summary", _rich_text(record.summary))
    if record.external_id:
        put("External ID", _rich_text(record.external_id))
    if record.notes:
        put("Notes", _rich_text(record.notes))
    if record.tags:
        # Notion multi_select requires schema support; include only if the key exists.
        put("Tags", {"multi_select": [{"name": tag} for tag in record.tags[:20]]})
    if record.metadata:
        put("Metadata", _rich_text(str(record.metadata)))

    put("Updated At", _rich_text(datetime.now().isoformat()))
    return props


def create_company_record(
    record: CompanyRecord,
    *,
    db_id: str | None = None,
    db_schema: dict[str, Any] | None = None,
) -> dict[str, Any]:
    resolved_db = resolve_company_db_id(db_id)
    if not resolved_db:
        raise RuntimeError("Company Notion database id unavailable")

    client = notion_client()
    props = company_properties(record, db_schema=db_schema)
    page = client.pages.create(
        parent={"database_id": resolved_db},
        properties=props,
    )
    return page


def upsert_company_record(
    record: CompanyRecord,
    *,
    db_id: str | None = None,
    db_schema: dict[str, Any] | None = None,
    match_field: str = "External ID",
) -> dict[str, Any]:
    resolved_db = resolve_company_db_id(db_id)
    if not resolved_db:
        raise RuntimeError("Company Notion database id unavailable")

    client = notion_client()
    props = company_properties(record, db_schema=db_schema)

    try:
        search_value = record.external_id or record.name
        if search_value:
            query = client.databases.query(
                database_id=resolved_db,
                filter={
                    "property": match_field,
                    "rich_text": {"equals": search_value},
                },
                page_size=1,
            )
            results = query.get("results", [])
            if results:
                page_id = results[0]["id"]
                return client.pages.update(page_id=page_id, properties=props)
    except Exception:
        # Fall through to create when filter is unavailable or schema differs.
        pass

    return client.pages.create(
        parent={"database_id": resolved_db},
        properties=props,
    )


def normalize_page(item: dict[str, Any]) -> dict[str, Any]:
    properties = item.get("properties", {})

    def extract_title(key: str) -> str | None:
        prop = properties.get(key, {})
        title = prop.get("title", [])
        if title:
            return title[0].get("plain_text")
        return None

    def extract_select(key: str) -> str | None:
        prop = properties.get(key, {})
        select = prop.get("select") or {}
        return select.get("name")

    def extract_rich_text(key: str) -> str | None:
        prop = properties.get(key, {})
        rich = prop.get("rich_text", [])
        if rich:
            return rich[0].get("plain_text")
        return None

    name = (
        extract_title("Name")
        or extract_title("Title")
        or extract_title("Record Name")
        or "Untitled"
    )
    entity_type = extract_select("Entity Type") or extract_select("Type") or "unknown"
    role = extract_select("Role") or "staff"
    status = extract_select("Status") or "unknown"
    connector = extract_select("Connector")
    owner = extract_select("Owner")
    source = extract_select("Source")
    summary = extract_rich_text("Summary") or extract_rich_text("Snippet") or extract_rich_text("Notes")
    external_id = extract_rich_text("External ID")
    notes = extract_rich_text("Notes")

    tags_prop = properties.get("Tags", {})
    tags = [item.get("name") for item in tags_prop.get("multi_select", []) if item.get("name")]

    return {
        "name": name,
        "entity_type": entity_type,
        "role": role,
        "status": status,
        "connector": connector,
        "owner": owner,
        "source": source,
        "summary": summary,
        "tags": tags,
        "external_id": external_id,
        "notes": notes,
        "id": item.get("id"),
        "url": item.get("url"),
    }


def query_company_records(
    *,
    db_id: str | None = None,
    query: str | None = None,
    page_size: int = 25,
    max_pages: int = 1,
) -> dict[str, Any]:
    resolved_db = resolve_company_db_id(db_id)
    if not resolved_db:
        if not query:
            raise RuntimeError("Company Notion database id unavailable and no search query provided")
        client = notion_client()
        results = client.search(query=query).get("results", [])
        dbs = []
        for item in results:
            if item.get("object") != "database":
                continue
            dbs.append(
                {
                    "id": item.get("id"),
                    "title": item.get("title", [{}])[0].get("plain_text", "Untitled") if item.get("title") else "Untitled",
                    "url": item.get("url"),
                }
            )
        return {"mode": "search", "query": query, "databases": dbs}

    client = notion_client()
    rows: list[dict[str, Any]] = []
    cursor = None
    pages = 0

    while True:
        payload = {"database_id": resolved_db, "page_size": page_size}
        if cursor:
            payload["start_cursor"] = cursor
        response = client.databases.query(**payload)
        for item in response.get("results", []):
            rows.append(normalize_page(item))
        pages += 1
        if not response.get("has_more") or pages >= max_pages:
            break
        cursor = response.get("next_cursor")

    return {
        "mode": "direct",
        "database_id": resolved_db,
        "count": len(rows),
        "results": rows,
        "has_more": response.get("has_more", False),
        "next_cursor": response.get("next_cursor"),
    }

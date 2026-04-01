from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConnectorRoute:
    canonical: str
    aliases: tuple[str, ...]
    layer: str
    transport: str
    status: str = "declared"
    kind: str = "service"


CONNECTOR_ROUTES: tuple[ConnectorRoute, ...] = (
    ConnectorRoute(
        canonical="Stripe",
        aliases=("stripe", "payments", "billing"),
        layer="economics",
        transport="balancehub",
        status="live",
        kind="external-service",
    ),
    ConnectorRoute(
        canonical="Registry-Service",
        aliases=(
            "github",
            "github-actions",
            "github-cli",
            "github-desktop",
            "copilot",
            "gitkraken",
            "notion",
            "linear",
            "atlassian",
            "rovo",
            "asana",
            "airtable",
            "figma",
        ),
        layer="registry",
        transport="balancehub",
        status="declared",
        kind="external-service",
    ),
    ConnectorRoute(
        canonical="Invocation-Gateway",
        aliases=(
            "replit",
            "playwright",
            "codex",
            "openai",
            "gemini",
            "firebase",
            "cloudrun",
            "gke",
            "bigquery",
            "mongodb",
            "neon",
            "vercel",
            "netlify",
            "slack",
            "discord",
            "telegram",
        ),
        layer="execution",
        transport="balancehub",
        status="declared",
        kind="external-service",
    ),
    ConnectorRoute(
        canonical="BalanceHub",
        aliases=("balancehub", "mcp-router", "factory-worker", "apo-kernel", "aios-kernel", "aios-router", "aios-worker"),
        layer="control-plane",
        transport="local-docker",
        status="live",
        kind="control-plane",
    ),
    ConnectorRoute(
        canonical="Postgres",
        aliases=("postgres", "database", "sql"),
        layer="data",
        transport="local-docker",
        status="live",
        kind="substrate",
    ),
    ConnectorRoute(
        canonical="Redis",
        aliases=("redis", "cache", "queue"),
        layer="data",
        transport="local-docker",
        status="live",
        kind="substrate",
    ),
    ConnectorRoute(
        canonical="Prometheus",
        aliases=("prometheus", "metrics", "monitoring"),
        layer="observability",
        transport="local-docker",
        status="live",
        kind="observer",
    ),
    ConnectorRoute(
        canonical="Fallback-Router",
        aliases=("fallback", "recovery", "defer", "retry"),
        layer="safety",
        transport="balancehub",
        status="live",
        kind="safety-router",
    ),
    ConnectorRoute(
        canonical="Audit-Logger",
        aliases=("audit", "logger", "trace", "tracing"),
        layer="safety",
        transport="balancehub",
        status="live",
        kind="observer",
    ),
    ConnectorRoute(
        canonical="Omega-Core",
        aliases=("omega", "orchestrator", "workspace", "planner"),
        layer="strategy",
        transport="balancehub",
        status="declared",
        kind="core-node",
    ),
    ConnectorRoute(
        canonical="Antigravity-Core",
        aliases=("antigravity", "runtime", "shell", "context"),
        layer="identity",
        transport="workbench",
        status="declared",
        kind="core-node",
    ),
    ConnectorRoute(
        canonical="HuggingFace",
        aliases=("huggingface", "hf", "model-hub"),
        layer="execution",
        transport="balancehub",
        status="declared",
        kind="external-service",
    ),
    ConnectorRoute(
        canonical="DAIOF-Framework",
        aliases=("daiof", "framework", "ecosystem"),
        layer="execution",
        transport="local-docker",
        status="declared",
        kind="node-host",
    ),
    ConnectorRoute(
        canonical="HyperAI-API",
        aliases=("hyperai-api", "api"),
        layer="execution",
        transport="local-docker",
        status="declared",
        kind="node-host",
    ),
    ConnectorRoute(
        canonical="UEVS-Service",
        aliases=("uevs", "service"),
        layer="safety",
        transport="balancehub",
        status="declared",
        kind="safety-router",
    ),
    ConnectorRoute(
        canonical="SACR-Service",
        aliases=("sacr", "service"),
        layer="safety",
        transport="balancehub",
        status="declared",
        kind="safety-router",
    ),
    ConnectorRoute(
        canonical="Digital-Ecosystem",
        aliases=("digital-ecosystem", "simulator"),
        layer="experimental",
        transport="local-docker",
        status="declared",
        kind="node-host",
    ),
    ConnectorRoute(
        canonical="Evaluation-Runner",
        aliases=("evaluation", "runner", "benchmark"),
        layer="observability",
        transport="balancehub",
        status="declared",
        kind="observer",
    ),
    ConnectorRoute(
        canonical="HAIOS-Monitor",
        aliases=("haios", "monitor", "health"),
        layer="observability",
        transport="balancehub",
        status="declared",
        kind="observer",
    ),
    ConnectorRoute(
        canonical="tele_node",
        aliases=("tele-node", "telegram-node", "axis_1.messaging.telegram"),
        layer="messaging",
        transport="telegram",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="discord_node",
        aliases=("discord-node", "axis_1.messaging.discord"),
        layer="messaging",
        transport="discord",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="slack_node",
        aliases=("slack-node", "axis_1.messaging.slack"),
        layer="messaging",
        transport="slack",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="omega_core_agent",
        aliases=("omega-core-agent", "axis_2.reasoning.planning"),
        layer="reasoning",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="antigravity_core_agent",
        aliases=("antigravity-core-agent", "axis_2.analysis.code_audit"),
        layer="analysis",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="heuristic_agent",
        aliases=("heuristic-agent", "axis_2.logic.heuristic"),
        layer="reasoning",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="agent_browser_v2",
        aliases=("agent-browser-v2", "axis_3.ui_vision.element_recognition"),
        layer="vision",
        transport="browser",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="ocr_node",
        aliases=("ocr-node", "axis_3.ocr.text_recognition"),
        layer="vision",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="stable_diffusion_agent",
        aliases=("stable-diffusion-agent", "axis_3.image_gen.stable_diffusion"),
        layer="vision",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="postgres_agent",
        aliases=("postgres-agent", "axis_4.data.persistence"),
        layer="data",
        transport="postgres",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="redis_agent",
        aliases=("redis-agent", "axis_4.data.cache"),
        layer="data",
        transport="redis",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="balancehub_agent",
        aliases=("balancehub-agent", "axis_5.execution.system_control"),
        layer="execution",
        transport="local-docker",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="bridge_agent",
        aliases=("bridge-agent", "axis_5.execution.bridge"),
        layer="execution",
        transport="local-docker",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="vercel_agent",
        aliases=("vercel-agent", "axis_5.deployment.vercel"),
        layer="deployment",
        transport="vercel",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="netlify_agent",
        aliases=("netlify-agent", "axis_5.deployment.netlify"),
        layer="deployment",
        transport="netlify",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="malwarebytes_agent",
        aliases=("malwarebytes-agent", "axis_6.security.protection"),
        layer="security",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="guardian_node",
        aliases=("guardian-node", "axis_6.security.audit"),
        layer="security",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="revenue_node",
        aliases=("revenue-node", "axis_7.economics.value_scoring"),
        layer="economics",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="stripe_agent",
        aliases=("stripe-agent", "axis_7.economics.finance"),
        layer="economics",
        transport="stripe",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="identity_agent",
        aliases=("identity-agent", "axis_8.identity.supreme_commander_auth"),
        layer="identity",
        transport="local",
        status="live",
        kind="node",
    ),
    ConnectorRoute(
        canonical="shutdown_agent",
        aliases=("shutdown-agent", "axis_8.lifecycle.panic_shutdown"),
        layer="lifecycle",
        transport="local",
        status="live",
        kind="node",
    ),
)

_ALIAS_INDEX = {
    alias: route.canonical
    for route in CONNECTOR_ROUTES
    for alias in route.aliases
}

_CANONICAL_INDEX = {route.canonical.lower(): route for route in CONNECTOR_ROUTES}


def normalize_service_name(name: str) -> str:
    return name.strip().lower().replace("_", "-").replace(" ", "-")


def resolve_connector(name: str) -> str:
    normalized = normalize_service_name(name)
    if normalized in _ALIAS_INDEX:
        return _ALIAS_INDEX[normalized]
    if normalized in _CANONICAL_INDEX:
        return _CANONICAL_INDEX[normalized].canonical
    return "Registry-Service"


def connector_route(name: str) -> ConnectorRoute:
    canonical = resolve_connector(name)
    return _CANONICAL_INDEX.get(canonical.lower(), ConnectorRoute(canonical, (), "registry", "balancehub"))


def mesh_summary() -> list[dict[str, str]]:
    return [
        {
            "canonical": route.canonical,
            "layer": route.layer,
            "transport": route.transport,
            "status": route.status,
            "kind": route.kind,
            "aliases": ",".join(route.aliases),
        }
        for route in CONNECTOR_ROUTES
    ]


def connector_context(name: str, *, task_id: str | None = None) -> dict[str, str]:
    route = connector_route(name)
    return {
        "requested_name": name,
        "canonical": route.canonical,
        "layer": route.layer,
        "transport": route.transport,
        "status": route.status,
        "kind": route.kind,
        "task_id": task_id or "",
    }

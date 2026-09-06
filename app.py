"""Extension declaration, capabilities, health check for Autodesk Construction Cloud Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "autodesk-construction-cloud-connector",
    version="0.1.0",
    display_name="Autodesk Construction Cloud",
    icon="icon.svg",
    capabilities=["autodesk_construction_cloud:manage"],
    description="Official Imperal connector for Autodesk Construction Cloud (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("autodesk_construction_cloud_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Autodesk Construction Cloud connection(s) configured." if count else "Not connected yet."
    }

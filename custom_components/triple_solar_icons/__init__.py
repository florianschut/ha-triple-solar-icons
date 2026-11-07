"""Adds the "triple-solar:" icon set, e.g. triple-solar:pika, to the frontend."""

from pathlib import Path

from homeassistant.components.frontend import add_extra_js_url, remove_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "triple_solar_icons"
ICONS_JS_URL = f"/{DOMAIN}/triple-solar-icons.js"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Make the frontend load the icon set."""
    # Routes can't be removed again, so only register on the first setup.
    if not hass.data.get(DOMAIN):
        path = Path(__file__).parent / "frontend" / "triple-solar-icons.js"
        await hass.http.async_register_static_paths(
            [StaticPathConfig(ICONS_JS_URL, str(path), cache_headers=False)]
        )
        hass.data[DOMAIN] = True
    add_extra_js_url(hass, ICONS_JS_URL)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Stop the frontend from loading the icon set."""
    remove_extra_js_url(hass, ICONS_JS_URL)
    return True

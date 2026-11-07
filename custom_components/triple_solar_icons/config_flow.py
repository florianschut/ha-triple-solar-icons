"""Config flow: nothing to configure, adding the integration enables the icons."""

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from . import DOMAIN


class TripleSolarIconsConfigFlow(ConfigFlow, domain=DOMAIN):
    """Add the Triple Solar icons."""

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Confirm adding the icons."""
        if user_input is not None:
            return self.async_create_entry(title="Triple Solar icons", data={})
        return self.async_show_form(step_id="user")

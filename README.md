# Triple Solar icons for Home Assistant

Adds Triple Solar icons to Home Assistant, for use on entities and dashboards
next to the regular `mdi:` icons.

| Icon | Name |
| --- | --- |
| Pika | `triple-solar:pika` |

This is a companion to the [Triple Solar](https://github.com/florianschut/ha-triple-solar)
integration. That integration is meant for Home Assistant core, which only
allows Material Design Icons, so the custom icons live here. It is not made or
supported by Triple Solar.

## Installation

1. Copy `custom_components/triple_solar_icons` into your Home Assistant
   `config/custom_components` folder (or add this repository to HACS as a
   custom integration repository), then restart Home Assistant.
2. Go to **Settings > Devices & services**, select **Add integration** and add
   **Triple Solar icons**.
3. Reload the page in your browser.

## Using the icons

Enter an icon name such as `triple-solar:pika` wherever Home Assistant asks
for an icon: in an entity's settings, or as `icon:` on a dashboard card.

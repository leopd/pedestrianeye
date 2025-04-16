# Pedestrian Eye

Camera mounted on dashcam, watches for pedestrians that are obscured by the A-pillar.

## Initial Setup and Trial Run

```bash
curl -fsSL https://astral.sh/uv/install.sh | bash
source $HOME/.local/bin/env
uv sync
uv run framegrab autodiscover > camera.yaml
uv run src/watcher.py
```

## Making it run on boot:

### Using Desktop Autostart Entry (Raspberry Pi OS)

1. Install the desktop entry:

```bash
mkdir -p ~/.config/autostart/
cp pedestrian-eye.desktop ~/.config/autostart/
```

The application will now start automatically when you log in after rebooting.

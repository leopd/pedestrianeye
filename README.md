# Pedestrian Eye

Camera mounted on dashcam, watches for pedestrians that are obscured by the A-pillar.

## Setup

```bash
curl -fsSL https://astral.sh/uv/install.sh | bash
source $HOME/.local/bin/env
uv sync
uv run framegrab autodiscover > camera.yaml
uv run src/watcher.py
```
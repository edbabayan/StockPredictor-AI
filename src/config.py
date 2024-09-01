from pathlib import Path


class CFG:
    root = Path(__file__).parent.parent.absolute()
    api_key_path = root.joinpath('anthropic_api_key.json')

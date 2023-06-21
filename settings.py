from pathlib import Path
import yaml


def config():
    root_dir = Path(__file__).parent
    with open(f"{root_dir}/config/service.yml", 'r', encoding='utf-8') as file:
        return yaml.load(file.read(), Loader=yaml.BaseLoader)['environment']["prod"]
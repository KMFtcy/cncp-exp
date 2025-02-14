import yaml
from typing import Dict, Any

DEFAULT_CONFIG_FILE = 'config.yaml'

def read_config(config_file: str = DEFAULT_CONFIG_FILE) -> Dict[Any, Any]:
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{config_file}' not found")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing configuration file: {str(e)}")
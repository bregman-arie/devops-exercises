"""
Schema loader for YAML validation.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional

from .config_schema import SCHEMA_MAPPING, get_kubernetes_schema, get_ansible_schema, get_docker_compose_schema, get_exercise_schema


class SchemaLoader:
    def __init__(self, custom_schema_path: Optional[Path] = None):
        self.custom_schema_path = custom_schema_path
        self._loaded_schemas: Dict[str, Any] = {}

    def load_schema(self, schema_type: str, subtype: Optional[str] = None) -> Dict[str, Any]:
        cache_key = f"{schema_type}:{subtype}" if subtype else schema_type
        
        if cache_key in self._loaded_schemas:
            return self._loaded_schemas[cache_key]

        if schema_type == 'kubernetes':
            schema = get_kubernetes_schema(subtype)
        elif schema_type == 'ansible':
            schema = get_ansible_schema()
        elif schema_type == 'docker-compose':
            schema = get_docker_compose_schema()
        elif schema_type == 'exercise':
            schema = get_exercise_schema()
        else:
            schema = SCHEMA_MAPPING.get(schema_type, {})

        self._loaded_schemas[cache_key] = schema
        return schema

    def load_schema_from_file(self, schema_path: Path) -> Dict[str, Any]:
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_path}")

        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def detect_schema_type(self, yaml_content: Dict[str, Any]) -> str:
        if isinstance(yaml_content, list):
            if all('hosts' in item and 'tasks' in item for item in yaml_content if isinstance(item, dict)):
                return 'ansible'
        
        if isinstance(yaml_content, dict):
            if 'apiVersion' in yaml_content or 'kind' in yaml_content:
                return 'kubernetes'
            if 'services' in yaml_content or 'version' in yaml_content:
                return 'docker-compose'
            if 'exercise' in yaml_content and 'category' in yaml_content:
                return 'exercise'
            if 'hosts' in yaml_content or ('name' in yaml_content and 'tasks' in yaml_content):
                return 'ansible'

        return 'unknown'

    def get_schema_for_content(self, yaml_content: Dict[str, Any]) -> Dict[str, Any]:
        schema_type = self.detect_schema_type(yaml_content)
        
        if schema_type == 'kubernetes':
            kind = yaml_content.get('kind', 'default')
            return self.load_schema('kubernetes', kind)
        elif schema_type == 'ansible':
            return self.load_schema('ansible')
        elif schema_type == 'docker-compose':
            return self.load_schema('docker-compose')
        elif schema_type == 'exercise':
            return self.load_schema('exercise')
        
        return {}

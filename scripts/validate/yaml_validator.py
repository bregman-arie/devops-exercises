"""
YAML Validator for DevOps Exercises.

Provides validation functionality for YAML/JSON configuration files
in the exercises directory.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple, Union
from dataclasses import dataclass, field

import yaml

from .schema_loader import SchemaLoader


@dataclass
class ValidationResult:
    is_valid: bool
    file_path: str
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    schema_type: str = "unknown"

    def add_error(self, message: str):
        self.errors.append(message)
        self.is_valid = False

    def add_warning(self, message: str):
        self.warnings.append(message)

    def __str__(self) -> str:
        status = "PASSED" if self.is_valid else "FAILED"
        result = f"[{status}] {self.file_path} (type: {self.schema_type})"
        if self.errors:
            result += f"\n  Errors: {len(self.errors)}"
            for error in self.errors:
                result += f"\n    - {error}"
        if self.warnings:
            result += f"\n  Warnings: {len(self.warnings)}"
            for warning in self.warnings:
                result += f"\n    - {warning}"
        return result


class YAMLValidator:
    def __init__(self, schema_loader: Optional[SchemaLoader] = None):
        self.schema_loader = schema_loader or SchemaLoader()
        self.results: List[ValidationResult] = []

    def validate_yaml_syntax(self, file_path: Path) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
            return True, content, None
        except yaml.YAMLError as e:
            return False, None, str(e)
        except Exception as e:
            return False, None, str(e)

    def validate_json_syntax(self, file_path: Path) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
            return True, content, None
        except json.JSONDecodeError as e:
            return False, None, str(e)
        except Exception as e:
            return False, None, str(e)

    def validate_schema(self, content: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
        errors = []
        self._validate_recursive(content, schema, errors, path="")
        return errors

    def _validate_recursive(self, content: Any, schema: Dict[str, Any], errors: List[str], path: str):
        if not schema:
            return

        if 'required' in schema:
            for required_field in schema['required']:
                if isinstance(content, dict) and required_field not in content:
                    errors.append(f"Missing required field: {path}.{required_field}" if path else f"Missing required field: {required_field}")

        if 'type' in schema:
            expected_type = schema['type']
            if not self._check_type(content, expected_type):
                errors.append(f"Type mismatch at {path}: expected {expected_type}, got {type(content).__name__}")
                return

        if 'properties' in schema and isinstance(content, dict):
            for prop_name, prop_schema in schema['properties'].items():
                if prop_name in content:
                    new_path = f"{path}.{prop_name}" if path else prop_name
                    self._validate_recursive(content[prop_name], prop_schema, errors, new_path)

        if 'items' in schema and isinstance(content, list):
            for idx, item in enumerate(content):
                new_path = f"{path}[{idx}]"
                self._validate_recursive(item, schema['items'], errors, new_path)

        if 'additionalProperties' in schema and isinstance(content, dict):
            additional_schema = schema['additionalProperties']
            for key, value in content.items():
                if 'properties' not in schema or key not in schema['properties']:
                    new_path = f"{path}.{key}" if path else key
                    self._validate_recursive(value, additional_schema, errors, new_path)

        if 'enum' in schema:
            if content not in schema['enum']:
                errors.append(f"Invalid value at {path}: {content}. Must be one of {schema['enum']}")

        if 'const' in schema:
            if content != schema['const']:
                errors.append(f"Invalid value at {path}: expected {schema['const']}, got {content}")

    def _check_type(self, value: Any, expected_type: Union[str, List[str]]) -> bool:
        if isinstance(expected_type, list):
            return any(self._check_type(value, t) for t in expected_type)

        type_mapping = {
            'string': str,
            'integer': int,
            'number': (int, float),
            'boolean': bool,
            'array': list,
            'object': dict,
            'null': type(None)
        }

        expected_python_type = type_mapping.get(expected_type)
        if expected_python_type is None:
            return True

        if expected_type == 'integer':
            return isinstance(value, int) and not isinstance(value, bool)
        if expected_type == 'number':
            return isinstance(value, (int, float)) and not isinstance(value, bool)

        return isinstance(value, expected_python_type)

    def validate_kubernetes_yaml(self, content: Dict[str, Any]) -> List[str]:
        errors = []
        
        if 'apiVersion' not in content:
            errors.append("Missing required field: apiVersion")
        if 'kind' not in content:
            errors.append("Missing required field: kind")
        if 'metadata' not in content:
            errors.append("Missing required field: metadata")
        elif not isinstance(content.get('metadata'), dict):
            errors.append("metadata must be an object")
        elif 'name' not in content['metadata']:
            errors.append("Missing required field: metadata.name")
        
        if 'spec' not in content:
            errors.append("Missing required field: spec")

        return errors

    def validate_ansible_yaml(self, content: Union[List, Dict]) -> List[str]:
        errors = []
        
        if not isinstance(content, list):
            errors.append("Ansible playbook must be a list of plays")
            return errors

        for idx, play in enumerate(content):
            if not isinstance(play, dict):
                errors.append(f"Play {idx} must be an object")
                continue
            
            if 'name' not in play:
                errors.append(f"Play {idx}: Missing required field 'name'")
            if 'hosts' not in play:
                errors.append(f"Play {idx}: Missing required field 'hosts'")

        return errors

    def validate_docker_compose_yaml(self, content: Dict[str, Any]) -> List[str]:
        errors = []
        
        if 'services' not in content:
            errors.append("Missing required field: services")
            return errors

        if not isinstance(content.get('services'), dict):
            errors.append("services must be an object")
            return errors

        for service_name, service_config in content['services'].items():
            if not isinstance(service_config, dict):
                errors.append(f"Service '{service_name}' must be an object")
                continue
            
            if 'image' not in service_config and 'build' not in service_config:
                errors.append(f"Service '{service_name}': Missing 'image' or 'build' field")

        return errors

    def validate_file(self, file_path: Path) -> ValidationResult:
        result = ValidationResult(is_valid=True, file_path=str(file_path))

        suffix = file_path.suffix.lower()
        
        if suffix in ['.yaml', '.yml']:
            is_valid, content, error = self.validate_yaml_syntax(file_path)
            if not is_valid:
                result.add_error(f"YAML syntax error: {error}")
                return result
        elif suffix == '.json':
            is_valid, content, error = self.validate_json_syntax(file_path)
            if not is_valid:
                result.add_error(f"JSON syntax error: {error}")
                return result
        else:
            result.add_error(f"Unsupported file type: {suffix}")
            return result

        if content is None:
            result.add_warning("File is empty")
            return result

        schema_type = self.schema_loader.detect_schema_type(content)
        result.schema_type = schema_type

        if schema_type == 'kubernetes':
            errors = self.validate_kubernetes_yaml(content)
        elif schema_type == 'ansible':
            errors = self.validate_ansible_yaml(content)
        elif schema_type == 'docker-compose':
            errors = self.validate_docker_compose_yaml(content)
        else:
            result.add_warning(f"Unknown schema type for validation")
            return result

        for error in errors:
            result.add_error(error)

        return result

    def validate_directory(self, directory: Path, recursive: bool = True) -> List[ValidationResult]:
        results = []
        
        if not directory.exists():
            result = ValidationResult(is_valid=False, file_path=str(directory))
            result.add_error(f"Directory does not exist: {directory}")
            results.append(result)
            return results

        patterns = ['*.yaml', '*.yml', '*.json']
        
        for pattern in patterns:
            if recursive:
                files = list(directory.rglob(pattern))
            else:
                files = list(directory.glob(pattern))
            
            for file_path in files:
                result = self.validate_file(file_path)
                results.append(result)

        self.results.extend(results)
        return results

    def get_summary(self) -> Dict[str, Any]:
        total = len(self.results)
        passed = sum(1 for r in self.results if r.is_valid)
        failed = total - passed
        
        return {
            'total': total,
            'passed': passed,
            'failed': failed,
            'success_rate': (passed / total * 100) if total > 0 else 0
        }


def validate_yaml_file(file_path: Union[str, Path]) -> ValidationResult:
    validator = YAMLValidator()
    return validator.validate_file(Path(file_path))


def validate_all_yaml_files(directory: Union[str, Path], recursive: bool = True) -> List[ValidationResult]:
    validator = YAMLValidator()
    return validator.validate_directory(Path(directory), recursive=recursive)


def validate_exercises_directory() -> List[ValidationResult]:
    project_root = Path(__file__).parent.parent.parent
    exercises_dir = project_root / "exercises"
    return validate_all_yaml_files(exercises_dir)

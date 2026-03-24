"""
Test cases for YAML/JSON validation scripts.

This module tests the validation functionality for exercises directory
YAML and JSON configuration files.
"""

import json
import tempfile
from pathlib import Path
from unittest import TestCase

from scripts.validate import (
    YAMLValidator,
    validate_yaml_file,
    validate_all_yaml_files,
    SchemaLoader,
    get_kubernetes_schema,
    get_ansible_schema,
    get_docker_compose_schema,
)
from scripts.validate.yaml_validator import ValidationResult


class TestSchemaLoader(TestCase):
    def setUp(self):
        self.loader = SchemaLoader()

    def test_load_kubernetes_schema(self):
        schema = self.loader.load_schema('kubernetes', 'Deployment')
        self.assertIn('required', schema)
        self.assertIn('apiVersion', schema['required'])
        self.assertIn('kind', schema['required'])

    def test_load_ansible_schema(self):
        schema = self.loader.load_schema('ansible')
        self.assertEqual(schema['type'], 'array')

    def test_load_docker_compose_schema(self):
        schema = self.loader.load_schema('docker-compose')
        self.assertIn('services', schema['required'])

    def test_detect_kubernetes_schema_type(self):
        content = {
            'apiVersion': 'apps/v1',
            'kind': 'Deployment',
            'metadata': {'name': 'test'},
            'spec': {}
        }
        schema_type = self.loader.detect_schema_type(content)
        self.assertEqual(schema_type, 'kubernetes')

    def test_detect_ansible_schema_type(self):
        content = [
            {'name': 'test', 'hosts': 'localhost', 'tasks': []}
        ]
        schema_type = self.loader.detect_schema_type(content)
        self.assertEqual(schema_type, 'ansible')

    def test_detect_docker_compose_schema_type(self):
        content = {
            'version': '3.8',
            'services': {'web': {'image': 'nginx'}}
        }
        schema_type = self.loader.detect_schema_type(content)
        self.assertEqual(schema_type, 'docker-compose')


class TestValidationResult(TestCase):
    def test_initial_state(self):
        result = ValidationResult(is_valid=True, file_path='test.yaml')
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.warnings), 0)

    def test_add_error(self):
        result = ValidationResult(is_valid=True, file_path='test.yaml')
        result.add_error('Test error')
        self.assertFalse(result.is_valid)
        self.assertEqual(len(result.errors), 1)
        self.assertIn('Test error', result.errors)

    def test_add_warning(self):
        result = ValidationResult(is_valid=True, file_path='test.yaml')
        result.add_warning('Test warning')
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.warnings), 1)


class TestYAMLValidator(TestCase):
    def setUp(self):
        self.validator = YAMLValidator()
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _create_temp_file(self, content, filename, suffix='.yaml'):
        file_path = Path(self.test_dir) / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path

    def test_validate_valid_kubernetes_deployment(self):
        content = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: test
"""
        file_path = self._create_temp_file(content, 'deployment.yaml')
        result = self.validator.validate_file(file_path)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.schema_type, 'kubernetes')

    def test_validate_valid_kubernetes_service(self):
        content = """
apiVersion: v1
kind: Service
metadata:
  name: test-service
spec:
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: test
"""
        file_path = self._create_temp_file(content, 'service.yaml')
        result = self.validator.validate_file(file_path)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.schema_type, 'kubernetes')

    def test_validate_invalid_kubernetes_missing_api_version(self):
        content = """
kind: Deployment
metadata:
  name: test-deployment
spec:
  replicas: 1
"""
        file_path = self._create_temp_file(content, 'invalid_deployment.yaml')
        result = self.validator.validate_file(file_path)
        self.assertFalse(result.is_valid)
        self.assertTrue(any('apiVersion' in e for e in result.errors))

    def test_validate_invalid_kubernetes_missing_kind(self):
        content = """
apiVersion: apps/v1
metadata:
  name: test-deployment
spec:
  replicas: 1
"""
        file_path = self._create_temp_file(content, 'invalid_deployment2.yaml')
        result = self.validator.validate_file(file_path)
        self.assertFalse(result.is_valid)
        self.assertTrue(any('kind' in e for e in result.errors))

    def test_validate_valid_ansible_playbook(self):
        content = """
- name: Test playbook
  hosts: localhost
  tasks:
    - name: Test task
      debug:
        msg: "Hello"
"""
        file_path = self._create_temp_file(content, 'playbook.yaml')
        result = self.validator.validate_file(file_path)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.schema_type, 'ansible')

    def test_validate_invalid_ansible_not_list(self):
        content = """
name: Test playbook
hosts: localhost
tasks: []
"""
        file_path = self._create_temp_file(content, 'invalid_playbook.yaml')
        result = self.validator.validate_file(file_path)
        self.assertFalse(result.is_valid)

    def test_validate_valid_docker_compose(self):
        content = """
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
"""
        file_path = self._create_temp_file(content, 'docker-compose.yaml')
        result = self.validator.validate_file(file_path)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.schema_type, 'docker-compose')

    def test_validate_invalid_docker_compose_missing_services(self):
        content = """
version: '3.8'
"""
        file_path = self._create_temp_file(content, 'invalid_compose.yaml')
        result = self.validator.validate_file(file_path)
        self.assertFalse(result.is_valid)

    def test_validate_yaml_syntax_error(self):
        content = """
invalid: yaml: content:
  - broken
    - indentation
"""
        file_path = self._create_temp_file(content, 'syntax_error.yaml')
        result = self.validator.validate_file(file_path)
        self.assertFalse(result.is_valid)
        self.assertTrue(any('syntax error' in e.lower() for e in result.errors))

    def test_validate_json_file(self):
        content = '{"test": "value"}'
        file_path = self._create_temp_file(content, 'test.json', '.json')
        result = self.validator.validate_file(file_path)
        self.assertTrue(result.is_valid)

    def test_validate_invalid_json_file(self):
        content = '{invalid json}'
        file_path = self._create_temp_file(content, 'invalid.json', '.json')
        result = self.validator.validate_file(file_path)
        self.assertFalse(result.is_valid)
        self.assertTrue(any('JSON' in e for e in result.errors))

    def test_validate_empty_yaml_file(self):
        content = ""
        file_path = self._create_temp_file(content, 'empty.yaml')
        result = self.validator.validate_file(file_path)
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.warnings), 1)

    def test_validate_directory(self):
        valid_content = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test
spec:
  replicas: 1
"""
        invalid_content = """
kind: Deployment
metadata:
  name: test
"""
        self._create_temp_file(valid_content, 'valid.yaml')
        self._create_temp_file(invalid_content, 'invalid.yaml')

        results = self.validator.validate_directory(Path(self.test_dir))
        self.assertEqual(len(results), 2)

    def test_get_summary(self):
        content = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test
spec:
  replicas: 1
"""
        self._create_temp_file(content, 'test.yaml')
        self.validator.validate_directory(Path(self.test_dir))
        summary = self.validator.get_summary()
        self.assertIn('total', summary)
        self.assertIn('passed', summary)
        self.assertIn('failed', summary)


class TestValidateYAMLFile(TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_validate_yaml_file_function(self):
        file_path = Path(self.test_dir) / 'test.yaml'
        content = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test
spec:
  replicas: 1
"""
        with open(file_path, 'w') as f:
            f.write(content)

        result = validate_yaml_file(file_path)
        self.assertIsInstance(result, ValidationResult)
        self.assertTrue(result.is_valid)


class TestValidateAllYAMLFiles(TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_validate_all_yaml_files(self):
        file_path = Path(self.test_dir) / 'test.yaml'
        content = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test
spec:
  replicas: 1
"""
        with open(file_path, 'w') as f:
            f.write(content)

        results = validate_all_yaml_files(self.test_dir)
        self.assertEqual(len(results), 1)
        self.assertTrue(results[0].is_valid)


class TestExercisesDirectoryValidation(TestCase):
    def test_validate_exercises_directory(self):
        from scripts.validate.yaml_validator import validate_exercises_directory
        results = validate_exercises_directory()
        self.assertIsInstance(results, list)
        for result in results:
            self.assertIsInstance(result, ValidationResult)


class TestSchemaFunctions(TestCase):
    def test_get_kubernetes_schema_deployment(self):
        schema = get_kubernetes_schema('Deployment')
        self.assertIn('required', schema)

    def test_get_kubernetes_schema_service(self):
        schema = get_kubernetes_schema('Service')
        self.assertIn('required', schema)

    def test_get_ansible_schema(self):
        schema = get_ansible_schema()
        self.assertEqual(schema['type'], 'array')

    def test_get_docker_compose_schema(self):
        schema = get_docker_compose_schema()
        self.assertIn('services', schema['required'])


class TestTypeChecking(TestCase):
    def setUp(self):
        self.validator = YAMLValidator()

    def test_check_type_string(self):
        self.assertTrue(self.validator._check_type("test", "string"))

    def test_check_type_integer(self):
        self.assertTrue(self.validator._check_type(42, "integer"))
        self.assertFalse(self.validator._check_type(42.5, "integer"))

    def test_check_type_boolean(self):
        self.assertTrue(self.validator._check_type(True, "boolean"))
        self.assertTrue(self.validator._check_type(False, "boolean"))

    def test_check_type_array(self):
        self.assertTrue(self.validator._check_type([1, 2, 3], "array"))

    def test_check_type_object(self):
        self.assertTrue(self.validator._check_type({"key": "value"}, "object"))

    def test_check_type_multiple(self):
        self.assertTrue(self.validator._check_type("test", ["string", "integer"]))
        self.assertTrue(self.validator._check_type(42, ["string", "integer"]))

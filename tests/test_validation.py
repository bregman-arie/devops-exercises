"""
Test suite for YAML/JSON validation scripts.

This test suite verifies the functionality of the validation scripts
in scripts/validate/ directory.
"""

import os
import sys
import tempfile
import pathlib
import pytest

# Add the project root to Python path
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from scripts.validate.validator import (
    validate_yaml_file,
    validate_json_file,
    validate_all_yaml_files,
    validate_all_json_files,
    YAMLValidationError,
)


class TestYAMLValidation:
    """Test cases for YAML file validation."""

    def test_valid_yaml_file(self):
        """Test validation of a valid YAML file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write("""
apiVersion: v1
kind: ConfigMap
metadata:
  name: test-config
data:
  key: value
""")
            temp_file = pathlib.Path(f.name)
        
        try:
            is_valid, errors = validate_yaml_file(temp_file)
            assert is_valid is True
            assert len(errors) == 0
        finally:
            os.unlink(temp_file)

    def test_invalid_yaml_file(self):
        """Test validation of an invalid YAML file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write("""
apiVersion: v1
kind: ConfigMap
metadata:
  name: test-config
data:
  key: value
invalid: [missing space after colon
""")
            temp_file = pathlib.Path(f.name)
        
        try:
            is_valid, errors = validate_yaml_file(temp_file)
            assert is_valid is False
            assert len(errors) > 0
        finally:
            os.unlink(temp_file)

    def test_valid_multi_document_yaml(self):
        """Test validation of a valid multi-document YAML file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write("""
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: config1
---
apiVersion: v1
kind: Secret
metadata:
  name: secret1
""")
            temp_file = pathlib.Path(f.name)
        
        try:
            is_valid, errors = validate_yaml_file(temp_file)
            assert is_valid is True
            assert len(errors) == 0
        finally:
            os.unlink(temp_file)

    def test_empty_yaml_file(self):
        """Test validation of an empty YAML file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write("")
            temp_file = pathlib.Path(f.name)
        
        try:
            is_valid, errors = validate_yaml_file(temp_file)
            assert is_valid is True  # Empty YAML is technically valid
            assert len(errors) == 0
        finally:
            os.unlink(temp_file)


class TestJSONValidation:
    """Test cases for JSON file validation."""

    def test_valid_json_file(self):
        """Test validation of a valid JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("""
{
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata": {
    "name": "test-config"
  },
  "data": {
    "key": "value"
  }
}
""")
            temp_file = pathlib.Path(f.name)
        
        try:
            is_valid, errors = validate_json_file(temp_file)
            assert is_valid is True
            assert len(errors) == 0
        finally:
            os.unlink(temp_file)

    def test_invalid_json_file(self):
        """Test validation of an invalid JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("""
{
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata": {
    "name": "test-config"
  },
  "data": {
    "key": "value"
  }
  missing_comma: "error"
}
""")
            temp_file = pathlib.Path(f.name)
        
        try:
            is_valid, errors = validate_json_file(temp_file)
            assert is_valid is False
            assert len(errors) > 0
        finally:
            os.unlink(temp_file)


class TestAllFilesValidation:
    """Test cases for validating all files in a directory."""

    def test_validate_all_yaml_in_directory(self):
        """Test validating all YAML files in a directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = pathlib.Path(tmpdir)
            
            # Create a valid YAML file
            with open(tmp_path / "valid.yml", 'w') as f:
                f.write("key: value\n")
            
            # Create a subdirectory with another valid YAML file
            subdir = tmp_path / "subdir"
            subdir.mkdir()
            with open(subdir / "valid2.yaml", 'w') as f:
                f.write("another: value\n")
            
            all_valid, errors = validate_all_yaml_files(tmp_path)
            assert all_valid is True
            assert len(errors) == 0

    def test_validate_all_yaml_with_invalid(self):
        """Test validating all YAML files with one invalid file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = pathlib.Path(tmpdir)

            # Create a valid YAML file
            with open(tmp_path / "valid.yml", 'w') as f:
                f.write("key: value\n")

            # Create an invalid YAML file - unmatched bracket
            with open(tmp_path / "invalid.yml", 'w') as f:
                f.write("key: value\ninvalid: [unclosed bracket\n")

            all_valid, errors = validate_all_yaml_files(tmp_path)
            assert all_valid is False
            assert len(errors) > 0

    def test_validate_all_json_in_directory(self):
        """Test validating all JSON files in a directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = pathlib.Path(tmpdir)
            
            # Create a valid JSON file
            with open(tmp_path / "valid.json", 'w') as f:
                f.write('{"key": "value"}\n')
            
            all_valid, errors = validate_all_json_files(tmp_path)
            assert all_valid is True
            assert len(errors) == 0


class TestModuleImport:
    """Test cases for module imports."""

    def test_import_validator_module(self):
        """Test that the validator module can be imported."""
        from scripts.validate import validator
        assert validator is not None

    def test_import_all_symbols(self):
        """Test that all symbols are exported correctly."""
        from scripts.validate import (
            validate_yaml_file,
            validate_all_yaml_files,
            YAMLValidationError,
        )
        assert validate_yaml_file is not None
        assert validate_all_yaml_files is not None
        assert YAMLValidationError is not None


class TestExistingYAMLFiles:
    """Test validation of existing YAML files in the repository."""

    def test_existing_yaml_files_are_valid(self):
        """Test that all existing YAML files in the repository are valid."""
        # This tests against the actual files in the repository
        all_valid, errors = validate_all_yaml_files()
        
        if not all_valid:
            print("\nExisting YAML validation errors:")
            for file_path, errs in errors.items():
                print(f"\n  {file_path}:")
                for err in errs:
                    print(f"    - {err}")
        
        assert all_valid is True, f"YAML validation failed with errors: {errors}"

    def test_existing_json_files_are_valid(self):
        """Test that all existing JSON files in the repository are valid."""
        # This tests against the actual files in the repository
        all_valid, errors = validate_all_json_files()
        
        if not all_valid:
            print("\nExisting JSON validation errors:")
            for file_path, errs in errors.items():
                print(f"\n  {file_path}:")
                for err in errs:
                    print(f"    - {err}")
        
        assert all_valid is True, f"JSON validation failed with errors: {errors}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

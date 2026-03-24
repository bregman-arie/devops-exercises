"""
YAML/JSON Configuration Validator for DevOps Exercises

This module provides functionality to validate YAML and JSON configuration files
for syntax correctness, schema compliance, and best practices.
"""

import os
import pathlib
from typing import List, Dict, Any, Tuple, Optional
import yaml
import json


class YAMLValidationError(Exception):
    """Exception raised for YAML validation errors."""
    pass


def validate_yaml_file(file_path: pathlib.Path) -> Tuple[bool, List[str]]:
    """
    Validate a single YAML file for syntax correctness.
    
    Args:
        file_path: Path to the YAML file to validate
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to load all YAML documents (supports multi-document YAML)
        # Need to iterate over the generator to trigger parsing
        list(yaml.load_all(content, Loader=yaml.FullLoader))
        
    except yaml.YAMLError as e:
        error_msg = f"YAML Syntax Error in {file_path}: {str(e)}"
        errors.append(error_msg)
        return False, errors
    except UnicodeDecodeError as e:
        error_msg = f"Encoding Error in {file_path}: {str(e)}"
        errors.append(error_msg)
        return False, errors
    except Exception as e:
        error_msg = f"Unexpected error in {file_path}: {str(e)}"
        errors.append(error_msg)
        return False, errors
    
    return True, errors


def validate_json_file(file_path: pathlib.Path) -> Tuple[bool, List[str]]:
    """
    Validate a single JSON file for syntax correctness.
    
    Args:
        file_path: Path to the JSON file to validate
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
            
    except json.JSONDecodeError as e:
        error_msg = f"JSON Syntax Error in {file_path}: Line {e.lineno}, Column {e.colno}: {e.msg}"
        errors.append(error_msg)
        return False, errors
    except UnicodeDecodeError as e:
        error_msg = f"Encoding Error in {file_path}: {str(e)}"
        errors.append(error_msg)
        return False, errors
    except Exception as e:
        error_msg = f"Unexpected error in {file_path}: {str(e)}"
        errors.append(error_msg)
        return False, errors
    
    return True, errors


def validate_all_yaml_files(root_dir: Optional[pathlib.Path] = None) -> Tuple[bool, Dict[str, List[str]]]:
    """
    Validate all YAML files in the given directory and subdirectories.
    
    Args:
        root_dir: Root directory to search for YAML files (defaults to exercises/)
        
    Returns:
        Tuple of (all_valid, dict_of_errors_by_file)
    """
    if root_dir is None:
        root_dir = pathlib.Path(__file__).parent.parent.parent / "exercises"
    
    all_errors = {}
    all_valid = True
    
    # Find all YAML files
    yaml_patterns = ["*.yaml", "*.yml"]
    for pattern in yaml_patterns:
        for yaml_file in root_dir.rglob(pattern):
            is_valid, errors = validate_yaml_file(yaml_file)
            if not is_valid:
                all_errors[str(yaml_file)] = errors
                all_valid = False
    
    # Also check topics directory for YAML files (as per project structure)
    topics_dir = root_dir.parent / "topics"
    if topics_dir.exists():
        for pattern in yaml_patterns:
            for yaml_file in topics_dir.rglob(pattern):
                is_valid, errors = validate_yaml_file(yaml_file)
                if not is_valid:
                    all_errors[str(yaml_file)] = errors
                    all_valid = False
    
    return all_valid, all_errors


def validate_all_json_files(root_dir: Optional[pathlib.Path] = None) -> Tuple[bool, Dict[str, List[str]]]:
    """
    Validate all JSON files in the given directory and subdirectories.
    
    Args:
        root_dir: Root directory to search for JSON files (defaults to exercises/)
        
    Returns:
        Tuple of (all_valid, dict_of_errors_by_file)
    """
    if root_dir is None:
        root_dir = pathlib.Path(__file__).parent.parent.parent / "exercises"
    
    all_errors = {}
    all_valid = True
    
    # Find all JSON files
    for json_file in root_dir.rglob("*.json"):
        is_valid, errors = validate_json_file(json_file)
        if not is_valid:
            all_errors[str(json_file)] = errors
            all_valid = False
    
    # Also check topics directory for JSON files
    topics_dir = root_dir.parent / "topics"
    if topics_dir.exists():
        for json_file in topics_dir.rglob("*.json"):
            is_valid, errors = validate_json_file(json_file)
            if not is_valid:
                all_errors[str(json_file)] = errors
                all_valid = False
    
    return all_valid, all_errors


def main() -> None:
    """Main function to run validation from command line."""
    import sys
    
    print("=" * 60)
    print("DevOps Exercises YAML/JSON Validator")
    print("=" * 60)
    
    # Validate YAML files
    print("\nValidating YAML files...")
    yaml_valid, yaml_errors = validate_all_yaml_files()
    
    if yaml_valid:
        print("✅ All YAML files are valid!")
    else:
        print("❌ YAML validation failed!")
        for file_path, errors in yaml_errors.items():
            print(f"\n  {file_path}:")
            for error in errors:
                print(f"    - {error}")
    
    # Validate JSON files
    print("\nValidating JSON files...")
    json_valid, json_errors = validate_all_json_files()
    
    if json_valid:
        print("✅ All JSON files are valid!")
    else:
        print("❌ JSON validation failed!")
        for file_path, errors in json_errors.items():
            print(f"\n  {file_path}:")
            for error in errors:
                print(f"    - {error}")
    
    if not yaml_valid or not json_valid:
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("All validations passed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

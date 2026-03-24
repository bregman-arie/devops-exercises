#!/usr/bin/env python3
"""
Command Line Interface for YAML/JSON Validation
"""

import argparse
import pathlib
import sys
from .validator import (
    validate_yaml_file,
    validate_json_file,
    validate_all_yaml_files,
    validate_all_json_files,
)


def main():
    parser = argparse.ArgumentParser(
        description="Validate YAML and JSON files for DevOps Exercises"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Validate all files
    validate_all_parser = subparsers.add_parser(
        "all", help="Validate all YAML and JSON files"
    )
    validate_all_parser.add_argument(
        "--dir",
        type=str,
        help="Root directory to search for files (default: exercises/)",
    )
    
    # Validate single file
    validate_file_parser = subparsers.add_parser(
        "file", help="Validate a single YAML or JSON file"
    )
    validate_file_parser.add_argument(
        "file_path", type=str, help="Path to the file to validate"
    )
    
    # Validate YAML files only
    validate_yaml_parser = subparsers.add_parser(
        "yaml", help="Validate all YAML files"
    )
    validate_yaml_parser.add_argument(
        "--dir",
        type=str,
        help="Root directory to search for YAML files (default: exercises/)",
    )
    
    # Validate JSON files only
    validate_json_parser = subparsers.add_parser(
        "json", help="Validate all JSON files"
    )
    validate_json_parser.add_argument(
        "--dir",
        type=str,
        help="Root directory to search for JSON files (default: exercises/)",
    )
    
    args = parser.parse_args()
    
    if args.command == "all":
        root_dir = pathlib.Path(args.dir) if args.dir else None
        print("=" * 60)
        print("Validating all YAML and JSON files...")
        print("=" * 60)
        
        yaml_valid, yaml_errors = validate_all_yaml_files(root_dir)
        json_valid, json_errors = validate_all_json_files(root_dir)
        
        if yaml_valid:
            print("\n✅ All YAML files are valid!")
        else:
            print("\n❌ YAML validation failed!")
            for file_path, errors in yaml_errors.items():
                print(f"\n  {file_path}:")
                for error in errors:
                    print(f"    - {error}")
        
        if json_valid:
            print("\n✅ All JSON files are valid!")
        else:
            print("\n❌ JSON validation failed!")
            for file_path, errors in json_errors.items():
                print(f"\n  {file_path}:")
                for error in errors:
                    print(f"    - {error}")
        
        if not yaml_valid or not json_valid:
            sys.exit(1)
            
    elif args.command == "file":
        file_path = pathlib.Path(args.file_path)
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            sys.exit(1)
        
        print(f"Validating file: {file_path}")
        print("-" * 60)
        
        if file_path.suffix.lower() in (".yaml", ".yml"):
            is_valid, errors = validate_yaml_file(file_path)
        elif file_path.suffix.lower() == ".json":
            is_valid, errors = validate_json_file(file_path)
        else:
            print(f"❌ Unsupported file type: {file_path.suffix}")
            sys.exit(1)
        
        if is_valid:
            print("✅ File is valid!")
        else:
            print("❌ Validation failed!")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
            
    elif args.command == "yaml":
        root_dir = pathlib.Path(args.dir) if args.dir else None
        print("=" * 60)
        print("Validating YAML files...")
        print("=" * 60)
        
        yaml_valid, yaml_errors = validate_all_yaml_files(root_dir)
        
        if yaml_valid:
            print("\n✅ All YAML files are valid!")
        else:
            print("\n❌ YAML validation failed!")
            for file_path, errors in yaml_errors.items():
                print(f"\n  {file_path}:")
                for error in errors:
                    print(f"    - {error}")
            sys.exit(1)
            
    elif args.command == "json":
        root_dir = pathlib.Path(args.dir) if args.dir else None
        print("=" * 60)
        print("Validating JSON files...")
        print("=" * 60)
        
        json_valid, json_errors = validate_all_json_files(root_dir)
        
        if json_valid:
            print("\n✅ All JSON files are valid!")
        else:
            print("\n❌ JSON validation failed!")
            for file_path, errors in json_errors.items():
                print(f"\n  {file_path}:")
                for error in errors:
                    print(f"    - {error}")
            sys.exit(1)
            
    else:
        parser.print_help()
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Validation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

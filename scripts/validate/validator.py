"""
自动化答案验证脚本 - 支持批量检查YAML/JSON配置正确性

此模块提供对 exercises/ 目录下所有YAML/JSON文件的schema验证功能
"""

import json
import yaml
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class ValidationStatus(Enum):
    """验证状态枚举"""
    VALID = "valid"
    INVALID = "invalid"
    ERROR = "error"


@dataclass
class ValidationResult:
    """验证结果数据类"""
    file_path: Path
    status: ValidationStatus
    message: str = ""
    errors: List[str] = None

    def __post_init__(self):
        if self.errors is None:
            self.errors = []


class ConfigValidator:
    """
    配置验证器类 - 用于验证YAML和JSON文件的结构正确性
    """

    def __init__(self, exercises_path: Optional[Path] = None):
        """
        初始化验证器

        Args:
            exercises_path: exercises目录路径，默认为项目根目录下的exercises/
        """
        if exercises_path is None:
            self.exercises_path = Path(__file__).parent.parent.parent / "exercises"
        else:
            self.exercises_path = Path(exercises_path)

    def find_yaml_files(self) -> List[Path]:
        """
        查找exercises/目录下的所有YAML文件（包括.yml和.yaml）

        Returns:
            List[Path]: YAML文件路径列表
        """
        yaml_files = []
        if self.exercises_path.exists():
            yaml_files.extend(self.exercises_path.rglob("*.yml"))
            yaml_files.extend(self.exercises_path.rglob("*.yaml"))
        return yaml_files

    def find_json_files(self) -> List[Path]:
        """
        查找exercises/目录下的所有JSON文件

        Returns:
            List[Path]: JSON文件路径列表
        """
        json_files = []
        if self.exercises_path.exists():
            json_files.extend(self.exercises_path.rglob("*.json"))
        return json_files

    def validate_yaml_file(self, file_path: Path) -> ValidationResult:
        """
        验证单个YAML文件（支持多文档YAML）

        Args:
            file_path: YAML文件路径

        Returns:
            ValidationResult: 验证结果
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 尝试解析YAML（支持多文档）
            documents = list(yaml.safe_load_all(content))

            # 检查是否有至少一个非空文档
            valid_docs = [doc for doc in documents if doc is not None]

            if not valid_docs and content.strip():
                return ValidationResult(
                    file_path=file_path,
                    status=ValidationStatus.INVALID,
                    message="YAML file contains no valid documents",
                    errors=["No valid YAML documents found"]
                )

            return ValidationResult(
                file_path=file_path,
                status=ValidationStatus.VALID,
                message=f"YAML syntax is valid ({len(valid_docs)} document(s))"
            )
        except yaml.YAMLError as e:
            return ValidationResult(
                file_path=file_path,
                status=ValidationStatus.INVALID,
                message=f"YAML parsing error: {str(e)}",
                errors=[str(e)]
            )
        except Exception as e:
            return ValidationResult(
                file_path=file_path,
                status=ValidationStatus.ERROR,
                message=f"Error reading file: {str(e)}",
                errors=[str(e)]
            )

    def validate_json_file(self, file_path: Path) -> ValidationResult:
        """
        验证单个JSON文件

        Args:
            file_path: JSON文件路径

        Returns:
            ValidationResult: 验证结果
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 尝试解析JSON
            json.loads(content)

            return ValidationResult(
                file_path=file_path,
                status=ValidationStatus.VALID,
                message="JSON syntax is valid"
            )
        except json.JSONDecodeError as e:
            return ValidationResult(
                file_path=file_path,
                status=ValidationStatus.INVALID,
                message=f"JSON parsing error: {str(e)}",
                errors=[str(e)]
            )
        except Exception as e:
            return ValidationResult(
                file_path=file_path,
                status=ValidationStatus.ERROR,
                message=f"Error reading file: {str(e)}",
                errors=[str(e)]
            )

    def validate_all_yaml(self) -> List[ValidationResult]:
        """
        批量验证所有YAML文件

        Returns:
            List[ValidationResult]: 所有YAML文件的验证结果列表
        """
        yaml_files = self.find_yaml_files()
        results = []
        for file_path in yaml_files:
            result = self.validate_yaml_file(file_path)
            results.append(result)
        return results

    def validate_all_json(self) -> List[ValidationResult]:
        """
        批量验证所有JSON文件

        Returns:
            List[ValidationResult]: 所有JSON文件的验证结果列表
        """
        json_files = self.find_json_files()
        results = []
        for file_path in json_files:
            result = self.validate_json_file(file_path)
            results.append(result)
        return results

    def validate_all(self) -> Dict[str, List[ValidationResult]]:
        """
        验证所有YAML和JSON文件

        Returns:
            Dict[str, List[ValidationResult]]: 包含yaml和json验证结果的字典
        """
        return {
            "yaml": self.validate_all_yaml(),
            "json": self.validate_all_json()
        }

    def get_summary(self, results: Dict[str, List[ValidationResult]]) -> Dict[str, Any]:
        """
        获取验证结果汇总

        Args:
            results: validate_all()返回的验证结果

        Returns:
            Dict[str, Any]: 汇总统计信息
        """
        summary = {
            "total_files": 0,
            "valid_files": 0,
            "invalid_files": 0,
            "error_files": 0,
            "yaml_count": len(results.get("yaml", [])),
            "json_count": len(results.get("json", []))
        }

        for file_type, file_results in results.items():
            for result in file_results:
                summary["total_files"] += 1
                if result.status == ValidationStatus.VALID:
                    summary["valid_files"] += 1
                elif result.status == ValidationStatus.INVALID:
                    summary["invalid_files"] += 1
                elif result.status == ValidationStatus.ERROR:
                    summary["error_files"] += 1

        return summary


def validate_exercises(exercises_path: Optional[Path] = None) -> Tuple[bool, Dict[str, Any]]:
    """
    验证exercises目录下的所有配置文件

    Args:
        exercises_path: exercises目录路径，可选

    Returns:
        Tuple[bool, Dict[str, Any]]: (是否全部通过, 详细结果)
    """
    validator = ConfigValidator(exercises_path)
    results = validator.validate_all()
    summary = validator.get_summary(results)

    all_valid = summary["invalid_files"] == 0 and summary["error_files"] == 0

    return all_valid, {
        "summary": summary,
        "results": results
    }


if __name__ == "__main__":
    # 命令行执行入口
    import sys

    print("Starting validation of exercises/ directory...")
    all_valid, report = validate_exercises()

    summary = report["summary"]
    print(f"\nValidation Summary:")
    print(f"  Total files checked: {summary['total_files']}")
    print(f"  YAML files: {summary['yaml_count']}")
    print(f"  JSON files: {summary['json_count']}")
    print(f"  Valid files: {summary['valid_files']}")
    print(f"  Invalid files: {summary['invalid_files']}")
    print(f"  Error files: {summary['error_files']}")

    # 显示失败的文件
    if summary["invalid_files"] > 0 or summary["error_files"] > 0:
        print("\nFailed files:")
        for file_type, results in report["results"].items():
            for result in results:
                if result.status != ValidationStatus.VALID:
                    print(f"  - {result.file_path}: {result.message}")
        sys.exit(1)
    else:
        print("\nAll files passed validation!")
        sys.exit(0)

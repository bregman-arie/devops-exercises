"""
自动化答案验证脚本的测试用例

测试 scripts/validate/validator.py 中的验证功能
"""

import tempfile
import os
from pathlib import Path
from unittest import TestCase
import sys

# 添加scripts目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from validate.validator import (
    ConfigValidator,
    ValidationStatus,
    ValidationResult,
    validate_exercises
)


class TestConfigValidator(TestCase):
    """测试配置验证器类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_dir = tempfile.mkdtemp()
        self.validator = ConfigValidator(self.temp_dir)

    def tearDown(self):
        """清理测试环境"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_find_yaml_files(self):
        """测试查找YAML文件功能"""
        # 创建测试YAML文件
        yaml_content = "key: value\nlist:\n  - item1\n  - item2"
        yaml_path = Path(self.temp_dir) / "test.yml"
        with open(yaml_path, 'w') as f:
            f.write(yaml_content)

        # 创建子目录中的YAML文件
        subdir = Path(self.temp_dir) / "subdir"
        subdir.mkdir()
        yaml_path2 = subdir / "test.yaml"
        with open(yaml_path2, 'w') as f:
            f.write(yaml_content)

        files = self.validator.find_yaml_files()
        self.assertEqual(len(files), 2)
        self.assertIn(yaml_path, files)
        self.assertIn(yaml_path2, files)

    def test_find_json_files(self):
        """测试查找JSON文件功能"""
        # 创建测试JSON文件
        json_content = '{"key": "value", "list": [1, 2, 3]}'
        json_path = Path(self.temp_dir) / "test.json"
        with open(json_path, 'w') as f:
            f.write(json_content)

        files = self.validator.find_json_files()
        self.assertEqual(len(files), 1)
        self.assertIn(json_path, files)

    def test_validate_valid_yaml(self):
        """测试验证有效的YAML文件"""
        yaml_content = """
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
"""
        yaml_path = Path(self.temp_dir) / "valid.yaml"
        with open(yaml_path, 'w') as f:
            f.write(yaml_content)

        result = self.validator.validate_yaml_file(yaml_path)
        self.assertEqual(result.status, ValidationStatus.VALID)
        self.assertIn("valid", result.message.lower())

    def test_validate_invalid_yaml(self):
        """测试验证无效的YAML文件"""
        invalid_yaml = """
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
  invalid_indent:
   - item1
  - item2
"""
        yaml_path = Path(self.temp_dir) / "invalid.yaml"
        with open(yaml_path, 'w') as f:
            f.write(invalid_yaml)

        result = self.validator.validate_yaml_file(yaml_path)
        self.assertEqual(result.status, ValidationStatus.INVALID)
        self.assertTrue(len(result.errors) > 0)

    def test_validate_valid_json(self):
        """测试验证有效的JSON文件"""
        json_content = '{"name": "test", "version": "1.0", "enabled": true}'
        json_path = Path(self.temp_dir) / "valid.json"
        with open(json_path, 'w') as f:
            f.write(json_content)

        result = self.validator.validate_json_file(json_path)
        self.assertEqual(result.status, ValidationStatus.VALID)
        self.assertIn("valid", result.message.lower())

    def test_validate_invalid_json(self):
        """测试验证无效的JSON文件"""
        invalid_json = '{"name": "test", "version": "1.0",}'  # 尾随逗号
        json_path = Path(self.temp_dir) / "invalid.json"
        with open(json_path, 'w') as f:
            f.write(invalid_json)

        result = self.validator.validate_json_file(json_path)
        self.assertEqual(result.status, ValidationStatus.INVALID)
        self.assertTrue(len(result.errors) > 0)

    def test_validate_all_yaml(self):
        """测试批量验证YAML文件"""
        # 创建多个YAML文件
        for i in range(3):
            yaml_path = Path(self.temp_dir) / f"test{i}.yml"
            with open(yaml_path, 'w') as f:
                f.write(f"key{i}: value{i}")

        results = self.validator.validate_all_yaml()
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertEqual(result.status, ValidationStatus.VALID)

    def test_validate_all_json(self):
        """测试批量验证JSON文件"""
        # 创建多个JSON文件
        for i in range(2):
            json_path = Path(self.temp_dir) / f"test{i}.json"
            with open(json_path, 'w') as f:
                f.write(f'{{"key{i}": "value{i}"}}')

        results = self.validator.validate_all_json()
        self.assertEqual(len(results), 2)
        for result in results:
            self.assertEqual(result.status, ValidationStatus.VALID)

    def test_get_summary(self):
        """测试验证结果汇总功能"""
        # 创建混合文件
        valid_yaml = Path(self.temp_dir) / "valid.yml"
        with open(valid_yaml, 'w') as f:
            f.write("key: value")

        invalid_yaml = Path(self.temp_dir) / "invalid.yml"
        with open(invalid_yaml, 'w') as f:
            f.write("invalid: yaml: content::")

        valid_json = Path(self.temp_dir) / "valid.json"
        with open(valid_json, 'w') as f:
            f.write('{"key": "value"}')

        results = self.validator.validate_all()
        summary = self.validator.get_summary(results)

        self.assertEqual(summary["total_files"], 3)
        self.assertEqual(summary["yaml_count"], 2)
        self.assertEqual(summary["json_count"], 1)
        self.assertEqual(summary["valid_files"], 2)
        self.assertEqual(summary["invalid_files"], 1)

    def test_validate_exercises_function(self):
        """测试validate_exercises函数"""
        # 创建有效文件
        yaml_path = Path(self.temp_dir) / "test.yml"
        with open(yaml_path, 'w') as f:
            f.write("key: value")

        all_valid, report = validate_exercises(self.temp_dir)
        self.assertTrue(all_valid)
        self.assertIn("summary", report)
        self.assertIn("results", report)

    def test_empty_directory(self):
        """测试空目录情况"""
        results = self.validator.validate_all()
        summary = self.validator.get_summary(results)
        self.assertEqual(summary["total_files"], 0)
        self.assertEqual(summary["yaml_count"], 0)
        self.assertEqual(summary["json_count"], 0)

    def test_validation_result_dataclass(self):
        """测试ValidationResult数据类"""
        result = ValidationResult(
            file_path=Path("/test/file.yaml"),
            status=ValidationStatus.VALID,
            message="Test message"
        )
        self.assertEqual(result.file_path, Path("/test/file.yaml"))
        self.assertEqual(result.status, ValidationStatus.VALID)
        self.assertEqual(result.message, "Test message")
        self.assertEqual(result.errors, [])

    def test_complex_yaml_structure(self):
        """测试复杂YAML结构验证"""
        complex_yaml = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        resources:
          limits:
            cpu: "500m"
            memory: "128Mi"
          requests:
            cpu: "250m"
            memory: "64Mi"
"""
        yaml_path = Path(self.temp_dir) / "complex.yaml"
        with open(yaml_path, 'w') as f:
            f.write(complex_yaml)

        result = self.validator.validate_yaml_file(yaml_path)
        self.assertEqual(result.status, ValidationStatus.VALID)

    def test_complex_json_structure(self):
        """测试复杂JSON结构验证"""
        complex_json = """{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "roles": ["admin", "user"],
      "settings": {
        "theme": "dark",
        "notifications": true
      }
    },
    {
      "id": 2,
      "name": "Bob",
      "roles": ["user"],
      "settings": {
        "theme": "light",
        "notifications": false
      }
    }
  ],
  "config": {
    "version": "1.0.0",
    "features": {
      "auth": true,
      "logging": false
    }
  }
}"""
        json_path = Path(self.temp_dir) / "complex.json"
        with open(json_path, 'w') as f:
            f.write(complex_json)

        result = self.validator.validate_json_file(json_path)
        self.assertEqual(result.status, ValidationStatus.VALID)


class TestValidationIntegration(TestCase):
    """集成测试 - 测试与实际项目结构的兼容性"""

    def test_default_exercises_path(self):
        """测试默认exercises路径设置"""
        validator = ConfigValidator()
        expected_path = Path(__file__).parent.parent / "exercises"
        self.assertEqual(validator.exercises_path, expected_path)

    def test_real_exercises_directory(self):
        """测试真实exercises目录（如果存在）"""
        exercises_path = Path(__file__).parent.parent / "exercises"
        if exercises_path.exists():
            validator = ConfigValidator()
            results = validator.validate_all()
            # 验证结果结构正确
            self.assertIn("yaml", results)
            self.assertIn("json", results)


if __name__ == "__main__":
    import unittest
    unittest.main()

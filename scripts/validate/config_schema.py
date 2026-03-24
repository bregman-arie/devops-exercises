"""
Schema definitions for different YAML configuration types.
"""

KUBERNETES_DEPLOYMENT_SCHEMA = {
    "type": "object",
    "required": ["apiVersion", "kind", "metadata", "spec"],
    "properties": {
        "apiVersion": {"type": "string"},
        "kind": {"type": "string", "enum": ["Deployment", "Service", "Pod", "ConfigMap", "Secret", "Namespace", "Ingress", "ReplicaSet", "DaemonSet", "StatefulSet", "Job", "CronJob"]},
        "metadata": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"},
                "namespace": {"type": "string"},
                "labels": {"type": "object"},
                "annotations": {"type": "object"}
            }
        },
        "spec": {"type": "object"}
    }
}

KUBERNETES_SERVICE_SCHEMA = {
    "type": "object",
    "required": ["apiVersion", "kind", "metadata", "spec"],
    "properties": {
        "apiVersion": {"type": "string"},
        "kind": {"type": "string", "const": "Service"},
        "metadata": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"},
                "namespace": {"type": "string"},
                "labels": {"type": "object"}
            }
        },
        "spec": {
            "type": "object",
            "required": ["ports"],
            "properties": {
                "ports": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["port"],
                        "properties": {
                            "port": {"type": "integer"},
                            "targetPort": {"type": ["integer", "string"]},
                            "protocol": {"type": "string"},
                            "name": {"type": "string"}
                        }
                    }
                },
                "selector": {"type": "object"},
                "type": {"type": "string", "enum": ["ClusterIP", "NodePort", "LoadBalancer", "ExternalName"]}
            }
        }
    }
}

ANSIBLE_PLAYBOOK_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["name", "hosts"],
        "properties": {
            "name": {"type": "string"},
            "hosts": {"type": ["string", "array"]},
            "become": {"type": "boolean"},
            "become_user": {"type": "string"},
            "vars": {"type": "object"},
            "vars_files": {"type": "array"},
            "tasks": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["name"],
                    "properties": {
                        "name": {"type": "string"},
                        "module": {"type": "string"},
                        "when": {"type": ["string", "boolean"]},
                        "loop": {"type": ["array", "string"]},
                        "register": {"type": "string"},
                        "failed_when": {"type": ["string", "array", "boolean"]}
                    }
                }
            },
            "roles": {"type": "array"}
        }
    }
}

DOCKER_COMPOSE_SCHEMA = {
    "type": "object",
    "required": ["services"],
    "properties": {
        "version": {"type": "string"},
        "services": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "image": {"type": "string"},
                    "build": {"type": ["string", "object"]},
                    "ports": {
                        "type": "array",
                        "items": {"type": ["string", "integer"]}
                    },
                    "environment": {"type": ["object", "array"]},
                    "volumes": {"type": "array"},
                    "depends_on": {"type": ["array", "object"]},
                    "networks": {"type": ["array", "object"]},
                    "restart": {"type": "string"}
                }
            }
        },
        "networks": {"type": "object"},
        "volumes": {"type": "object"}
    }
}

EXERCISE_CONFIG_SCHEMA = {
    "type": "object",
    "required": ["exercise", "category"],
    "properties": {
        "exercise": {
            "type": "object",
            "required": ["title", "description"],
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "difficulty": {"type": "string", "enum": ["beginner", "intermediate", "advanced"]},
                "tags": {"type": "array", "items": {"type": "string"}}
            }
        },
        "category": {"type": "string"},
        "solution": {"type": "string"},
        "hints": {"type": "array", "items": {"type": "string"}},
        "validation": {
            "type": "object",
            "properties": {
                "expected_output": {"type": "string"},
                "commands": {"type": "array", "items": {"type": "string"}}
            }
        }
    }
}


def get_kubernetes_schema(kind=None):
    if kind == "Deployment":
        return KUBERNETES_DEPLOYMENT_SCHEMA
    elif kind == "Service":
        return KUBERNETES_SERVICE_SCHEMA
    return KUBERNETES_DEPLOYMENT_SCHEMA


def get_ansible_schema():
    return ANSIBLE_PLAYBOOK_SCHEMA


def get_docker_compose_schema():
    return DOCKER_COMPOSE_SCHEMA


def get_exercise_schema():
    return EXERCISE_CONFIG_SCHEMA


SCHEMA_MAPPING = {
    'kubernetes': {
        'Deployment': KUBERNETES_DEPLOYMENT_SCHEMA,
        'Service': KUBERNETES_SERVICE_SCHEMA,
        'Pod': KUBERNETES_DEPLOYMENT_SCHEMA,
        'ConfigMap': KUBERNETES_DEPLOYMENT_SCHEMA,
        'Secret': KUBERNETES_DEPLOYMENT_SCHEMA,
        'default': KUBERNETES_DEPLOYMENT_SCHEMA
    },
    'ansible': ANSIBLE_PLAYBOOK_SCHEMA,
    'docker-compose': DOCKER_COMPOSE_SCHEMA,
    'exercise': EXERCISE_CONFIG_SCHEMA
}

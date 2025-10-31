# AWS MSK and CDC Concepts - Complete Guide

This guide explains all the key concepts, components, and technologies used in this MSK CDC pipeline.

---

## Table of Contents

- [What is AWS MSK?](#what-is-aws-msk)
- [Apache Kafka Fundamentals](#apache-kafka-fundamentals)
- [MSK Cluster Components](#msk-cluster-components)
- [MSK Connect](#msk-connect)
- [Change Data Capture (CDC)](#change-data-capture-cdc)
- [Debezium](#debezium)
- [MySQL Binary Logs (binlog)](#mysql-binary-logs-binlog)
- [Prerequisites for CDC](#prerequisites-for-cdc)
- [Architecture Deep Dive](#architecture-deep-dive)
- [Performance and Scaling](#performance-and-scaling)

---

## What is AWS MSK?

**Amazon Managed Streaming for Apache Kafka (MSK)** is a fully managed service that makes it easy to build and run applications that use Apache Kafka to process streaming data.

### Key Benefits

| Feature | Description |
|---------|-------------|
| **Fully Managed** | AWS handles setup, provisioning, and operations |
| **High Availability** | Multi-AZ deployment with automatic failover |
| **Secure** | Encryption at rest and in transit, IAM integration |
| **Scalable** | Easy to scale brokers and storage |
| **Cost-Effective** | Pay only for what you use |
| **Integrated** | Works with AWS services (Lambda, S3, etc.) |

### Use Cases

1. **Real-time Analytics** - Process streaming data in real-time
2. **Log Aggregation** - Collect logs from multiple sources
3. **Event Sourcing** - Store state changes as events
4. **Change Data Capture (CDC)** - Capture database changes
5. **Stream Processing** - Transform and enrich data streams
6. **Microservices Communication** - Event-driven architecture

---

## Apache Kafka Fundamentals

### What is Apache Kafka?

Apache Kafka is a distributed streaming platform that:
- Publishes and subscribes to streams of records
- Stores streams of records durably and reliably
- Processes streams of records as they occur

### Core Concepts

#### 1. **Topics**

A **topic** is a category or feed name to which records are published.

```
Topic: user-events
├── Partition 0: [msg1, msg2, msg3]
├── Partition 1: [msg4, msg5, msg6]
└── Partition 2: [msg7, msg8, msg9]
```

**Characteristics:**
- Topics are split into **partitions** for parallelism
- Each partition is an ordered, immutable sequence of records
- Records in a partition are assigned a sequential ID called **offset**

#### 2. **Producers**

Producers **publish** data to topics.

```java
// Example: Debezium CDC Connector acts as a producer
Producer → Topic(user-changes) → Kafka Brokers
```

#### 3. **Consumers**

Consumers **subscribe** to topics and process the data.

```java
// Example: Your application consuming CDC events
Kafka Brokers → Topic(user-changes) → Consumer
```

#### 4. **Consumer Groups**

Multiple consumers can work together as a **consumer group**.

```
Consumer Group: analytics-app
├── Consumer 1: Reads Partition 0, 1
└── Consumer 2: Reads Partition 2, 3
```

**Benefits:**
- Load balancing across consumers
- Fault tolerance (if one consumer fails, others take over)
- Parallel processing

#### 5. **Brokers**

A Kafka **broker** is a server that stores data and serves clients.

```
MSK Cluster
├── Broker 1 (AZ-1): kafka-b-1.msk.amazonaws.com:9092
├── Broker 2 (AZ-2): kafka-b-2.msk.amazonaws.com:9092
└── Broker 3 (AZ-3): kafka-b-3.msk.amazonaws.com:9092
```

---

## MSK Cluster Components

### 1. **Bootstrap Brokers**

**Bootstrap brokers** are the initial connection points for Kafka clients.

#### What are Bootstrap Brokers?

Bootstrap brokers are a **comma-separated list** of broker addresses that clients use to:
1. **Discover** the cluster topology
2. **Connect** to the right brokers
3. **Retrieve metadata** about topics and partitions

#### Example Bootstrap Server String

```
b-1.msk-cluster.abc123.c2.kafka.us-east-1.amazonaws.com:9092,
b-2.msk-cluster.abc123.c2.kafka.us-east-1.amazonaws.com:9092,
b-3.msk-cluster.abc123.c2.kafka.us-east-1.amazonaws.com:9092
```

#### Why Multiple Bootstrap Brokers?

- **High Availability**: If one broker is down, clients can connect to others
- **Load Distribution**: Clients don't all connect to the same broker
- **Fault Tolerance**: Cluster remains accessible even if some brokers fail

#### How Bootstrap Brokers Work

```
1. Client connects to any bootstrap broker
   Client → Broker 1 (bootstrap)

2. Broker returns cluster metadata
   Broker 1 → Client: {
     brokers: [broker1, broker2, broker3],
     topics: [...],
     partitions: [...]
   }

3. Client connects to appropriate brokers
   Client → Broker 2 (for partition 0)
   Client → Broker 3 (for partition 1)
```

#### Types of Bootstrap Endpoints

| Type | Port | Use Case |
|------|------|----------|
| **Plaintext** | 9092 | Unencrypted communication |
| **TLS** | 9094 | Encrypted communication |
| **SASL/SCRAM** | 9096 | Authentication with credentials |
| **IAM** | 9098 | IAM-based authentication |

**In our setup:** We use **plaintext (9092)** for simplicity.

### 2. **Cluster Configuration**

Cluster configuration defines how the MSK cluster behaves.

#### Key Configuration Parameters

```hcl
resource "aws_msk_configuration" "cluster_configuration" {
  name = "msk-cluster-configuration"
  kafka_versions = ["3.8.x"]
  
  server_properties = <<EOF
    auto.create.topics.enable=true
    default.replication.factor=3
    min.insync.replicas=2
    log.retention.hours=168
    log.retention.bytes=1073741824
  EOF
}
```

#### Important Settings

| Setting | Value | Purpose |
|---------|-------|---------|
| `auto.create.topics.enable` | `true` | Auto-create topics when producer writes |
| `default.replication.factor` | `3` | Number of copies of each partition |
| `min.insync.replicas` | `2` | Min replicas that must acknowledge writes |
| `log.retention.hours` | `168` | Keep messages for 7 days |
| `log.retention.bytes` | `1GB` | Max size per partition |

#### Why Replication Factor = 3?

```
Topic: user-events, Partition 0, Replication Factor: 3

Broker 1 (Leader):    [msg1, msg2, msg3] ← Writes go here
Broker 2 (Follower):  [msg1, msg2, msg3] ← Syncs from leader
Broker 3 (Follower):  [msg1, msg2, msg3] ← Syncs from leader
```

**Benefits:**
- **Durability**: Data survives broker failures
- **Availability**: If leader fails, follower becomes leader
- **Reliability**: Multiple copies ensure no data loss

### 3. **Broker Node Groups**

Defines the compute and storage for brokers.

```hcl
broker_node_group_info {
  instance_type   = "kafka.t3.small"
  client_subnets  = [subnet-1, subnet-2, subnet-3]
  security_groups = [sg-msk]
  
  storage_info {
    ebs_storage_info {
      volume_size = 10  # GB per broker
    }
  }
}
```

#### Instance Types

| Type | vCPU | Memory | Network | Use Case |
|------|------|--------|---------|----------|
| kafka.t3.small | 2 | 2 GB | Low | Dev/Test |
| kafka.m5.large | 2 | 8 GB | Moderate | Small Production |
| kafka.m5.xlarge | 4 | 16 GB | High | Production |
| kafka.m5.2xlarge | 8 | 32 GB | Very High | Large Production |

### 4. **Multi-AZ Deployment**

MSK automatically deploys brokers across **3 Availability Zones** for high availability.

```
Region: us-east-1
├── AZ 1: Broker 1
├── AZ 2: Broker 2
└── AZ 3: Broker 3
```

**Benefits:**
- Survives entire AZ failures
- Low latency within region
- Automatic failover

---

## MSK Connect

**MSK Connect** is a feature of Amazon MSK that makes it easy to run fully managed Apache Kafka Connect workers.

### What is Kafka Connect?

**Kafka Connect** is a framework for connecting Kafka with external systems (databases, file systems, key-value stores, search indexes, etc.).

### Architecture

```
Source System         Kafka Connect            Kafka Cluster
┌──────────┐         ┌─────────────┐          ┌──────────┐
│  MySQL   │  ────→  │   Source    │  ────→   │  Topic   │
│   RDS    │         │  Connector  │          │          │
└──────────┘         └─────────────┘          └──────────┘
                           ↓
                     ┌─────────────┐
                     │   Worker    │
                     │Configuration│
                     └─────────────┘
```

### Components of MSK Connect

#### 1. **Custom Plugins**

Plugins contain the connector code (JAR files).

```hcl
resource "aws_mskconnect_custom_plugin" "connector_plugin_debezium" {
  name         = "debezium-mysql-connector"
  content_type = "ZIP"
  
  location {
    s3 {
      bucket_arn = "arn:aws:s3:::my-bucket"
      file_key   = "plugins/debezium-mysql-plugin.zip"
    }
  }
}
```

**In our setup:**
- Plugin: Debezium MySQL Connector
- Location: S3 bucket (`aws-msk-resources-bucket`)
- Format: ZIP file with all JARs

#### 2. **Worker Configuration**

Defines how workers process data.

```hcl
resource "aws_mskconnect_worker_configuration" "connector_configuration" {
  name = "worker-configuration"
  
  properties_file_content = <<EOF
    key.converter=org.apache.kafka.connect.storage.StringConverter
    value.converter=org.apache.kafka.connect.json.JsonConverter
  EOF
}
```

**Key Settings:**
- `key.converter`: How to serialize message keys
- `value.converter`: How to serialize message values

**Common Converters:**
| Converter | Format | Use Case |
|-----------|--------|----------|
| `StringConverter` | Plain text | Simple keys/values |
| `JsonConverter` | JSON | Structured data (our choice) |
| `AvroConverter` | Avro | Schema evolution |
| `ByteArrayConverter` | Binary | Raw bytes |

#### 3. **MSK Connector**

The actual connector instance that runs the CDC.

```hcl
resource "aws_mskconnect_connector" "msk_cdc_connector" {
  name = "cdc-connector"
  
  capacity {
    provisioned_capacity {
      mcu_count    = 2  # Memory/CPU units
      worker_count = 1  # Number of workers
    }
  }
  
  connector_configuration = {
    "connector.class" = "io.debezium.connector.mysql.MySqlConnector"
    "database.hostname" = "rds-endpoint.amazonaws.com"
    "database.user" = "admin"
    "database.password" = "${secret}"
    # ... more config
  }
}
```

#### Capacity Options

**Provisioned Capacity:**
- Specify exact MCU (Memory & CPU Unit) count
- Each MCU = 1 vCPU + 4 GB memory
- Fixed cost regardless of usage

**Auto-Scaling (coming soon):**
- Automatically adjusts based on load
- Pay only for what you use

#### Connector States

| State | Description |
|-------|-------------|
| **CREATING** | Connector is being created |
| **RUNNING** | Actively processing data |
| **UPDATING** | Configuration being updated |
| **FAILED** | Error occurred, check logs |
| **DELETING** | Being deleted |

---

## Change Data Capture (CDC)

### What is CDC?

**Change Data Capture (CDC)** is a design pattern that tracks changes in a database and makes them available to downstream systems in real-time.

### Why CDC?

Traditional approaches to data synchronization:

#### ❌ **Batch Processing** (Old Way)
```
Every 1 hour:
  1. Query: SELECT * FROM users WHERE updated_at > last_sync
  2. Compare with target
  3. Update differences
```

**Problems:**
- High latency (data delayed by hours)
- Resource intensive (full table scans)
- Missed deletes (hard to track)
- Database load spikes

#### ✅ **Change Data Capture** (Modern Way)
```
Real-time:
  1. Database writes → binlog
  2. CDC captures change
  3. Publish to Kafka
  4. Consumers react instantly
```

**Benefits:**
- **Real-time**: Changes available in milliseconds
- **Low overhead**: Only changed records
- **Complete**: Captures INSERT, UPDATE, DELETE
- **Non-invasive**: No application changes needed

### CDC Use Cases

1. **Data Replication**
   ```
   Production DB → CDC → Replica DB
   ```

2. **Real-time Analytics**
   ```
   Orders DB → CDC → Analytics Dashboard
   ```

3. **Event-Driven Microservices**
   ```
   User DB → CDC → Email Service
                  → Notification Service
                  → Analytics Service
   ```

4. **Data Warehouse Sync**
   ```
   OLTP DB → CDC → Data Lake → Data Warehouse
   ```

5. **Cache Invalidation**
   ```
   MySQL → CDC → Invalidate Redis Cache
   ```

### CDC Architecture in Our Setup

```
┌─────────────────────────────────────────────────────────────┐
│                    CDC Pipeline Flow                        │
└─────────────────────────────────────────────────────────────┘

1. Application writes data
   ↓
2. MySQL RDS executes SQL
   INSERT INTO users (name) VALUES ('John');
   ↓
3. MySQL writes to Binary Log (binlog)
   Position: 12345
   Event: INSERT users {id:1, name:'John'}
   ↓
4. Debezium Connector reads binlog
   ↓
5. Debezium transforms to Kafka message
   {
     "before": null,
     "after": {"id":1, "name":"John"},
     "op": "c"
   }
   ↓
6. Publishes to MSK Kafka topic
   Topic: gaurav.cdc.users
   ↓
7. Consumers receive event
   Consumer processes change in real-time
```

---

## Debezium

### What is Debezium?

**Debezium** is an open-source distributed platform for change data capture. It monitors databases and produces events for each row-level change.

### Why Debezium?

| Feature | Benefit |
|---------|---------|
| **Open Source** | Free, community-supported |
| **Multi-Database** | MySQL, PostgreSQL, MongoDB, SQL Server, Oracle |
| **Kafka Integration** | Native Kafka Connect connector |
| **At-Least-Once** | Guarantees no data loss |
| **Schema Changes** | Handles DDL changes gracefully |
| **Snapshot** | Initial full table copy |

### Debezium MySQL Connector

#### How It Works

```
┌──────────────────────────────────────────────────────────┐
│              Debezium MySQL Connector                     │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  1. Connect to MySQL as replication slave                │
│     ↓                                                     │
│  2. Read binary log (binlog) events                      │
│     ↓                                                     │
│  3. Parse binlog events (INSERT/UPDATE/DELETE)           │
│     ↓                                                     │
│  4. Transform to CDC format (before/after)               │
│     ↓                                                     │
│  5. Publish to Kafka topic                               │
│     ↓                                                     │
│  6. Store position/offset for reliability                │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

#### Key Configuration

```javascript
{
  "connector.class": "io.debezium.connector.mysql.MySqlConnector",
  
  // Database Connection
  "database.hostname": "rds-endpoint.amazonaws.com",
  "database.port": "3306",
  "database.user": "admin",
  "database.password": "${from_secrets_manager}",
  
  // What to Capture
  "database.include.list": "cdc",  // Only 'cdc' database
  "table.include.list": "cdc.*",   // All tables in 'cdc' db
  
  // Topic Configuration
  "topic.prefix": "gaurav",  // Topic name: gaurav.cdc.tablename
  
  // Binlog Settings
  "database.server.id": "906010",  // Unique server ID
  
  // Schema History (tracks DDL changes)
  "schema.history.internal.kafka.bootstrap.servers": "broker1:9092",
  "schema.history.internal.kafka.topic": "schemahistory.fullfillment",
  
  // Data Format
  "value.converter": "org.apache.kafka.connect.json.JsonConverter",
  "value.converter.schemas.enable": false,
  
  // Performance
  "tasks.max": "1"  // Number of parallel tasks
}
```

### Debezium Event Structure

#### INSERT Event
```json
{
  "schema": { ... },
  "payload": {
    "before": null,
    "after": {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": 1704105600000
    },
    "source": {
      "version": "2.7.4.Final",
      "connector": "mysql",
      "name": "gaurav",
      "ts_ms": 1704105600123,
      "db": "cdc",
      "table": "users",
      "server_id": 906010,
      "gtid": null,
      "file": "mysql-bin.000001",
      "pos": 12345,
      "row": 0
    },
    "op": "c",  // c=create, u=update, d=delete, r=read (snapshot)
    "ts_ms": 1704105600456
  }
}
```

#### UPDATE Event
```json
{
  "before": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "after": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@newdomain.com"  // Changed
  },
  "op": "u"
}
```

#### DELETE Event
```json
{
  "before": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "after": null,
  "op": "d"
}
```

### Debezium Features

#### 1. **Initial Snapshot**

When connector starts for the first time, it takes a snapshot of existing data.

```
1. Lock tables (optional)
2. Read all existing rows
3. Create 'r' (read) events for each row
4. Publish to Kafka
5. Switch to binlog streaming
```

#### 2. **Schema Evolution**

Handles database schema changes (ALTER TABLE) gracefully.

```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
```

Debezium:
- Captures DDL change
- Updates internal schema
- Continues CDC with new schema

#### 3. **Exactly-Once Semantics**

Debezium tracks its position in the binlog to ensure:
- No data loss (at-least-once delivery)
- Minimal duplicates (idempotent processing recommended)

#### 4. **Filtering**

```javascript
// Include only specific databases
"database.include.list": "cdc,analytics"

// Exclude specific tables
"table.exclude.list": "cdc.temp_.*,cdc.backup_.*"

// Column filtering
"column.exclude.list": "cdc.users.password,cdc.users.ssn"
```

---

## MySQL Binary Logs (binlog)

### What is Binary Log?

**Binary log (binlog)** is a set of log files that contain information about data modifications made to a MySQL server.

### Why binlog?

1. **Replication**: Slave servers read master's binlog
2. **Point-in-Time Recovery**: Restore to exact moment
3. **Auditing**: Track all changes
4. **CDC**: Source for change data capture

### binlog Format

#### Row-Based Replication (ROW) ← **We use this**

```
Event: UPDATE users
WHERE id = 1
Before: {id:1, name:"John", email:"john@old.com"}
After:  {id:1, name:"John", email:"john@new.com"}
```

**Advantages:**
- Exact row changes captured
- No ambiguity
- Perfect for CDC
- Safe for all statements

**Disadvantages:**
- Larger binlog size
- More I/O

#### Statement-Based Replication (STATEMENT)

```
Event: UPDATE users SET email = CONCAT(name, '@new.com') WHERE id > 100
```

**Advantages:**
- Smaller binlog
- Less storage

**Disadvantages:**
- Non-deterministic functions problematic
- Can't guarantee exact replication
- Not ideal for CDC

#### Mixed Mode (MIXED)

Switches between ROW and STATEMENT based on the query.

### binlog Configuration for CDC

Required MySQL settings:

```sql
-- Enable binlog with ROW format
SET GLOBAL binlog_format = 'ROW';
SET GLOBAL binlog_row_image = 'FULL';

-- Check settings
SHOW VARIABLES LIKE 'binlog_format';
SHOW VARIABLES LIKE 'binlog_row_image';
```

**In our RDS configuration:**
```hcl
db_cluster_parameter_group_parameters = [
  {
    name  = "binlog_format"
    value = "ROW"
    apply_method = "pending-reboot"
  },
  {
    name  = "binlog_row_image"
    value = "FULL"
    apply_method = "pending-reboot"
  }
]
```

### binlog Row Image Options

| Option | Description | Size | Use Case |
|--------|-------------|------|----------|
| **FULL** | Before and after image | Large | CDC (our choice) |
| **MINIMAL** | Only changed columns | Small | Replication only |
| **NOBLOB** | Exclude BLOB columns | Medium | Compromise |

### binlog Position Tracking

Debezium tracks its position in binlog:

```
{
  "file": "mysql-bin.000003",
  "pos": 154,
  "row": 1,
  "server_id": 906010,
  "gtid": "3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5"
}
```

If connector restarts, it resumes from last position.

### binlog Retention

```sql
-- Set binlog retention (seconds)
CALL mysql.rds_set_configuration('binlog retention hours', 168);  -- 7 days

-- Check retention
CALL mysql.rds_show_configuration;
```

**Important:** Retention must be longer than maximum connector downtime!

---

## Prerequisites for CDC

### 1. Database Prerequisites

#### Enable Binary Logging

```sql
-- Check if binlog is enabled
SHOW VARIABLES LIKE 'log_bin';  -- Should be ON

-- Check binlog format
SHOW VARIABLES LIKE 'binlog_format';  -- Should be ROW

-- Check row image
SHOW VARIABLES LIKE 'binlog_row_image';  -- Should be FULL
```

#### Create CDC User with Permissions

```sql
-- Create user
CREATE USER 'cdc_user'@'%' IDENTIFIED BY 'SecurePassword123!';

-- Grant required permissions
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT 
ON *.* TO 'cdc_user'@'%';

-- For specific database
GRANT ALL PRIVILEGES ON cdc.* TO 'cdc_user'@'%';

FLUSH PRIVILEGES;
```

**Permission Explanation:**
- `SELECT`: Read table data
- `RELOAD`: Flush logs
- `SHOW DATABASES`: List databases
- `REPLICATION SLAVE`: Read binlog
- `REPLICATION CLIENT`: Use replication commands

#### Configure Server ID

Each MySQL server needs a unique server ID:

```sql
SHOW VARIABLES LIKE 'server_id';
```

### 2. Network Prerequisites

#### Security Groups

```
RDS Security Group
├── Inbound: Port 3306 from MSK Connector SG
└── Outbound: All traffic

MSK Security Group
├── Inbound: Port 9092 from MSK Connector SG
└── Outbound: All traffic

MSK Connector Security Group
├── Inbound: None needed
└── Outbound: All traffic
```

#### VPC and Subnets

- All components in same VPC
- Multi-AZ subnets for high availability
- Internet gateway for S3 access (plugin download)

### 3. AWS Prerequisites

#### IAM Permissions

MSK Connector role needs:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kafka-cluster:Connect",
        "kafka-cluster:DescribeCluster",
        "kafka-cluster:*Topic*",
        "kafka-cluster:WriteData",
        "kafka-cluster:ReadData"
      ],
      "Resource": "arn:aws:kafka:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "arn:aws:secretsmanager:*:*:secret:rds!cluster-*"
    }
  ]
}
```

#### S3 Bucket

For Debezium plugin storage:

```
s3://aws-msk-resources-bucket/
└── plugins/
    └── debezium-mysql-plugin.zip
```

### 4. Application Prerequisites

#### Database Schema

Tables should have:
- **Primary Key**: For proper CDC tracking
- **Timestamps**: For ordering (optional but recommended)

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

#### Initial Data Load

For existing databases:
1. Debezium takes initial snapshot
2. Can take hours for large tables
3. Consider pre-loading data or using snapshot modes

---

## Architecture Deep Dive

### Complete Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     Complete CDC Architecture                    │
└─────────────────────────────────────────────────────────────────┘

1. Application Layer
   ┌──────────────┐
   │ Application  │ ← User Actions
   └──────┬───────┘
          │ SQL: INSERT/UPDATE/DELETE
          ↓
2. Database Layer
   ┌──────────────┐
   │  MySQL RDS   │
   │  Aurora      │
   │              │
   │ ┌──────────┐ │
   │ │  binlog  │ │ ← All changes logged
   │ └──────────┘ │
   └──────┬───────┘
          │ Replication Protocol
          ↓
3. CDC Layer (MSK Connect)
   ┌───────────────────────────────┐
   │  Debezium Connector Worker    │
   │                               │
   │  ┌─────────────────────────┐  │
   │  │ 1. Read binlog events   │  │
   │  │ 2. Parse event          │  │
   │  │ 3. Transform to JSON    │  │
   │  │ 4. Publish to Kafka     │  │
   │  └─────────────────────────┘  │
   └───────────┬───────────────────┘
               │ CDC Events
               ↓
4. Streaming Layer (MSK)
   ┌───────────────────────────────┐
   │      Kafka Cluster (MSK)      │
   │                               │
   │  Topic: gaurav.cdc.users      │
   │  ┌─────────────────────────┐  │
   │  │ Partition 0 [msgs...]   │  │
   │  │ Partition 1 [msgs...]   │  │
   │  │ Partition 2 [msgs...]   │  │
   │  └─────────────────────────┘  │
   └───────────┬───────────────────┘
               │ Stream Processing
               ↓
5. Consumer Layer
   ┌───────────────────────────────┐
   │     Your Applications         │
   │                               │
   │  ├─ Real-time Analytics       │
   │  ├─ Data Warehouse Sync       │
   │  ├─ Notification Service      │
   │  ├─ Search Index Update       │
   │  └─ Cache Invalidation        │
   └───────────────────────────────┘
```

### High Availability Architecture

```
Region: us-east-1
├── AZ-1 (us-east-1a)
│   ├── MSK Broker 1
│   ├── RDS Instance 1 (Writer)
│   └── Connector Worker (if multi-worker)
│
├── AZ-2 (us-east-1b)
│   ├── MSK Broker 2
│   ├── RDS Instance 2 (Reader)
│   └── Connector Worker (if multi-worker)
│
└── AZ-3 (us-east-1c)
    ├── MSK Broker 3
    └── RDS Instance 3 (Reader)
```

**Failure Scenarios:**

| Failure | Impact | Recovery |
|---------|--------|----------|
| **1 Broker fails** | No impact | Automatic failover to follower |
| **1 AZ fails** | No impact | Other AZs continue |
| **Connector fails** | CDC pauses | Resumes from last position |
| **RDS Writer fails** | CDC pauses | Failover to reader (1-2 min) |

---

## Performance and Scaling

### Factors Affecting Performance

#### 1. **Database Load**

```
Low Load:    100 changes/sec   → Easy
Medium Load: 1,000 changes/sec → Manageable
High Load:   10,000+ changes/sec → Requires tuning
```

#### 2. **Message Size**

```
Small:  < 1 KB    → 10,000+ msgs/sec
Medium: 1-10 KB   → 1,000-5,000 msgs/sec
Large:  > 100 KB  → 100-500 msgs/sec
```

#### 3. **Network Latency**

```
Same VPC:      < 1 ms
Cross-Region:  50-100 ms
Internet:      100-300 ms
```

### Tuning for Performance

#### MSK Cluster

```hcl
# Increase broker count for throughput
number_of_broker_nodes = 6  # Instead of 3

# Use larger instance type
broker_instance_type = "kafka.m5.xlarge"  # Instead of kafka.t3.small

# Increase storage
ebs_volume_size = 100  # GB

# Tune partitions
topic.creation.default.partitions = 6  # More parallelism
```

#### Debezium Connector

```javascript
// Increase tasks for parallelism
"tasks.max": "4",  // More workers

// Batch size
"max.batch.size": "2048",

// Poll interval
"poll.interval.ms": "1000",

// Buffer size
"max.queue.size": "8192"
```

#### RDS Configuration

```sql
-- Increase binlog cache
SET GLOBAL binlog_cache_size = 1048576;  -- 1 MB

-- Increase max_allowed_packet
SET GLOBAL max_allowed_packet = 67108864;  -- 64 MB
```

### Monitoring Metrics

| Metric | What to Monitor | Alert Threshold |
|--------|----------------|-----------------|
| **Consumer Lag** | How far behind consumers are | > 10,000 messages |
| **Connector Status** | Is connector running? | != RUNNING |
| **Binlog Position** | Is connector keeping up? | Growing constantly |
| **Message Rate** | Messages/second | Baseline + 50% |
| **Error Rate** | Failed messages | > 0.1% |
| **Latency** | End-to-end delay | > 5 seconds |

---

## Summary

### Key Takeaways

1. **AWS MSK** provides fully managed Kafka clusters
2. **Bootstrap brokers** are entry points for Kafka clients
3. **Cluster configuration** defines behavior and performance
4. **MSK Connect** simplifies running Kafka Connect
5. **CDC** captures database changes in real-time
6. **Debezium** reads MySQL binlog and publishes to Kafka
7. **binlog (ROW format)** is essential for CDC
8. **Proper prerequisites** ensure smooth CDC operation
9. **Multi-AZ deployment** provides high availability
10. **Monitoring** is critical for production systems

### Technology Stack

```
Layer          | Technology
---------------|------------------
Database       | MySQL (RDS Aurora)
CDC Engine     | Debezium 2.7.4
Connector      | MSK Connect
Message Broker | Apache Kafka 3.8 (MSK)
Orchestration  | Terraform
CI/CD          | Jenkins
Security       | AWS Secrets Manager
Monitoring     | CloudWatch
```

---

## Additional Resources

### Official Documentation

- [AWS MSK Documentation](https://docs.aws.amazon.com/msk/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
- [Kafka Connect Documentation](https://kafka.apache.org/documentation/#connect)
- [MySQL Binary Log](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html)

### Tutorials

- [Getting Started with MSK](https://aws.amazon.com/msk/getting-started/)
- [Debezium Tutorial](https://debezium.io/documentation/reference/tutorial.html)
- [Kafka Connect Quickstart](https://kafka.apache.org/quickstart#quickstart_kafkaconnect)

### Best Practices

- [AWS MSK Best Practices](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html)
- [Debezium Best Practices](https://debezium.io/documentation/reference/operations/index.html)
- [Kafka Performance Tuning](https://kafka.apache.org/documentation/#hwandos)

---

**🎓 You now understand all the core concepts of AWS MSK and CDC!**


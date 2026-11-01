# Notifications System

## Functional requirements

- Handle multiple producers
- Dispatch to different channels or clients
- Control plane controlling the dispatching behaviors
- System health, retries, rate limits, DLQ (dead-letter-queue)
- Telemetry, metrics
- At least once
- Cancel-able

### Out of the scope

- Dashboard
- Metrics aggregation
- OTEL framework and handling

## Non-functional requirements

- 100M messages per day (~1k QPS)
- P50 at 500ms, p90 at 1 second
- Elastic worker capacity

## Data Schema

### API

- api/v1/deliver {[]Message} -> {[]task-id}
- api/v1/status {[]task-id} -> {[]task}
- api/v1/action {
  type: Cancel,
  ids: []Message-id,
}
- api/v1/template {
  POST: create
  GET: read
  PUT: update
  DELETE: delete
}

### Message mapping - control plane, push model

- Message
  - ID (PK, UUID)
  - Creation date
  - Deadline
  - Delivery Template
  - Message
  - Status

- Delivery Template
  - ID (PK, UUID)
  - Expiry DT
  - RetryCount
  - ComposeTemplate

- Channel
  - ID (PK)
  - Name
  - Type [email, SMS, app, s3d parth svc]
  - Worker task template

- Task
  - ID (PK)
  - Message
  - Channel
  - RetryCount

- Relationship tables:
  - Message <> Task
  - Delivery Template <> Channel

## High Level Design

### Init Delivery  

- API Gateway + Load balancer

- Message processors
  - queue, Kafka to shard by message ID
  - Delivery Template need to be cached and push-updated from the control plane
  - process messages, find the template, decides the worker queue

- Fan-out to workers
  - Fan-out to worker queue
  - control plane: queue maintainer nodes for retry counter, DLQ delivery, find worker, scale up
    or down for the worker pool, monitoring worker status (heartbeat, load, health alerts, etc.), 
    backup on status to the Redis cache, leader-follower pattern, 

- Worker
  - 1 worker node for each delivery type [email, SMS, app, 3rd party svc]
  - delivery failure

### Cancel Delivery

- Read status cache
- Redis cache
- Checked by both delivery and worker
- TTL == Message deadline

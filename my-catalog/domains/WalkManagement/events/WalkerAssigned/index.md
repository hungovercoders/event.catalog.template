---
name: WalkerAssigned
version: 0.0.2
summary: |
  Holds information about the walker assigned to a dog walking request.
producers:
    - Scheduling Team
consumers:
    - Data Lake
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per customer. Every time a walker is assigned to a dog walking request this event will be triggered.

We have a frontend application that allows users to schedule dog walks. This front end interacts directly with the `Scheduling Team` to assign walkers. The `Scheduling Team` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
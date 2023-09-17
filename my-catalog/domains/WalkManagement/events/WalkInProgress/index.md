---
name: WalkInProgress
version: 0.0.2
summary: |
  Holds information about the current status of the dog walk.
producers:
    - WalkTeam
consumers:
    - Data Lake
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per customer. Every time the walk status changes (start, in progress, end), this event will be triggered.

We have a frontend application that allows customers to schedule walks for their dogs. This front end interacts directly with the `WalkTeam` to track walk statuses. The `WalkTeam` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
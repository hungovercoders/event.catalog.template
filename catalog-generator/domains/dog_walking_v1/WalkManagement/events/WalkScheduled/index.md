---
name: WalkScheduled
version: 0.0.2
summary: |
  Holds information about the scheduled dog walking event.
producers:
    - Scheduling Service
consumers:
    - Data Lake
owners:
    - dboyne

---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per customer. Everytime a dog walk is scheduled this event will be triggered.

We have a frontend application that allows users to schedule dog walks. This front end interacts directly with the `Scheduling Service` to schedule walks. The `Scheduling Service` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
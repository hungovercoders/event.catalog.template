---
name: DogProfileUpdated
version: 0.0.2
summary: |
  Holds information about the updates to the dog's profile.
producers:
    - Walker Team
consumers:
    - Data Lake
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per dog. Every time an update is made to a dog's profile this event will be triggered.

We have a dog management application that allows dog owners to update their dog's profile. This management application interacts directly with the `Walker Team` to update the dog's profile. The `Walker Team` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
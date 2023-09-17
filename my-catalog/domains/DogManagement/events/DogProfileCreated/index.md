---
name: DogProfileCreated
version: 0.0.2
summary: |
  Holds information about the creation of a dog profile.
producers:
    - Registration Team
consumers:
    - Dog Management Team
    - Scheduling Team
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered once per dog. Every time a new dog profile is created, this event will be triggered.

We have a frontend application that allows users to create profiles for their dogs. This front end interacts directly with the `Registration Team` to add the profile. The `Registration Team` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
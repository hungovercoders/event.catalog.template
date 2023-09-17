---
name: UserRegistered
version: 0.0.2
summary: |
  Holds information about the registration of a new user in the dog walking system.
producers:
    - Registration System
consumers:
    - Dog Management System
    - Scheduling System
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times as every new user registration in the dog walking system triggers this event.

We have a user interface that allows potential users to register for our dog walking services. This interface interacts directly with the `Registration System` to register new users. The `Registration System` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
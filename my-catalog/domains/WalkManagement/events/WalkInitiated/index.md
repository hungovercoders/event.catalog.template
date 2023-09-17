---
name: WalkInitiated
version: 0.0.2
summary: |
  Indicates that a walk for the dog has been started.
producers:
    - WalkerTeam
consumers:
    - DogManagementTeam
    - CustomerSupportTeam
    - SchedulingTeam
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per day as different walkers may initiate walks with different dogs. Everytime a walk is being commenced, this event will be triggered.

The `WalkTeam` and `RegistrationTeam` have the permissions to initiate a dog walk. The `DogManagementTeam`, `CustomerSupportTeam`, and `SchedulingTeam` are the consumers of this event.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
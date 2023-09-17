---
name: PaymentReceived
version: 0.0.2
summary: |
  Holds information about the payment received for the dog walking service.
producers:
    - WalkTeam
consumers:
    - FinanceTeam
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered after every walk. When the payment for the walk is received this event will be triggered.

We have a frontend application that allows users to book a walk for their dog. This front end interacts directly with the `WalkTeam` to schedule walks and receive payment. The `WalkTeam` will raise the events which then would be consumed by `FinanceTeam`.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
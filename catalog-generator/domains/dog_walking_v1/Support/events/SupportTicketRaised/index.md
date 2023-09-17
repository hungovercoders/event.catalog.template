---
name: SupportTicketRaised
version: 0.0.2
summary: |
  Holds information about the support ticket raised by the user for dog walking service.
producers:
    - Walkers Management Service
consumers:
    - Customer Support Service
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per customer. Anytime the customer faces a problem with the dog walking service, they can raise a ticket and this event will be triggered.

We have a frontend application that allows users to book and manage walks for their dogs. This front end interacts directly with the `Walkers Management Service` to raise any issues. The `Customer Support Service` will handle the tickets.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
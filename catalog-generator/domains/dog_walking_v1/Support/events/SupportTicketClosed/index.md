---
name: SupportTicketClosed
version: 0.0.2
summary: |
  Holds information about the support ticket that was closed related to dog walking.
producers:
    - Customer Support Team
consumers:
    - Data Lake
owners:
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered when a support ticket related to dog walking is closed. It could be due to resolution of a ticket or closure due to lack of response. Every closure of a ticket trigger this event.

Our team interacts directly with the `Customer Support Team` to handle queries and issues. The `Customer Support Team` will raise the events when tickets are being closed.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
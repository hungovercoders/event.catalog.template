---
name: PaymentMade
version: 0.0.2
summary: |
  Holds information about a payment made by a user for dog walking service.
producers: 
    - Scheduling Service
consumers: 
    - Data Lake
owners: 
    - dboyne
---

<Admonition>When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.</Admonition>

### Details

This event can be triggered multiple times per customer. Every time the customer makes a payment for the dog walking service, this event will be triggered.

We have a frontend application that allows users to schedule and pay for dog walking services. This front end interacts directly with the `Scheduling Service` to schedule services and make payments. The `Scheduling Service` will raise the events.

<NodeGraph title="Consumer / Producer Diagram" />

<EventExamples title="How to trigger event" />

<Schema />

<SchemaViewer renderRootTreeLines defaultExpandedDepth='0' maxHeight="500" />
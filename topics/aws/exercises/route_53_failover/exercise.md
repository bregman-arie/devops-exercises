## AWS Route 53 - Failover

### Requirements

A running EC2 web instance with an health check defined for it in Route 53

### Objectives

1. Create a failover record that will failover to another record if an health check isn't passing
  1. Make sure TTL is 30
  2. Associate the failover record with the health check you have

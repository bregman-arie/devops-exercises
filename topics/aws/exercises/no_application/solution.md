## No Application :'(

### Objectives

Explain what might be possible reasons for the following issues:

1. Getting "time out" when trying to reach an application running on EC2 instance
2. Getting "connection refused" error

### Solution

1. 'Time out' Can be due to one of the following:

  * Security group doesn't allow access
  * No host (yes, I know. Not the first thing to check and yet...)
  * Operating system firewall blocking traffic

2. 'Connection refused' can happen due to one of the following:

  * Application didn't launch properly or has some issue (doesn't listens on the designated port)
  * Firewall replied with a reject instead of dropping the packets

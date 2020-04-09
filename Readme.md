# Binlog Streaming Exercise
> This repository is designed to be a sample of a small project and is 
> not intended for production use.

This project is designed to hook up to the bin log stream of a MYSQL 
database and send logs to an elastic search cluster hosted in AWS.

This function needs to be placed so that is can read from a MYSQL database
hosted in AWS and send records to ES with the lowest latency possible. The
highest possible uptime is desired by the team. 

## Task 1
Prepare a proposal for how you would deploy this application to meet
the requirements. What technologies would you use? How would you handle
deploys? Would you implement any automation?

## Task 2
Assess the code for effeciency and make recommendations, if any,
concerning:
- Compliance and Security
- Format and readability
- Documentation
- Testing
- Any other concerns?

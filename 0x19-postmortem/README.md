# **Postmortem**

Last month, the users were unable to access Holberton/Alx Intranet platform. All the services were down and all requests made on the platform routes returned 500 errors
Duration of the outage: 4:30 PM GMT on January 3rd, 2023 to 2:15 PM GMT on January 4rd, 2023
Impact: During the outage, all incoming traffic to the website was blocked and resulted in the website being inaccessible for 96% of users.
Root Cause: The root cause was the failure of the master server web-01.

## Timeline:

4:30 PM GMT, January 3rd, 2023: The issue was detected when monitoring alerts showed that the website was not responding.

5:35 PM GMT, January 3rd, 2023: The issue was investigated after receiving the monitoring alert.

6:55 PM GMT, January 3rd, 2023: After investigating the server, a Site Reliability Engineer found that the issue was that the master server lagging in speed.

7:00 PM CMT, January 3rd, 2023: The on-call engineers team disconnected the master server web-02 for additional system examination and routed all requests to client server web-03. 

2:15 AM GMT, January 4rd, 2022: The issue was fully resolved and the website was accessible to all users.

## Root Cause and Resolution:

Two Ubuntu cloud servers provide service to the Alx/Holberton platform. The master server web-01 is connected to serve all requests but it stopped functioning due to memory outage since there were a lot of requests as the client server web-02 was temporarily disconnected during a previous test and was not connected to the load balancer afterwards. 
The problem was solved when the load balancer was restarted after the master server had been momentarily unplugged for memory cleanup, and the round-robin algorithm was set up so that both the master and client servers could handle an equal number of requests.

## Corrective and Preventative Measures:

To prevent similar issues from happening in the future, the following measures have been taken:

1.	Choose the optimal loadbalancing algorithm for programs.

2.	Constantly monitor the servers to make sure they are functioning properly.

3.	Have additional back-up servers to prevent the program from falling offline entirely when an issue arises.

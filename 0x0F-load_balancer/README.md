# 0x0F. Load balancer

You have been given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

Tasks :

## 0. Double the number of webservers
Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task

## 1. Install your load balancer
Install and configure HAproxy on your lb-01 server.

# 0x10. HTTPS SSL

What happens when you don’t secure your website traffic?
![alt without ssl](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif)

## 0. World wide web
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

## 1. HAproxy SSL termination
Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.

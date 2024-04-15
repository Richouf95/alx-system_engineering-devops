# 0x13. Firewall

Your servers without a firewall…

![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

In this project wi'll make some ufw config on some server to incomong and outgoing trafic

Tasks: 

## 0. Block all incoming traffic but
Let’s install the ufw firewall and setup a few rules on web-01.

* The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
* Share the ufw commands that you used in your answer file

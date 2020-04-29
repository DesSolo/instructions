Fail2Ban
=====
### Install
```shell script
yum install fail2ban -y
vim /etc/fail2ban/jail.d/00-firewalld.conf
```
```
[DEFAULT]
banaction = firewallcmd-ipset
bantime = 3600
sender = fail2ban
destemail = root

[sshd]
enabled = true
port = ssh,80,443
maxentry = 3
findtime = 600
```
### Nginx 4xx
```shell script
vim /etc/fail2ban/filter.d/nginx-4xx.conf
```
```
[Definition]
failregex = ^<HOST>.*"(GET|POST).*" (404|444|403|400) .*$
ignoreregex =
```
```shell script
vim /etc/fail2ban/jail.d/00-firewalld.conf
```
```
[nginx-4xx]
enabled = true
port = 80,443
logpath  = /var/log/nginx/access.log
maxentry = 10
findtime = 600

[recidive]
enabled = true
port = 80,443
maxentry = 3
findtime = 86400
bantime = 604800
```
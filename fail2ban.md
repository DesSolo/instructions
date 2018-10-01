# Fail2Ban
```bash
yum install fail2ban -y
vim /etc/fail2ban/jail.d/00-firewalld.conf
```


>[DEFAULT]<br/>
>banaction = firewallcmd-ipset<br/>
>bantime = 3600<br/>
>sender = fail2ban<br/>
>destemail = root<br/>
><br/>
>[sshd]<br/>
>enabled = true<br/>
>port = ssh,80,443<br/>
>maxentry = 3<br/>
>findtime = 600<br/>

Nginx 4xx
```bash
vim /etc/fail2ban/filter.d/nginx-4xx.conf
```

[Definition]<br/>
failregex = ^<HOST>.*"(GET|POST).*" (404|444|403|400) .*$<br/>
ignoreregex =<br/>

```bash
vim /etc/fail2ban/jail.d/00-firewalld.conf
```

>[nginx-4xx]<br/>
>enabled = true<br/>
>port = 80,443<br/>
>logpath  = /var/log/nginx/access.log<br/>
>maxentry = 10<br/>
>findtime = 600<br/>

>[recidive]<br/>
>enabled = true<br/>
>port = 80,443<br/>
>maxentry = 3<br/>
>findtime = 86400<br/>
>bantime = 604800<br/>



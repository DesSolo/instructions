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

# Nagios
```bash
rpm -Uvh https://repo.nagios.com/nagios/7/nagios-repo-7-2.el7.noarch.rpm
yum install nagios -y
yum install nagion-plugins-all -y
systemctl enable httpd.service
systemctl start httpd.service
systemctl enable nagios.service
systemctl start nagios.service
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --reload
```

reset password

htpasswd -c /etc/nagios/passwd nagiosadmin

>http://ip/nagios<br/>

disable ip v6
```bash
vim /etc/nagios/objects/commands.cfg
```

```xml
# 'check-host-alive' command definition
define command{
        command_name    check-host-alive
        command_line    $USER1$/check_ping -4 -H $HOSTADDRESS$ -w 3000.0,80% -c 5000.0,100% -p 5
        }
```

# Telegramm
https://github.com/dariomas/nagios_telegram/wiki/Nagios-notifications-via-Telegram
```bash
yum install python2-pip -y
pip2.7 install requests pyopenssl urllib3
vim /etc/nagios/objects/contacts.cfg
```
```xml
define contact{
        contact_name dessolo
        service_notification_period 24x7
        host_notification_period 24x7
        service_notification_options w,u,c,r,f
        host_notification_options d,u,r,f
        service_notification_commands   notify-service-by-telegram
        host_notification_commands notify-host-by-telegram
        }
```


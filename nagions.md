# Nagios
```bash
yum install epel-release -y
yum install nagios -y
yum install nagios-plugins-all -y
systemctl enable httpd.service
systemctl start httpd.service
systemctl enable nagios.service
systemctl start nagios.service
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --reload
```

reset password
```bash
htpasswd -c /etc/nagios/passwd nagiosadmin
```
disable selinux
```bash
vim /etc/selinex/config
```
>SELINUX=disabled<br/>

>http://ip_address/nagios<br/>

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
cd /usr/local/bin
wget https://raw.githubusercontent.com/dariomas/nagios_telegram/master/nagios_telegram.py
chmod 755 /usr/local/bin/nagios_telegram.py
yum install python2-pip -y
pip2.7 install requests pyopenssl urllib3
vim /etc/nagios/objects/commands.cfg
```

```xml
# commands to send host/service notifications
define command {
  command_name     notify-host-by-telegram
  command_line     /usr/local/bin/nagios_telegram.py --token $USER4$ --object_type host --contact $USER3$ --notificationtype "$NOTIFICATIONTYPE$" --hoststate "$HOSTSTATE$" --hostname "$HOSTNAME$" --hostaddress "$HOSTADDRESS$" --datetime "$LONGDATETIME$" --output "$HOSTOUTPUT$"
}
define command {
  command_name     notify-service-by-telegram
  command_line     /usr/local/bin/nagios_telegram.py --token $USER4$ --object_type service --contact $USER3$ --notificationtype "$NOTIFICATIONTYPE$" --servicestate "$SERVICESTATE$" --hostname "$HOSTNAME$" --hostaddress "$HOSTADDRESS$" --datetime "$LONGDATETIME$" --output "$SERVICEOUTPUT$" --servicedesc "$SERVICEDESC$" --servicename "$SERVICENAME$"
}
```

```bash
vim /etc/nagios/private/resource.cfg
```
```xml
$USER3$=-135790246
$USER4$=123456789:ABCdEFGHIjKLMNoPQRSTUVWXYZ1q2w3e4R5t
```
```bash
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


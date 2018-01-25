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

# Timezone

```bash
vim /etc/nagios/nagios.cfg 
```
>use_timezone=Europe/Moscow<br/>

```bash
vim /etc/httpd/conf.d/nagios.conf
```
><Directory "/usr/lib64/nagios/cgi-bin/"><br/>
>   SetEnv TZ "Europe/Moscow"<br/>


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
# Example cfg server

```bash
vim /etc/nagios/objects/google.cfg
```

```xml
define host{
        use                     linux-server
        host_name               google.com
        alias                   google.com
        address                 www.google.com
        notification_period     24x7
        }
        
define service{
        use                             generic-service         ; Name of service template to use
        host_name                       google.com
        service_description             PING
        check_command                   check_ping!100.0,20%!500.0,60%
        notification_interval           0
        }

define service{
        use                             generic-service         ; Name of service template to use
        host_name                       google.com
        service_description             HTTP
        check_command                   check_http
        notifications_enabled           0
        }
```
```bash
vim /etc/nagios/nagios.cfg 
```

>cfg_file=/etc/nagios/objects/google.cfg<br/>

# Telegramm
https://github.com/dariomas/nagios_telegram/wiki/Nagios-notifications-via-Telegram
```bash
wget -O /usr/local/bin/nagios_telegram.py https://raw.githubusercontent.com/DesSolo/plex/master/nagios_telegram.py
chmod 755 /usr/local/bin/nagios_telegram.py
yum install python2-pip -y
pip2.7 install twx
vim /etc/nagios/objects/commands.cfg
```
```xml
# commands to send host/service notifications
define command {
        command_name     notify-host-by-telegram
        command_line     /usr/local/bin/nagios_telegram.py --token TOKEN --object_type host --contact "$CONTACTPAGER$" --notificationtype "$NOTIFICATIONTYPE$" --hoststate "$HOSTSTATE$" --hostname "$HOSTNAME$" --hostaddress "$HOSTADDRESS$" --datetime "$LONGDATETIME$" --output "$HOSTOUTPUT$"
}

define command {
        command_name     notify-service-by-telegram
        command_line     /usr/local/bin/nagios_telegram.py --token TOKEN --object_type service --contact "$CONTACTPAGER$" --notificationtype "$NOTIFICATIONTYPE$" --servicestate "$SERVICESTATE$" --hostname "$HOSTNAME$" --hostaddress "$HOSTADDRESS$" --datetime "$LONGDATETIME$" --output "$SERVICEOUTPUT$" --servicedesc "$SERVICEDESC$" --servicename "$SERVICENAME$"
}
```
```bash
vim /etc/nagios/objects/contacts.cfg
```
```xml
define contact{
        contact_name                    Telegram Group Chat
        pager                           -228700585                      ; The name of this contact template
        service_notification_period     24x7                            ; service notifications can be sent anytime
        host_notification_period        24x7                            ; host notifications can be sent anytime
        service_notification_options    w,u,c,r,f,s                     ; send notifications for all service states, flapping events, and scheduled downtime events
        host_notification_options       d,u,r,f,s                       ; send notifications for all host states, flapping events, and scheduled downtime events
        service_notification_commands   notify-service-by-telegram      ; send service notifications
        host_notification_commands      notify-host-by-telegram         ; send host notifications
        }
define contactgroup{
        contactgroup_name       admins
        alias                   Nagios Administrators
        members                 Telegram Group Chat

```


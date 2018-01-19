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

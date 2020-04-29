Grafana
=====
```shell script
vim /etc/yum.repos.d/grafana.repo
```
```
[grafana]
name=grafana
baseurl=https://packagecloud.io/grafana/stable/el/7/$basearch
gpgkey=https://packagecloud.io/gpg.key https://grafanarel.s3.amazonaws.com/RPM-GPG-KEY-grafana
enabled=0
gpgcheck=1
```
```shell script
yum --enablerepo=grafana -y install grafana initscripts fontconfig
```
*settings Grafana in /etc/grafana/grafana.ini*
```shell script
systemctl start grafana-server
systemctl enable grafana-server

firewall-cmd --zone=public --add-port=3000/tcp --permanent
firewall-cmd --reload
```

http://ip_address:3000  
admin:admin

```shell script
yum install graphite-web graphite-carbon -y
```

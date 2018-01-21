# Grafana
```bash
vim  /etc/yum.repos.d/grafana.repo
```

>[grafana]<br/>
>name=grafana<br/>
>baseurl=https://packagecloud.io/grafana/stable/el/7/$basearch<br/>
>gpgkey=https://packagecloud.io/gpg.key https://grafanarel.s3.amazonaws.com/RPM-GPG-KEY-grafana<br/>
>enabled=0<br/>
>gpgcheck=1<br/>

```bash
yum --enablerepo=grafana -y install grafana initscripts fontconfig
```
settings Grafana in /etc/grafana/grafana.ini
```bash
systemctl start grafana-server
systemctl enable grafana-server

firewall-cmd --zone=public --add-port=3000/tcp --permanent
firewall-cmd --reload
```
```xml
http://ip_address:3000
admin:admin
```
yum install graphite-web graphite-carbon -y

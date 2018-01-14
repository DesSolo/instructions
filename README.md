# Plex install Centos 7
```bash
yum update && sudo yum install wget
wget https://downloads.plex.tv/plex-media-server/1.10.1.4602-f54242b6b/plexmediaserver-1.10.1.4602-f54242b6b.x86_64.rpm
yum install plexmediaserver*.rpm
systemctl enable plexmediaserver.service
systemctl start plexmediaserver.service
```

# Fix
```bash
wget https://raw.githubusercontent.com/DesSolo/plex/master/PycharmProjects/plex_fix/fix.py
chmod +x fix.py
./fix.py
```
# Open ports firewall
```bash
vim /usr/lib/firewalld/services/plexmediaserver.xml
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>Plex Media Server</short>
  <description>This opens up PlexMediaServer for http (32400), upnp, and autodiscovery.</description>
  <port protocol="tcp" port="32469"/>
  <port protocol="tcp" port="32400"/>
  <port protocol="udp" port="32413"/>
  <port protocol="udp" port="1900"/>
  <port protocol="udp" port="32412"/>
  <port protocol="udp" port="32410"/>
  <port protocol="udp" port="32414"/>
</service>
```
```bash
firewall-cmd --permanent --zone=public --add-service=plexmediaserver
```
# Transmission
```bash
yum install epel-release
yum -y update
yum install transmission-daemon
systemctl start transmission-daemon.service
systemctl stop transmission-daemon.service
vim /var/lib/transmission/.config/transmission-daemon/settings.json
```
```xml
"rpc-whitelist-enabled": false,
```
```bash
systemctl start transmission-daemon.service
```

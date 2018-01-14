# plex fix
```bash
wget https://raw.githubusercontent.com/DesSolo/plex/master/PycharmProjects/plex_fix/fix.py
chmod +x fix.py
./fix.py
```
# plex ports firewall
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

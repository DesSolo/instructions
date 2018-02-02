# OenVPN server
```bash
yum install epel-release -y
yum install openvpn easy-rsa -y

mkdir /etc/openvpn/easy-rsa/
cp -r /usr/share/easy-rsa/3/* /etc/openvpn/easy-rsa/
cd /etc/openvpn/easy-rsa/

./easyrsa init-pki
./easyrsa build-ca
passfrase and name
./easyrsa gen-req server nopass
./easyrsa sign-req server server

./easyrsa gen-req user nopass
./easyrsa sign-req client user
yes and password

./easyrsa gen-dh

cp ./pki/ca.crt /etc/openvpn/
cp ./pki/dh.pem /etc/openvpn/dh1024.pem
cp ./pki/private/server.key /etc/openvpn/
cp ./pki/issued/server.crt /etc/openvpn/
cp ./pki/private/user.key /etc/openvpn/
cp ./pki/issued/user.crt /etc/openvpn/

vim /etc/openvpn/server.conf
```
```xml
local {ip addr}
port 1194
 
proto udp
dev tun
 
ca ca.crt
cert server.crt
key server.key
 
dh dh1024.pem
 
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt

client-to-client

push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"

keepalive 10 120

cipher AES-256-CBC
compress lz4-v2

comp-lzo
max-clients 100

user nobody
group nobody

persist-key
persist-tun

status /var/log/openvpn-status.log
log-append /var/log/openvpn.log

verb 3
explicit-exit-notify 1
```

```xml
client
dev tun
dev-type tun
server-poll-timeout 4
reneg-sec 604800
sndbuf 100000
rcvbuf 100000
;auth-user-pass

script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf

proto udp
remote {1p addr} 1194
resolv-retry infinite
nobind
 
persist-key
persist-tun

mute-replay-warnings
<ca>
-----BEGIN CERTIFICATE-----
{ca.crt}
-----END CERTIFICATE-----
</ca>
<cert>
-----BEGIN CERTIFICATE-----
{user.crt}
-----END CERTIFICATE-----
</cert>
<key>
-----BEGIN PRIVATE KEY-----
{user.key}
-----END PRIVATE KEY-----
</key>
key-direction 1
remote-cert-tls server
;tls-auth ta.key 1
cipher AES-256-CBC
 
comp-lzo
verb 3
```
```bash
firewall-cmd --zone=public --add-service openvpn --permanent
firewall-cmd --zone=public --add-masquerade --permanent
firewall-cmd --reload

systemctl start openvpn@server.service
systemctl enable openvpn@server.service
```

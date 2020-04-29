Postfix relay yandex
=====

```shell script
mv /etc/postfix/main.cf /etc/postfix/main.cf.old
vim /etc/postfix/main.cf
```
```
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/private/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_sasl_type = cyrus
smtp_sasl_mechanism_filter = login
smtp_sender_dependent_authentication = yes
sender_dependent_relayhost_maps = hash:/etc/postfix/private/sender_relay
sender_canonical_maps = hash:/etc/postfix/private/canonical
smtp_generic_maps = hash:/etc/postfix//private/generic
smtp_use_tls = yes
```

```shell script
mkdir /etc/postfix/private
```
```shell script
vim /etc/postfix/private/canonical
```
```
@yandex.ru	user@yandex.ru
```
```shell script
vim /etc/postfix/private/sender_relay
```
```
@yandex.ru	smtp.yandex.ru
```
```shell script
vim /etc/postfix/private/sasl_passwd
```
```
[smtp.yandex.ru]
user@yandex.ru:password
```
```shell script
vim /etc/postfix/private/generic
```
```
root@localhost  user@yandex.ru
asterisk@localhost  user@yandex.ru
root    user@yandex.ru
```

*Postfix lookup tables*
```shell script
postmap /etc/postfix/private/*
```
```shell script
systemctl restart postfix.service 
```

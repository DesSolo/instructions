# Postfix relay yandex

```bash
mv /etc/postfix/main.cf /etc/postfix/main.cf.old
vim /etc/postfix/main.cf
```
>smtp_sasl_auth_enable = yes<br />
>smtp_sasl_password_maps = hash:/etc/postfix/private/sasl_passwd<br />
>smtp_sasl_security_options = noanonymous<br />
>smtp_sasl_type = cyrus<br />
>smtp_sasl_mechanism_filter = login<br />
>smtp_sender_dependent_authentication = yes<br />
>sender_dependent_relayhost_maps = hash:/etc/postfix/private/sender_relay<br />
>sender_canonical_maps = hash:/etc/postfix/private/canonical<br />
>smtp_generic_maps = hash:/etc/postfix//private/generic<br />
>smtp_use_tls = yes<br />

Создаем папку /etc/postfix/private
```bash
mkdir /etc/postfix/private
```
Создаем файлы для Postfix lookup tables
```bash
vim /etc/postfix/private/canonical
```
>@yandex.ru	user@yandex.ru
```bash
vim /etc/postfix/private/sender_relay
```
>@yandex.ru	smtp.yandex.ru
```bash
vim /etc/postfix/private/sasl_passwd
```
>[smtp.yandex.ru]	user@yandex.ru:password
```bash
vim /etc/postfix/private/generic
```
>root@localhost  user@yandex.ru<br />
>asterisk@localhost      user@yandex.ru<br />
>root                            user@yandex.ru<br />

Создаем Postfix lookup tables
```bash
postmap /etc/postfix/private/*
```
Перезапускаем сервис
```bash
systemctl restart postfix.service 
```

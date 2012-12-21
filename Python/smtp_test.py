#!/usr/bin/python
# -*- coding: utf-8 -*-
# SMTP送信
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

SMTP_SERVER = 'smtp_server_name'
SMTP_PORT = 587
SMTP_LOGIN_UID = 'dummy_uid'
SMTP_LOGIN_PWD = 'dummy_password'
MESSAGE_ENCODING = 'ISO-2022-JP'

# create e-mail message
def create_message(from_addr, to_addrs, subject, body):
    msg = MIMEText(body, 'plain', MESSAGE_ENCODING)
    msg['Subject'] = Header(subject, MESSAGE_ENCODING)
    msg['From'] = from_addr
    msg['To'] = ''
    for v in to_addrs:
        msg['To'] = msg['To'] + v + ', '
    msg['Date'] = formatdate()
    return msg

# send e-mail
def send(from_addr, to_addrs, msg):
    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(SMTP_LOGIN_UID, SMTP_LOGIN_PWD)
    s.sendmail(from_addr, to_addrs, msg.as_string())
    s.close()

if __name__ == '__main__':
    from_addr = u'SENDER NAME<sender e-mail address>'
    to_addrs = ['user1@example.com', 'user2@example.com']
    msg = create_message(from_addr, to_addrs, u'日本語メールの試験サブジェクト5', u'これは試験メールの本文です。')
    send(from_addr, to_addrs, msg)



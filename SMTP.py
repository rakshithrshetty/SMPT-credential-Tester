#!/usr/bin/python
import smtplib
import re


def smtp_auth(gmailaddress, gmailpassword):
    mailServer = smtplib.SMTP('smtp.colorado.edu', 587)
    mailServer.starttls()
    try:
        mailServer.login(gmailaddress, gmailpassword)
        print("Auth Success\n")
        with open('output.txt', 'a') as f:
            f.write(gmailaddress + ':')
        with open('output.txt', 'a') as f:
            f.write(gmailpassword + '\n')
    except:
        print("Auth Failed\n")
    mailServer.quit()
    return ()


filepath = '2019-09-24-REN-ISAC-notification.txt'
file = open(filepath, 'r')
regex = re.compile("[a-zA-Z]{4}\d{4}")
for line in file:
    data = line.split(':')
    address = data[0]
    password = data[1][:-1]
    print(data)
    if regex.match(address):
        smtp_auth(address, password)

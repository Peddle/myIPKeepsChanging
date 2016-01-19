
import os
import urllib2
import smtplib

fromaddr = 'myipchangedagain@gmail.com'
toaddrs  = 'peddle.aaron@gmail.com'

# Credentials (if needed)
username = 'myipchangedagain@gmail.com'
password = 'securepassword'
import re

ip = None

def main():
    global ip


    while True: 
        currIp = get_ip()

        if ip != currIp:
            ip = currIp
            notify_email()

def notify_email():
    global ip

    print "emailing user..."

    msg = "Your IP is now " + str(ip)
    
    print msg

    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

    
def get_ip():
    page = urllib2.urlopen('http://whatismyip.org').read()
    
    ips = re.findall("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", page)

    if not ips:
        return None
    else:
        return ips[0]

main()

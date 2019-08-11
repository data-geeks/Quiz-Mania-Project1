#!/usr/bin/python3
import smtplib
class Verification:
    s = smtplib.SMTP_SSL('smtp.gmail.com',465)
    s.ehlo()
    sender='hvijay108@gmail.com'
    password='7062792821hv@gm'
    vcode=''
    name=''
    reciver=''
    msg='''
    From: %s
    To: %s
    Subject: Quiz Maina Verification
    
    %s
    '''

    body='''
    Hi there %s, hope you have a great day, please visit on the link below to verify your email
    
    %s
    '''

    reciver=''
    def send(self):
        print(self.msg)
        self.s.login(self.sender,self.password)
        self.s.sendmail(self.sender,self.reciver,self.body)
        self.s.quit()

    
from flask import render_template
from flask_mail import Message, Mail
from app.classes.auth import Auth_User
from app.send_msg import send_email
from app.classes.auth import Auth_User
from app import app
import time


def sendmsg():
    getusers = Auth_User.query.filter(Auth_User.confirmed == 1).all()

    for user in getusers:
        # set a time so email service dont get mad
        time.sleep(60)


        # email subject
        subject = "hello, %s. Clearnet Market is Free" % user.username
        # email body
        message ="""
            
            
        <div style="margin: 0 auto; max-width:150px; max-height:100px;">
        <img src="https://www.clearnetmarket.com/images/logo/smalllogo.png" width="150px" height="100px">
        </div>
        
            <h3>clearnetmarket.com is 100% free for users.</h3>
            <br>
        <div style="font-size:18px; color:#2a5ebb">
              No escrow service fees. No seller fees. No buying fees.  
              
              <br>
              <br>
              
              Want to support a crypto future?  Post your stuff on www.clearnetmarket.com today!
        </div>
            
            
            """


        with app.app_context():
            send_email(subject, [user.email], '', message)


sendmsg()
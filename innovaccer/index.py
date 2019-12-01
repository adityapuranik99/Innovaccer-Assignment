import smtplib, ssl
import os
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import time

cred = credentials.Certificate('entrymanagement-cd6d8-firebase-adminsdk-306tv-23c24e98fc.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://entrymanagement-cd6d8.firebaseio.com'
})


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'Order-Status-c0ffd279137b.json'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    room = TextField('Room:', validators=[validators.required(), validators.Length(min=3, max=35)])
    contact = TextField('Contact:', validators=[validators.required()])
    
class ReusableForm1(Form):
    timeField = TextField('Check Out:', validators = [validators.required()])
    room = TextField('Room:', validators=[validators.required(), validators.Length(min=3, max=35)])
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
        return render_template('home1.html')
        
    @app.route("/host", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print (form.errors)
        if request.method == 'POST':
            name=request.form['name']
            room=request.form['room']
            email=request.form['email']
            contact = request.form ['contact']
            now = str(time.strftime("%A %B %d, %I:%M:%S"))
            print(now)
            
            print (name, " ", email, " ", room) 
            orderNo = 12345
            response ="1"
            ref = db.reference('Meetings')
            #for val in ref.get().items():
             #   print(val[1])
            if room == 'D317':
                meet_ref = ref.child('Meeting 1')
                meet_ref.update({
                    'Name' : name,
                    'Email': email,
                    'CheckIn' : now,
                    'Contact' : contact,
                    'Room' : room
                })
            elif room == 'D123':
                meet_ref = ref.child('Meeting 2')
                meet_ref.update({
                    'Name' : name,
                    'Email' : email,
                    'CheckIn' : now,
                    'Contact' : contact,
                    'Room' : room
                })
            elif room == 'D205':
                meet_ref = ref.child('Meeting 3')
                meet_ref.update({
                    'Name' : name,
                    'Email' : email,
                    'CheckIn' : now,
                    'Contact' : contact,
                    'Room' : room
                })
            elif room == 'D113':
                meet_ref = ref.child('Meeting 4')
                meet_ref.update({
                    'Name' : name,
                    'Email' : email,
                    'CheckIn' : now,
                    'Contact' : contact,
                    'Room' : room
                })      
            elif room == 'D215':
                meet_ref = ref.child('Meeting 5')
                meet_ref.update({
                    'Name' : name,
                    'Email' : email,
                    'CheckIn' : now,
                    'Contact' : contact,
                    'Room' : room
                })
            else:
                flash('Error: All the form fields are required. ')
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('home.html', form=form)
    
    @app.route("/guest", methods=['GET', 'POST'])
    def guest():
        form = ReusableForm(request.form)
        
        print(form.errors)
        if(request.method == 'POST'):
            global GuestName,room
            GuestName=request.form['name']
            room=request.form['room']
            GuestEmail=request.form['email']
            Contact = request.form['contact']
            now = str(time.strftime("%A %B %d, %I:%M:%S"))
            print(now)
            
            print (GuestName, " ", GuestEmail, " ", room) 
            orderNo = 12345
            response ="1"
            ref = db.reference('Meetings')
            if room == 'D317':
                meet_ref = ref.child('Meeting 1')
                meet_ref.update({ 
                   'GuestName' : GuestName,
                   'GuestEmail': GuestEmail,
                   'CheckIn' : now,
                   'GuestContact' : Contact
                })
                for val in ref.get().items():
                    if(str(val[1]['GuestName'])==GuestName):
                        response = "The guest details are \nName: " + val[1]['GuestName']+"\nEmail: "+val[1]['GuestEmail'] + "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nHost Email: " + val[1]['Email'] + "\nRoom: " + val[1]['Room']
                        response1 = val[1]['Email']
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response1
                mailto2 = GuestEmail
                msg = response

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit()
                """
                import requests
                url = "https://www.fast2sms.com/dev/bulk"
                payload = "sender_id=FSTSMS&message=HiWorld&language=english&route=p&numbers=9416382702,7014309396"
                headers = {
                                'authorization': "Tty6cpmgEU93NZd4kbzrlX02KAfLqPMBQu7HYxJWjO8GwnievIqBQHae7lTOKoAMtdUw3pxXrNSVY561",
                                'Content-Type': "application/x-www-form-urlencoded",
                                'Cache-Control': "no-cache",
                      }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                """
                # we import the Twilio client from the dependency we just installed
                from twilio.rest import Client

                # the following line needs your Twilio Account SID and Auth Token
                client = Client("ACc6b7d06c45155cd21bb8fdbde9584e4b", "897fcf59e9951209efe2c8b2c2dcbd6f")

                # change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to="+919950957199", #Please enter your registered mobile no.
                                       from_="+15087090116", #"Please enter your twilio phone no.
                                       body=response)
            elif room == 'D123':
                meet_ref = ref.child('Meeting 2')
                meet_ref.update({ 
                   'GuestName' : GuestName,
                   'GuestEmail': GuestEmail,
                   'CheckIn' : now,
                   'GuestContact' : Contact
                    
                })
                for val in ref.get().items():
                    if(str(val[1]['GuestName'])==GuestName):
                        response = "The guest details are \nName: " + val[1]['GuestName']+"\nEmail: "+val[1]['GuestEmail'] + "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nHost Email: " + val[1]['Email'] + "\nRoom: " + val[1]['Room']
                        response1 = val[1]['Email']
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response1
                mailto2 = GuestEmail
                msg = response

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit()
                """
                import requests
                url = "https://www.fast2sms.com/dev/bulk"
                payload = "sender_id=FSTSMS&message=HiWorld&language=english&route=p&numbers=9416382702,7014309396"
                headers = {
                                'authorization': "Tty6cpmgEU93NZd4kbzrlX02KAfLqPMBQu7HYxJWjO8GwnievIqBQHae7lTOKoAMtdUw3pxXrNSVY561",
                                'Content-Type': "application/x-www-form-urlencoded",
                                'Cache-Control': "no-cache",
                      }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                """
                # we import the Twilio client from the dependency we just installed
                from twilio.rest import Client

                # the following line needs your Twilio Account SID and Auth Token
                client = Client("ACc6b7d06c45155cd21bb8fdbde9584e4b", "897fcf59e9951209efe2c8b2c2dcbd6f")

                # change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to="+919950957199", #Please enter your registered mobile no. 
                                       from_="+15087090116", #"Please enter your twilio phone no. 
                                       body=response)
            elif room == 'D205':
                meet_ref = ref.child('Meeting 3')
                meet_ref.update({ 
                   'GuestName' : GuestName,
                   'GuestEmail': GuestEmail,
                   'CheckIn' : now,
                   'GuestContact' : Contact
                    
                })
                for val in ref.get().items():
                    if(str(val[1]['GuestName'])==GuestName):
                        response = "The guest details are \nName: " + val[1]['GuestName']+"\nEmail: "+val[1]['GuestEmail'] + "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nHost Email: " + val[1]['Email'] + "\nRoom: " + val[1]['Room']
                        response1 = val[1]['Email']
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                print(response1)
                mailto1 = response1
                mailto2 = GuestEmail
                msg = response

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit()
                """
                import requests
                url = "https://www.fast2sms.com/dev/bulk"
                payload = "sender_id=FSTSMS&message=HiWorld&language=english&route=p&numbers=9416382702,7014309396"
                headers = {
                                'authorization': "Tty6cpmgEU93NZd4kbzrlX02KAfLqPMBQu7HYxJWjO8GwnievIqBQHae7lTOKoAMtdUw3pxXrNSVY561",
                                'Content-Type': "application/x-www-form-urlencoded",
                                'Cache-Control': "no-cache",
                      }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                """
                # we import the Twilio client from the dependency we just installed
                from twilio.rest import Client

                # the following line needs your Twilio Account SID and Auth Token
                client = Client("ACc6b7d06c45155cd21bb8fdbde9584e4b", "897fcf59e9951209efe2c8b2c2dcbd6f")

                # change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to="+919950957199", #Please enter your registered mobile no.
                                       from_="+15087090116", #"Please enter your twilio phone no. 
                                       body=response)
            elif room == 'D113':
                meet_ref = ref.child('Meeting 4')
                meet_ref.update({ 
                   'GuestName' : GuestName,
                   'GuestEmail': GuestEmail,
                   'CheckIn' : now,
                   'GuestContact' : Contact
                    
                })
                for val in ref.get().items():
                    if(str(val[1]['GuestName'])==GuestName):
                        response = "The guest details are \nName: " + val[1]['GuestName']+"\nEmail: "+val[1]['GuestEmail'] + "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nHost Email: " + val[1]['Email'] + "\nRoom: " + val[1]['Room']
                        response1 = val[1]['Email']
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response1
                mailto2 = GuestEmail
                msg = response

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit()
                """
                import requests
                url = "https://www.fast2sms.com/dev/bulk"
                payload = "sender_id=FSTSMS&message=HiWorld&language=english&route=p&numbers=9416382702,7014309396"
                headers = {
                                'authorization': "Tty6cpmgEU93NZd4kbzrlX02KAfLqPMBQu7HYxJWjO8GwnievIqBQHae7lTOKoAMtdUw3pxXrNSVY561",
                                'Content-Type': "application/x-www-form-urlencoded",
                                'Cache-Control': "no-cache",
                      }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                """
                # we import the Twilio client from the dependency we just installed
                from twilio.rest import Client

                # the following line needs your Twilio Account SID and Auth Token
                client = Client("ACc6b7d06c45155cd21bb8fdbde9584e4b", "897fcf59e9951209efe2c8b2c2dcbd6f")

                # change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to="+919950957199", #"Please enter your registered mobile no. 
                                       from_="+15087090116", #"Please enter your twilio phone no. 
                                       body=response)
            elif room == 'D215':
                meet_ref = ref.child('Meeting 5')
                meet_ref.update({ 
                   'GuestName' : GuestName,
                   'GuestEmail': GuestEmail,
                   'CheckIn' : now,
                   'GuestContact' : Contact
                    
                })
                for val in ref.get().items():
                    if(str(val[1]['GuestName'])==GuestName):
                        response = "The guest details are \nName: " + val[1]['GuestName']+"\nEmail: "+val[1]['GuestEmail'] + "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nHost Email: " + val[1]['Email'] + "\nRoom: " + val[1]['Room']
                        response1 = val[1]['Email']
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response1
                mailto2 = GuestEmail
                msg = response

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit()
                """
                import requests
                url = "https://www.fast2sms.com/dev/bulk"
                payload = "sender_id=FSTSMS&message=HiWorld&language=english&route=p&numbers=9416382702,7014309396"
                headers = {
                                'authorization': "Tty6cpmgEU93NZd4kbzrlX02KAfLqPMBQu7HYxJWjO8GwnievIqBQHae7lTOKoAMtdUw3pxXrNSVY561",
                                'Content-Type': "application/x-www-form-urlencoded",
                                'Cache-Control': "no-cache",
                      }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                """
                # we import the Twilio client from the dependency we just installed
                from twilio.rest import Client

                # the following line needs your Twilio Account SID and Auth Token
                client = Client("ACc6b7d06c45155cd21bb8fdbde9584e4b", "897fcf59e9951209efe2c8b2c2dcbd6f")

                # change the "from_" number to your Twilio number and the "to" number
                # to the phone number you signed up for Twilio with, or upgrade your
                # account to send SMS to any phone number
                client.messages.create(to="+919950957199", #"Please enter your registered mobile no. 
                                       from_="+15087090116", #"Please enter your twilio phone no.
                                       body=response)
            else:
                flash('Error: All the form fields are required. ')
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + GuestName)
        else:
            flash('Error: All the form fields are required. ')
        return render_template('guest.html')
    
    @app.route("/guestOn", methods=['GET', 'POST'])
    def guestOn():
        form = ReusableForm1(request.form)
        response = ""
        response1 = ""
        response2 = ""
        response3 = ""
        response4 = ""
        errorresponse =""
        print(form.errors)
        if (request.method == 'POST'):
            data = request.form['timeField']
            room = request.form['room']
            ref = db.reference('Meetings')
            if room == 'D317':
                meet_ref = ref.child('Meeting 1')
                meet_ref.update({
                    'CheckOut' : data
                })
                for val in ref.get().items():
                    if(str(val[1]['Room'])==room):
                        response="\nHosted by: " + val[1]['Name'] + " \nat " + val[1]['CheckIn']
                        response1 = val[1]['GuestEmail']
                        response3 = val[1]['Email']
                        response4 = val[1]['GuestName']
                        response2 = "The meeting details are \nName: " + val[1]['GuestName']+ "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nRoom: " + val[1]['Room'] + "\nCheck Out:" + val[1]['CheckOut']
                        print(""+response)
                        print(""+response1)
                        print(""+response2)
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response3
                mailto2 = response1
                msg = response2

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                #mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit()
                errorresponse =""
            elif room == 'D123':
                meet_ref = ref.child('Meeting 2')
                meet_ref.update({
                    'CheckOut' : data
                })
                for val in ref.get().items():
                    if(str(val[1]['Room'])==room):
                        response="\nHosted by: " + val[1]['Name'] + " \nat " + val[1]['CheckIn']
                        response1 = val[1]['GuestEmail']
                        response3 = val[1]['Email']
                        response4 = val[1]['GuestName']
                        response2 = "The meeting details are \nName: " + val[1]['GuestName']+ "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nRoom: " + val[1]['Room'] + "\nCheck Out:" + val[1]['CheckOut']
                        print(""+response)
                        print(""+response1)
                        print(""+response2)
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response3
                mailto2 = response1
                msg = response2

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                #mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit() 
                errorresponse=""
            elif room == 'D205':
                meet_ref = ref.child('Meeting 3')
                meet_ref.update({
                    'CheckOut' : data
                })
                for val in ref.get().items():
                    if(str(val[1]['Room'])==room):
                        response="\nHosted by: " + val[1]['Name'] + " \nat " + val[1]['CheckIn']
                        response1 = val[1]['GuestEmail']
                        response3 = val[1]['Email']
                        response4 = val[1]['GuestName']
                        response2 = "The meeting details are \nName: " + val[1]['GuestName']+ "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nRoom: " + val[1]['Room'] + "\nCheck Out:" + val[1]['CheckOut']
                        print(""+response)
                        print(""+response1)
                        print(""+response2)
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response3
                mailto2 = response1
                msg = response2

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                #mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit() 
                errorrespoonse = ""
            elif room == 'D113':
                meet_ref = ref.child('Meeting 4')
                meet_ref.update({
                    'CheckOut' : data
                })
                for val in ref.get().items():
                    if(str(val[1][''])==room):
                        response="\nHosted by: " + val[1]['Name'] + " \nat " + val[1]['CheckIn']
                        response1 = val[1]['GuestEmail']
                        response3 = val[1]['Email']
                        response4 = val[1]['GuestName']
                        response2 = "The meeting details are \nName: " + val[1]['GuestName']+ "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nRoom: " + val[1]['Room'] + "\nCheck Out:" + val[1]['CheckOut']
                        print(""+response)
                        print(""+response1)
                        print(""+response2)
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response3
                mailto2 = response1
                msg = response2

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                #mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit() 
                errorresponse =""
            elif room == 'D215':
                meet_ref = ref.child('Meeting 5')
                meet_ref.update({
                    'CheckOut' : data
                })
                for val in ref.get().items():
                    if(str(val[1]['Room'])==room):
                        response="\nHosted by: " + val[1]['Name'] + " \nat " + val[1]['CheckIn']
                        response1 = val[1]['GuestEmail']
                        response3 = val[1]['Email']
                        response4 = val[1]['GuestName']
                        response2 = "The meeting details are \nName: " + val[1]['GuestName']+ "\nCheck In: " +val[1]['CheckIn'] + "\nContact: " +val[1]['GuestContact'] + "\nHost Name: " + val[1]['Name'] + "\nRoom: " + val[1]['Room'] + "\nCheck Out:" + val[1]['CheckOut']
                        print(""+response)
                        print(""+response1)
                        print(""+response2)
                gmailaddress = "innovaccerap@gmail.com"
                gmailpassword = "innov@99"
                mailto1 = response3
                mailto2 = response1
                msg = response2

                #msg= "Name {n} {n1}".format(n=name,n1=now)

                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                #mailServer.sendmail(gmailaddress, mailto1 , msg)
                mailServer.sendmail(gmailaddress, mailto2 , msg)
                print(" \n Sent!")
                mailServer.quit() 
                errorresponse =""
            else:
                errorresponse = "Please enter the correct room no."
        return render_template('guestOn.html', text1 = response4, text = response, text2 = errorresponse)

if __name__ == "__main__":
    app.run()

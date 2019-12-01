# Innovaccer-Assignment
Entry management software for Innovaccer SDE internship.

# Problem Statement
Given the visitors that we have in office and outside, there is a need to for an entry management software.
We need an application, which can capture the Name, email address, phone no of the visitor and same information also needs to be captured for the host on the front end. At the back end, once the user enters the information in the form, the backend should store all of the information with time stamp of the entry. This should trigger an email and an SMS to the host informing him of the details of the visitor. There should also be a provision of the checkout time which the guest can provide once he leaves. This should trigger an email to the guest with the complete form which should include:

Name
Phone
Check-in time,
Check-out time,
Host name
Address visited.
## Tech Stack

1. Python 3
2. Flask
3. WT forms
4. Twilio- for sending SMS
5. smtplib , ssl - for sending email
6. HTML, CSS Bootstrap- Frontend
7. Firebase- NoSQL database

## Installation
Assuming that the python3 is already installed. Clone the repository.

```
cd innovaccer
pip3 install -r requirements.txt
```

# Development Setup
Approach On the front end there are 4 pages home, host, guest, guestOn. Home asks whether you want to host a meeting or attend a metting.

### 1. If you host a meeting
<br/>
**Frontend:**
<br/>It will take you to host.html where you have enter Name,Contact, Email, Room ( where he want to host the meeting ). Once you click the signup it updates the Databse accordingly.
<br/>
<br/>
**Backend:** The textfields in the host.html page are WT forms, and the data can be directly retrieved in the python code. These values are then updated in the firebase databse. The firebase database required two keys in order to access the database, that is security account key and Google cloud SDK key both can be obtained from the respective sites in the form of JSON. Thus to give access to the database we have used, those two keys are already present in the folder. The database is useless if the JSON file is tampered. Currently the rooms are fixed and the host will have to enter a room from those specified rooms only, and the host's details get updated to the database. 
**Rooms : D317, D123, D205, D113, D215**

### 2. If you want to attend a meeting
<br/>
<br/>**Frontend:** A form appears, on clicking sign up after filling out the form, you have to click on "Proceed to check out", you will be directed to another page guestOn.html which return the time stamp of the user on clicking check out button and on clicking exit user is redirected back to the home page. As the checkout button is clicked a mail is delivered to the user with his respective session details.
<br/>**Backend:** As the guest enters all the details, the room number is checked and the firebase database is updated accordingly to the respective room and host. After clicking on signup, a mail and sms is sent to the host about the guest's session.

**Note:** Make sure you enter the same room number as the host, and while checking out, in order for the room to be alloted properly.

## Server pages
<br/> ```/ ```
<br/>Directs to the main page
<br/> ```/host ```
<br/>Directs to the page for hosts where you can host the meeting
<br/> ```/guest ```
<br/>Directs to the page for guests where you can attend the meeting.
<br/> ```/guestOn ```
<br/>Directs to the page where guest can exit ( redirects to homepage)

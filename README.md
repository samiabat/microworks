
follow the instruction
  # create new directry called basedir
  mkdir basedir
  # get into that path
  cd basedir
  # clone the code
  git clone https://github.com/samiabat/microworks/
  # get into this new directory
  cd microworks
  # create the venv called myenv
  python3 -m venv myenv
  # activate the venv
  source myenv/bin/activate
# install the requirements
  pip install -r requirements.txt
# run the server
  python manage.py runserver
# create mysql database on mysql command shell
create database microworks;
# Next configure the created database(microworks) in the setting.py

  


# Freelancing website Design Technology Documentation.
We are working on a freelancing website which focuses on applying and posting jobs without any different privileges.
Meaning the talent can act like a client on the other side a client can act as a talent according to the situations. For instance the talent can apply a proposal to a job posted by someone. In this way, he can post a job if he wants. The same way  is for a client. He can post a job on the other side he can apply to a job posted by someone else. The main aim for this web application is to minimize the division between clients and talents. A client can act as a talent and vice versa.This makes our web application unique from other freelancing sites in which the users can use only one account  to perform two different tasks as a client and as a talent at the same time. 

# 1)Technical Design
Technologies we are using:
Django Backend Framework
Bootstrap CSS and JS plugin for Frontend framework.
MySQL database
Our future goals in terms of Technologies:
Angular for frontend framework
Django RESTFUL API for backend framework

# How does it work?
Client⇒ Post a job
Talent⇒ Submit proposal for that job
Client ⇒ Choose the best experienced one by understanding the submitted proposals.
Client ⇒ reply to the preferred talent
Talent ⇒ react with the client and vice versa
They can chat within the website or with their own emails.
# Authentications:
 ⇒ Unauthorized users redirected to home page to sign up otherwise they can’t get the applications page i.e posted jobs
⇒ Only authorized users can access the applications page.
⇒ To see the dashboard you have to first register with your username, email, password.
⇒ After registration, the registration page redirects to the login page and the login page redirects to the dashboard page which encompasses the posted jobs, applications for those jobs, update, delete, and submitted proposals page.
⇒ Then you can post your own jobs for finding talents or you can apply for the posted jobs for work.
# Permissions and Authorizations:
⇒ First you have to sign up
⇒ Then you can log in with your account
⇒ Next you can post a job here
⇒ However, you can update or delete only your  jobs.
⇒ You don’t have access to update or delete the others posted jobs.

# 2)Scalability:
We have used :
django ⇒version = 4.0
Bootstrap ⇒version = 5
MySQL database

# Other functionalities
⇒ When you register, django validates your input forms like an email field.
⇒ You can change and reset your password at any time (the email confirmation will be sent to you)
⇒ We have used Gmail for email confirmations.
⇒ You can logout when you want. The page redirects to the home page when you log out from the current page.
⇒ You can upload your photos in your dashboard as SVG, JEPG, JPG, PNG and so on.
⇒ In the account settings page, the form automatically fills the forms that were already filled before and you can fill the forms in your settings page that you didn’t fill before.
# Dreams:
## ⇒The one we have submitted on January 16 2022 is just a demo for what we are going to do. But we are striving to make it functional and reach out to a product using the required technologies.
## ⇒We hope that we will work collaboratively and reach out  this web application to the product stage. 
## ⇒We hope that we will develop this ecommerce platform using Angular for frontend framework and Django RESTFUL API for backend framework.
# Thank you!
# Our contact Address
Name                                                             email                                                 phone
#
1, Samuel Abatneh                     samuelabatneh21@gmail.com                         0921936070
#
2, Sefineh Tesfa                          sefinehtesfa34@gmail.com                              0920627634
#
3, Zenamarkos Molla                  zienamarkos78@gmail.com                              0978070107  


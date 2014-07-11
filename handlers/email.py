from google.appengine.api import mail

message = mail.EmailMessage(sender="Example.com Support <support@example.com>",
                            reply_to="orsenthil@gmail.com",
                            subject="Thank you for your registration.")

message.to = "Albert Johnson <Albert.Johnson@example.com>"

message.body = """
Dear Albert:

Your example.com account has been approved.  You can now visit
http://www.example.com/ and sign in using your Google Account to
access new features.

Please let us know if you have any questions.

The example.com Team
"""

message.html = """
<html><head></head><body>
Dear Albert:

Your example.com account has been approved.  You can now visit
http://www.example.com/ and sign in using your Google Account to
access new features.

Please let us know if you have any questions.

The example.com Team
</body></html>
"""

message.send()


mail.send_mail(sender='shalgreetings@shalgreetings.appspotmail.com',
               to=friendemail,
               reply_to=myemail,
               subject='Hello %s!' % friend,
               body="""
Hello %s,

I have this nice card for you. Hope you like it.

Thanks,
%s

Card from http://www.shalgreetings.com
""" % (friend,me),
               attachments=[('greetings.jpg', chosencard.cardimage)])

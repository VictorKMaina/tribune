import os
from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string

def send_welcome_email(name, email):
    message = Mail(
        from_email="contact@victormaina.com",
        to_emails=email,
        subject="Test Subject",
        html_content = "<h1>This is a test email</h1>")
    
    try:
        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print("\nSENDGRID ERROR: ", e, "\n")


# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# def send_welcome_email(name, receiver):
#     subject = "Welcome to the MoringaTribune Newsletter"
#     sender = "james@moringaschool.com"

#     text_content = render_to_string("email/newsemail.txt", {"name":name})
#     html_content = render_to_string("email/newsemail.html", {"name":name})

#     msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send
from django.core.mail import send_mail

from django.conf import settings 


def success_mail(email,event,date,price):
    subject = 'Event Approved'
    nl = '\n'
    message = f'Hello , Your request for event booking is successfully approved {nl} Event Type: {event} {nl} Date: {date} {nl} Price: {price}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def reject_mail(email,event,date,price):
    subject = 'Event Rejected'
    nl = '\n'
    message = f'Hello , We are sorry to inform you that your request for event booking has been rejected due to some difficulties. Details of rejected event {nl} Event Type: {event} {nl} Date: {date} {nl} Price: {price}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from emailer.utils import send_siteusers_email
        
class Command(BaseCommand):
    args = "None"
    help = 'Process emails with SimpleProcessor'

    def handle(self, *args, **options):
        from_address = 'test@gmail.com'
        subject = 'one off test'
        
        html = '<p>Hello</p>lksjdlfkdj'
        
        users = User.objects.all()
        
        send_siteusers_email(users, from_address, subject, html)
        
        print 'Email Sent'
        
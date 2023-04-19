from django.core.signals import request_started, request_finished
from django.dispatch import receiver
@receiver(request_started)
def start_request(sender, **kwargs):
    print('Start the web request')
@receiver(request_finished)
def finish_request(sender, **kwargs):
    print('Web request finished !')
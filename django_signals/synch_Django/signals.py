import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received at: {timezone.now()}")
    time.sleep(5) 
    print(f"Signal processed at: {timezone.now()}")




# this  is the solution of second question

from django.conf import settings
import threading
import logging



logging.basicConfig(level=logging.INFO)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def log_thread_id(sender, instance, **kwargs):
    logging.info(f"Signal handler running in thread: {threading.get_ident()}")



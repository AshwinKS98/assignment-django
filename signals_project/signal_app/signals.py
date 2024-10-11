from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import sig  
import time
import threading
from django.db import transaction

# Synchronous signal handler
@receiver(post_save, sender=sig)
def sync_signal_handler(sender, instance, created, **kwargs):
    start_time = time.time()
    print(f"Signal received synchronously for {instance.name}")
    time.sleep(2)  
    end_time = time.time()
    print(f"Signal handler executed in {end_time - start_time:.2f} seconds")
# Transaction signal handler
@receiver(post_save, sender=sig)
def transaction_signal_handler(sender, instance, **kwargs):
    with transaction.atomic():
        if instance.name == "Invalid":
            raise Exception("Rolling back transaction")
        print(f"Signal handled in transaction for instance {instance.name}")
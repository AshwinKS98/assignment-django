from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YourModel  
import time
import threading
from django.db import transaction

# Synchronous signal handler
@receiver(post_save, sender=YourModel)
def sync_signal_handler(sender, instance, created, **kwargs):
    start_time = time.time()
    print(f"Signal received synchronously for {instance.name}")
    time.sleep(2)  
    end_time = time.time()
    print(f"Signal handler executed in {end_time - start_time:.2f} seconds")

# Threading signal handler
@receiver(post_save, sender=YourModel)
def threaded_signal_handler(sender, instance, **kwargs):
    thread = threading.Thread(target=handle_in_thread, args=(instance,))
    thread.start()

def handle_in_thread(instance):
    try: 
     print(f"Signal handled in new thread for instance {instance.name}")
    
    except Exception as e:
        print(f"Error in thread: {e}")

# Transaction signal handler
@receiver(post_save, sender=YourModel)
def transaction_signal_handler(sender, instance, **kwargs):
    with transaction.atomic():
        if instance.name == "Invalid":
            raise Exception("Rolling back transaction")
        print(f"Signal handled in transaction for instance {instance.name}")
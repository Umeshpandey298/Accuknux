from django.http import HttpResponse
from django.utils import timezone



def trigger_signal(request):
    print(f"Object creation started at: {timezone.now()}")
    from .models import MyModel
    obj = MyModel.objects.create(name='Test Object')
    print(f"Object creation finished at: {timezone.now()}")
    return HttpResponse("Bydefault,Django signals are executed synchronously. This means that when a signal is sent, the signal handlers are executed in the same process and thread as the code that sent the signal                                                                                                                                           Signal Triggered .")


import threading
import logging
logging.basicConfig(level=logging.INFO)
import time

def trigger_signal_2(request):
    from django.contrib.auth.models import User
    
    logging.info(f"View thread ID: {threading.get_ident()}")

    from .models import MyModel_2
    user = User.objects.create(username=time.time())
    MyModel_2.objects.create(user=user)

    return HttpResponse("Yes, Django signals run in the same thread as the caller. This means that when a signal is triggered, the signal handlers execute in the same thread that sent the signal, not in a different thread.                                                                                                                Signal triggered. Check the logs.")


from django.db import transaction


def create_instance(request):
    from .models import MyModel_3
    with transaction.atomic():  
        instance = MyModel_3(name='Umesh Pandey')
        instance.save()  
        # print("umesh")

    
    updated_instance = MyModel_3.objects.get(pk=instance.pk)
    print(f'Final instance name: {updated_instance.name}')
    return HttpResponse('By default, Django signals run within the same database transaction as the caller. This means if you trigger a signal while in a transaction, the signal handlers execute as part of that same transaction. Therefore, if the transaction is rolled back, any changes made by the signal handlers are also rolled back.                                                                                                                                                                                                                                                                                Signal triggered and instance created.')




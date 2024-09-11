from django.urls import path
# from .views import trigger_signal
from . import views

urlpatterns = [
    path('Question_1_trigger-signal/', views.trigger_signal, name='trigger_signal'),
    path('Question_2_thread_signal/', views.trigger_signal_2, name='trigger_signal_2'),
    path('Question_3_db_signal/', views.create_instance, name='create_instance'),
    

]

from django.urls import path
from .views import add_record, records_list  

urlpatterns = [
    path("add/", add_record, name="add_record"),  
    path("history/", records_list, name="records_list"),  
]

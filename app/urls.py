from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('jspider/', jspider, name = 'jspider'),
]
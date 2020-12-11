from django.urls import path
from . import views

app_name = 'Profile'
urlpatterns=[
    path('report/<int:id>',views.show_report,name="show_report")
]
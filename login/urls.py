from django.urls import path
from rest_framework import routers
from .api import LoginViewSet

from .views import (login_page)

router = routers.DefaultRouter()
router.register('api/', LoginViewSet, 'Loggins')

app_name = ''

urlpatterns = [
    path('', login_page, name ="login-page")
]

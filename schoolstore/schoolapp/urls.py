from django.urls import path, include
from schoolapp.views import home, login, register, new_page

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('new_page/', new_page, name='new_page'),
    # Add more URLs as needed
]

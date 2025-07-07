from django.urls import path
from queryapp.views import EmailIntentView, email_intent_view
from . import views

urlpatterns = [
    path('Intent/', EmailIntentView.as_view(), name='EmailIntent'),
    path('', views.email_intent_view, name='email_intent'),
]

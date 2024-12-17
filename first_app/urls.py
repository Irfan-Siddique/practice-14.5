from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('form_api/',views.form_api, name='form_api'),
    path('django_form/',views.djangoForm, name='django_form'),
    path('submitFormApi/',views.submitFormApi, name='submit_form_api'),
]
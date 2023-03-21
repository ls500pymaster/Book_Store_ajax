from django.urls import path
from app import views
from app.models import Contact

app_name = 'app'

urlpatterns = [
    path('', views.NumberFormView.as_view(), name='modal'),
    path("form/", views.form_test, name="form_test"),
    path("car/", views.car_form, name="car_form"),
    path("contact/", views.contact_form, name="contact_form"),
    path("success/", views.contact_success, name="contact_success"),
]
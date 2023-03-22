from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from app.forms import CarForm, ContactForm
from app.forms import NumberForm
from app.models import Number, Car


# Contact form
def contact_success(request):
    return render(request, 'app/success.html')


def contact_form(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    data = {}
    if is_ajax:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("id_message")
            # print(name, email, subject, message)
            send_mail(subject, message, email, ["admin@example.com"])
            data["status"] = "ok"
            # print(data)
            return JsonResponse(data)
        else:
            data["status"] = "error"
            return JsonResponse(data)
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {"form": form})


# Car
class CarFormView(FormView):
    form_class = CarForm
    template_name = "app/car.html"


def car_form(request, *args, **kwargs):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    form = CarForm()
    data = {}
    if is_ajax:
        form = CarForm(request.POST)
        if form.is_valid():
            data["style"] = form.cleaned_data.get("style")
            data["manufacturer"] = form.cleaned_data.get("manufacturer")
            data["model"] = form.cleaned_data.get("model")
            data["engine_cc"] = int(form.cleaned_data.get("engine_cc"))
            data["status"] = "ok"
            new_car = Car(
                style=data["style"],
                manufacturer=data["manufacturer"],
                model=data["model"],
                engine_cc=int(data["engine_cc"]),
            )
            print(new_car)
            new_car.save()
            return JsonResponse(data)
        else:
            data["status"] = "error"
            return JsonResponse(data)
    context = {"form": form}
    return render(request, "app/car.html", context)


# User-number
class NumberFormView(FormView):
    template_name = "app/home.html"
    form_class = NumberForm


def form_test(request, *args, **kwargs):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    form = NumberForm()
    data = {}
    if is_ajax:
        form = NumberForm(request.POST)
        if form.is_valid():
            data["username"] = form.cleaned_data.get("username")
            data["number"] = form.cleaned_data.get("number")
            data["status"] = "ok"
            new_number = Number(
                username=data["username"],
                number=data["number"])
            new_number.save()
            return JsonResponse(data)
        else:
            data["status"] = "error"
            return JsonResponse(data)
    context = {"form": form}
    return render(request, "app/home.html", context)
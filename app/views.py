from django.shortcuts import render
from django.views.generic import FormView
from app.forms import NumberForm
from django.http import JsonResponse
from app.models import Number, Car
from app.forms import CarForm


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
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from app.forms import NumberForm
from django.http import JsonResponse, BadHeaderError
from app.models import Number, Car
from app.forms import CarForm, ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.mail import send_mail


# Contact form
def contact_success(request):
    return render(request, 'app/success.html')


def contact_form(request):
    data = {}
    form = ContactForm(request.POST)
    if form.is_valid():
        data["name"] = form.cleaned_data.get("name")
        print(data)



    return render(request, 'app/contact.html')
    # is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    # template_name = 'app/contact.html'
    # form_class = ContactForm
    # success_url = reverse_lazy('app:contact_success')
    #
    # def form_valid(self, form):
    #     try:
    #         send_mail(form)
    #         return JsonResponse({'success': True})
    #     except BadHeaderError:
    #         return JsonResponse({'success': False, 'error': 'Invalid header found.'})
    #     except ValidationError as e:
    #         return JsonResponse({'success': False, 'error': e.message})
    #
    # def form_invalid(self, form):
    #     return JsonResponse({'success': False, 'error': 'Invalid form data.'})


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
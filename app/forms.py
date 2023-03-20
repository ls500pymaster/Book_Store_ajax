from django import forms


class NumberForm(forms.Form):
    username = forms.CharField(label="username", required=True, max_length=10)
    number = forms.IntegerField(label="number", required=True)


class CarForm(forms.Form):
    style = forms.CharField(label="style", required=False, max_length=10)
    manufacturer = forms.CharField(label="manufacturer", required=False, max_length=10)
    model = forms.CharField(label="model", required=False, max_length=20)
    engine_cc = forms.IntegerField(label="engine_cc", required=False)

# class CarForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ["style", "manufacturer", "model", "engine_cc", ]

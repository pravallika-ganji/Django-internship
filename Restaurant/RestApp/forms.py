from RestApp.models import Restaurant
from django import forms

class ReForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["rname","nitems","timings","rsimg","address"]
		widgets = {
		"rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter no of items available",
			}),
		"timings":forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter timings",
			"type":"time",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Adress",
			"rows":5,
			}),
		}




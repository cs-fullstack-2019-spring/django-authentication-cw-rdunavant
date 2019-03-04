from django import forms
from .models import FoodFitnessModel
class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model = FoodFitnessModel
        exclude = ["userTableForeignKey"]
        fields = ["username", "calories", "account"]
class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model = usernameModel
        exclude = ["linkUserForeignKey"]
        fields = ["username", "calories", "account"]
class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model = calorieModel
        exclude = ["linkUserForeignKey"]
        fields = ["username", "calories", "account"]

from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "e.g., Grandma's Spicy Pasta", 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Short description', 'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List ingredients separated by commas', 'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Step-by-step instructions', 'class': 'form-control'}),
        }

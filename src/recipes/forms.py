from django import forms
from .models import Ingredient

CHART_CHOICES = (
  ('#1', 'Pie Chart'),
  ('#2', 'Bar Chart'),
  ('#3', 'Line Chart'),
)

class RecipeSearchForm(forms.Form):
  Recipe_Name = forms.CharField(
    required=False,
    max_length=100,
    label='Recipe Name',
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Enter Recipe Name',
        'class': 'form-item',
      }
    )
  )
  Ingredients = forms.ModelMultipleChoiceField(
    required=False,
    queryset=Ingredient.objects.all(),
    label='Ingredients',
    widget=forms.SelectMultiple(
      attrs={
        'class': 'form-item',
      }
    )
  )
  chart_type = forms.ChoiceField(
    choices=CHART_CHOICES, widget=forms.Select(attrs={'class': 'form-item'})
  )

  def clean(self):
    cleaned_data = super().clean()
    recipe_name = cleaned_data.get('Recipe_Name')
    ingredients = cleaned_data.get('Ingredients')

    if not recipe_name and not ingredients:
      raise forms.ValidationError(
        'Please enter a recipe name or select an ingredient'
      )
    return cleaned_data
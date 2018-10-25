from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecipeForm
from .models import Recipe

def recipe_create(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_recipe = form.save()
        return redirect(new_recipe.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'recipes/form.html', context)


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe_detail.html', context)
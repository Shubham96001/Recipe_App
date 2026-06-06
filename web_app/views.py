from django.shortcuts import render, redirect, get_object_or_404
# Views for handling recipe creation, viewing, updating, and deletion.
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from .models import Recipe
from .forms import RecipeForm


def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    form = RecipeForm()
    return render(request, 'recipes/index.html', {'recipes': recipes, 'form': form})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            # Return JSON for AJAX modal submission
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'ok': True, 'id': recipe.id, 'title': recipe.title, 'description': recipe.description, 'ingredients': recipe.ingredients})
            return redirect('recipe_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
    return HttpResponseBadRequest('Invalid request')

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(instance=recipe)
    return render(request, 'recipes/detail.html', {'recipe': recipe, 'form': form})

@require_POST
def recipe_update_ajax(request, pk):
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        return HttpResponseBadRequest('Expected AJAX')
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST, instance=recipe)
    if form.is_valid():
        recipe = form.save()
        return JsonResponse({'ok': True, 'title': recipe.title, 'description': recipe.description, 'ingredients': recipe.ingredients})
    return JsonResponse({'ok': False, 'errors': form.errors}, status=400)

@require_POST
def recipe_delete_ajax(request, pk):
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        return HttpResponseBadRequest('Expected AJAX')
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return JsonResponse({'ok': True})


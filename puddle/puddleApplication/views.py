from django.shortcuts import render, redirect
from puddleApplication.templates import *
from puddleApplication.models import Recipe
# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe-name')
        recipe_desc = data.get('recipe-desc')
        recipe_image = request.FILES.get('recipe-image')
        Recipe.objects.create(
            recipeName=recipe_name,
            recipeDesc=recipe_desc,
            recipeImage=recipe_image
        )
        return redirect('/')
    return render(request,"recipes.html")
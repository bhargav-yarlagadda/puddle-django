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
    queryset = Recipe.objects.all()     
    context = {
        'recipes':queryset
     }
    return render(request,"recipes.html",context=context)
  
def delete_recipe(request,id):

    query_set = Recipe.objects.get(id=id)
    query_set.delete()
    return redirect('/')     

  
def update_recipe(request, id):
    query_set = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe-name')
        recipe_desc = data.get('recipe-desc')
        recipe_image = request.FILES.get('recipe-image')
        
        if recipe_name:
            query_set.recipeName = recipe_name
        if recipe_desc:
            query_set.recipeDesc = recipe_desc
        # Update image only if a new file is uploaded
        if recipe_image:
            query_set.recipeImage = recipe_image
            
        query_set.save()
        return redirect('/')
    
    context = {'recipe': query_set}
    return render(request, 'update.html', context=context)

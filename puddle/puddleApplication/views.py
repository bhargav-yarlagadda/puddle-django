from django.shortcuts import render, redirect, get_object_or_404
from puddleApplication.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login,logout
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
        'recipes': queryset
    }
    return render(request, "recipes.html", context=context)
  
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('/')     

def update_recipe(request, id):
    query_set = get_object_or_404(Recipe, id=id)
    
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
def logout_page(request):
    logout(request=request)
    return redirect('/login')
def login_page(request):
    if request.method == 'POST':
        data = request.POST
        user_name = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=user_name).exists():
            user = authenticate(username=user_name, password=password)
            if user is None:
                messages.error(request, "Invalid password")
                return redirect('/login')
            else:
                login(request, user)  # Pass the request as the first argument
                return redirect('/recipes')
        else:
            messages.error(request, "Invalid username")
            return redirect('/login')
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_name = data.get('username')
        password = data.get('password')
        existing_user = User.objects.filter(username=user_name)
        
        if existing_user.exists():
            messages.info(request, 'Username already exists! Please choose a different username')
            return redirect('/register')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name,
        )
        user.set_password(password)
        user.save()
        return redirect('/login')

    return render(request, 'register.html')

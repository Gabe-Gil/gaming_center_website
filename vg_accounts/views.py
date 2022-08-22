from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from vg_api.models import Game

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created.')
            return redirect('game-login')

    else:
        form = UserCreationForm()

    return render(request, 'vg_accounts/register.html', {'form':form})

@login_required
def profile(request, username):
    return render(request, 'vg_accounts/profile.html')

@login_required
def favorite(request, title):
    if request.method == 'POST':
        favorite = Game.objects.get(title=title)
        user = request.user
        
        if user.profile.favorites.filter(title=title).exists():
            user.profile.favorites.remove(favorite)

            messages.add_message(request, messages.WARNING, f'{title} was removed from your favorites.')

        else:
            user.profile.favorites.add(favorite)

            messages.add_message(request, messages.SUCCESS, f'{title} was added to your favorites.')
        
        return redirect('game_detail', pk=favorite.id)
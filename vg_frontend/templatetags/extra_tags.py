from turtle import title
from django import template
from vg_frontend.models import Playthrough
from vg_api.models import Game

register = template.Library()

def two_most_popular(value):
    temp1 = 0
    temp2 = 0
    temp_game = [None, None]
    game_list = Game.objects.order_by('-release_date')[:5]

    for i in game_list:
        if i.user_rating > temp1:
            temp_game[1] = temp_game[0]
            temp2 = temp1
            temp_game[0] = i
            temp1 = i.user_rating
    
    return temp_game

def find_game_image(value):
    game = Game.objects.filter(title=value).first()
    return game.image_url

def find_game_description(value):
    game = Game.objects.filter(title=value).first()
    return game.description

def find_game_link(value):
    game = Game.objects.filter(title=value).first()
    return game.id

def find_game_critic_rating(value):
    game = Game.objects.filter(title=value).first()
    return game.critic_rating

def find_completed_playthroughs(value, arg):
    playthrough = Playthrough.objects.filter(owner=arg, completed=True).order_by('-created')
    return playthrough

def find_uncompleted_playthroughs(value, arg):
    playthrough = Playthrough.objects.filter(owner=arg, completed=False)
    return playthrough    

register.filter('two_most_popular', two_most_popular)
register.filter('find_game_image', find_game_image)
register.filter('find_game_link', find_game_link)
register.filter('find_game_critic_rating', find_game_critic_rating)
register.filter('find_c_play', find_completed_playthroughs)
register.filter('find_u_play', find_uncompleted_playthroughs)
register.filter('find_game_description', find_game_description)
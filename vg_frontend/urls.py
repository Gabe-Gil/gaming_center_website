from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(template_name='vg_frontend/home.html'), name='game_home'),
    path('game/<int:pk>/', views.GameDetailView.as_view(template_name='vg_frontend/detail.html'), name='game_detail'),
    path('rating/', views.RatingHomeListView.as_view(template_name='vg_frontend/home_ratings.html'), name='game_home_rating'),
    path('search/', views.SearchListView.as_view(template_name='vg_frontend/search.html'), name='search_page'),
    path('search/user-ratings/', views.UserRatingGamesListView.as_view(template_name='vg_frontend/special_search.html'), name='user_ratings_search'),
    path('search/critic-ratings/', views.CriticRatingGamesListView.as_view(template_name='vg_frontend/search.html'), name='critic_ratings_search'),
    path('search/release/', views.ReleaseGamesListView.as_view(template_name='vg_frontend/search.html'), name='release_search'),
    path('search/results/', views.MultiSearchListView.as_view(template_name='vg_frontend/search.html'), name='multi_search_page'),
    path('search/all/', views.AllGamesListView.as_view(template_name='vg_frontend/all_games.html'), name='all_games'),
    path('collection/<str:username>/', views.UserCollectionListView.as_view(template_name='vg_frontend/collection.html'), name='collection'),
    path('favorites/<str:username>/', views.UserFavoriteListView.as_view(template_name='vg_frontend/special_search.html'), name='favorite_list'),
    path('playthrough/new/', views.PlaythroughCreateView.as_view(template_name='vg_frontend/playthrough_add.html'), name='playthrough_add'),
    path('playthrough/update/<int:pk>/', views.PlaythroughUpdateView.as_view(template_name='vg_frontend/playthrough_edit.html'), name='playthrough_update'),
    path('playthrough/delete/<int:pk>', views.PlaythroughDeleteView.as_view(template_name='vg_frontend/playthrough_delete.html'), name='playthrough_delete'),
    path('playthrough/<str:username>/completed/', views.PlaythroughCompleteListView.as_view(template_name='vg_frontend/playthrough_list.html'), name='completed_all'),
    path('playthrough/<str:username>/uncompleted/', views.PlaythroughNotCompleteListView.as_view(template_name='vg_frontend/playthrough_list.html'), name='uncompleted_all'),
]
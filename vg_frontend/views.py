from urllib import request
from vg_api.models import Game
from django.urls import reverse
from vg_api import views, models
from .models import Playthrough
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class HomeListView(ListView):
    model = models.Game
    template_name = 'home.html'
    paginate_by = 10
    ordering = ['-release_date']

class UserCollectionListView(LoginRequiredMixin, ListView):
    model = Playthrough
    context_object_name = 'playthrough_list'

    def get_queryset(self, **kwargs):
        return Playthrough.objects.filter(owner=self.request.user.pk)

class UserFavoriteListView(LoginRequiredMixin, ListView):
    context_object_name = 'search_list'
    ordering = ['-release_date']

    def get_queryset(self):
        return self.request.user.profile.favorites.all()

class PlaythroughCompleteListView(LoginRequiredMixin, ListView):
    context_object_name = 'search_list'
    ordering = ['-release_date']

    def get_queryset(self):
        return Playthrough.objects.filter(owner=self.request.user, completed=True)
       

class PlaythroughNotCompleteListView(LoginRequiredMixin, ListView):
    context_object_name = 'search_list'
    ordering = ['-release_date']

    def get_queryset(self):
        return Playthrough.objects.filter(owner=self.request.user, completed=False).order_by('-created')
        

class RatingHomeListView(ListView):
    model = models.Game
    template_name = 'home.html'
    paginate_by = 12
    ordering = ['-critic_rating']

class GameDetailView(DetailView):
    model = models.Game
    template_name = 'detail.html'
    context_object_name = 'game'

class AllGamesListView(ListView):
    model = models.Game
    template_name = 'all_games.html'
    paginate_by = 10
    ordering = ['-release_date']

class UserRatingGamesListView(ListView):
    model = models.Game
    template_name = 'special_search.html'
    paginate_by = 10
    ordering = ['-user_rating']
    context_object_name = 'search_list'

class CriticRatingGamesListView(ListView):
    model = models.Game
    template_name = 'search.html'
    paginate_by = 10
    ordering = ['-critic_rating']
    context_object_name = 'search_list'

class ReleaseGamesListView(ListView):
    model = models.Game
    template_name = 'search.html'
    paginate_by = 10
    ordering = ['-release_date']
    context_object_name = 'search_list'

class MultiSearchListView(ListView):
    template_name = 'search.html'
    paginate_by = 10
    model = models.Game
    context_object_name = 'search_list'
    ordering = ['-release_date']

    def get_queryset(self):
        result = super(MultiSearchListView, self).get_queryset()

        title = self.request.GET.get('title-search')
        genres = self.request.GET.get('genre-search')
        publisher = self.request.GET.get('publisher-search')
        developer = self.request.GET.get('developer-search')
        platforms = self.request.GET.get('platform-search')

        if title or genres or publisher or developer or platforms:
            if title:
                postresult = models.Game.objects.filter(title__icontains=title)

            if genres:
                postresult = models.Game.objects.filter(genres__icontains=genres)

            if publisher:
                postresult = models.Game.objects.filter(publisher__icontains=publisher)

            if developer:
                postresult = models.Game.objects.filter(developer__icontains=developer)

            if platforms:
                postresult = models.Game.objects.filter(platforms__icontains=platforms)
            
            result = postresult.order_by('-release_date')
            
        else:
            result = None

        if result:
            return result
        else:
            return []

class SearchListView(ListView):
    template_name = 'search.html'
    paginate_by = 10
    model = models.Game
    context_object_name = 'search_list'
    ordering = ['-release_date']

    def get_queryset(self):
        result = super(SearchListView, self).get_queryset()
        query = self.request.GET.get('search')

        if query:
            postresult = models.Game.objects.filter(title__icontains=query)
            result = postresult.order_by('-release_date')
        else:
            result = None

        if result:
            return result
        else:
            return []

class PlaythroughCreateView(LoginRequiredMixin, CreateView):
    model = Playthrough
    fields = ['game', 'playthrough_title', 'completed']

    def get_success_url(self):
        return reverse('collection', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PlaythroughUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Playthrough
    fields = ['game', 'playthrough_title', 'completed']

    def get_success_url(self):
        return reverse('collection', kwargs={'username': self.request.user.username})

    def test_func(self):
        playthrough = self.get_object()

        if self.request.user == playthrough.owner:
            return True
        
        else:
            return False

class PlaythroughDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Playthrough

    def get_success_url(self):
        return reverse('collection', kwargs={'username': self.request.user.username})

    def test_func(self):
        playthrough = self.get_object()

        if self.request.user == playthrough.owner:
            return True
        
        else:
            return False
from django.shortcuts import render
from django.views import View
from home.functions import HomeFunction
class HomeView(View):
    def get(self, request):
        func_obj = HomeFunction()
        top_posts = func_obj.get_top_posts()
        feature_posts = func_obj.get_feature_posts()
        popular_posts = func_obj.get_popular_posts()
        data = {
            'top_posts' : top_posts,
            'feature_posts' : feature_posts,
            'popular_posts':popular_posts,
        }
        return render(request, 'home.html',data)

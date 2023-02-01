from django.shortcuts import render
from django.views import View
from blogpost.models import BlogModel
# Create your views here.
class BlogPostView(View):
    def get(self,request,id):
        single_post = BlogModel.objects.get(id=id)
        data ={
            'single_post':single_post
        }
        return render(request, 'blogpost/blogpost.html',data)
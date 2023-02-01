from django.urls import path
from blogpost.views import BlogPostView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('post/<int:id>',BlogPostView.as_view(),name= "blogpost" ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
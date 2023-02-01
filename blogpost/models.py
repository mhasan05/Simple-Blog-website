from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
# Create your models here.



class CatagoryModel(models.Model):
    class Meta:
        verbose_name_plural ="Catagory"
    name = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)



class BlogModel(models.Model):
    class Meta:
        verbose_name_plural ="All Post"
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images/blog_image")
    created = models.DateTimeField(auto_now_add=True)
    catagory = models.ForeignKey(CatagoryModel,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)
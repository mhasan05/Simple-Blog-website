from blogpost.models import BlogModel
import random
class HomeFunction():
    def get_top_posts(self):
        all_posts = BlogModel.objects.all()
        top_posts = []
        for post in all_posts:
            if str(post.catagory) == 'Top':
                top_posts.append(post)
        top_posts.reverse() # reverse
        return top_posts

    def get_feature_posts(self):
        all_posts = BlogModel.objects.all()
        feature_posts = []
        for post in all_posts:
            if str(post.catagory) == 'Feature':
                feature_posts.append(post)
        feature_posts.reverse() # reverse
        return feature_posts

    def get_popular_posts(self):
        all_posts = BlogModel.objects.all()
        popular_posts = []
        for post in range(5):
            random_post = random.choice(all_posts)
            popular_posts.append(random_post)
        return popular_posts
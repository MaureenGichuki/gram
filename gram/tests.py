from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mo= Profile(user= 'mo', bio ='hello')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mo,Profile))

        # Testing Save Method Profile
    def test_save_method(self):
        self.mo.profile()
        users = Profile.objects.all()
        self.assertTrue(len(users) > 0)

class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new Post
        self.foodie= Post(caption = 'foodie',pic="logo.png")

    def test_instance(self):
        self.assertTrue(isinstance(self.greece,Post))

    def test_save_method(self):
        self.foodie.post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

class CommentTestClass(TestCase):
    # Creating a new Comment

    def setUp(self):
        self.hey= Comment(username= 'momo',comment = 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.hey,Comment))

    def test_save_method(self):
        self.hey.comment_save
        comment = Comment.objects.all()
        self.assertTrue(len(comment) > 0)

class FollowingTestClass(TestCase):

    def setUp(self):
        self.momo= Following(username= 'momo')

    def test_instance(self):
        self.assertTrue(isinstance(self.hey,Following))

    def test_save_method(self):
        self.momo.following
        following = Following.objects.all()
        self.assertTrue(len(following) > 0)





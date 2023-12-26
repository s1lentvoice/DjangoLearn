from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post

User = get_user_model()

class PostTest(TestCase):
    def setUp(self):
        author_1 = User.objects.create(username='author #1')
        author_2 = User.objects.create(username='author #2')
        
        Post.objects.create(title='First post',
                            text='text',
                            author=author_1)
        Post.objects.create(title='Second post',
                            text='text',
                            author=author_2)
        
    def test_publish_method_for_post(self):
        post = Post.objects.get(title='First post')
        post.publish()
        self.assertEqual(post.is_publish(), True)

    def test_published_post_filtering(self):
        post = Post.objects.get(title='First post')
        post.publish()
        posts = Post.published.all()
        self.assertEqual(posts.count(), 1)
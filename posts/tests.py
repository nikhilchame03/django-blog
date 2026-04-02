from django.test import TestCase,Client
from django.contrib.auth.models import User

from django.utils import timezone
from .models import Post
import datetime



class PostModelTest(TestCase):

    def test_post_published_in_past(self):
        time=timezone.now() - datetime.timedelta(days=20)
        old_post=Post(created_at=time)
        self.assertIs(old_post.was_published_in_past(),True)


    def test_post_published_in_future(self):
        time=timezone.now()+ datetime.timedelta(days=10)
        future_post=Post(created_at=time)
        self.assertIs(future_post.was_published_in_past(),False)


    def test_post_published_recently(self):

        time=timezone.now() - datetime.timedelta(days=20)
        old_post=Post(created_at=time)
        self.assertIs(old_post.was_published_recently(),False)



class IndexPageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_loads_successfully(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

   


    def test_posts_are_ordered_latest_first(self):
        old_post = Post.objects.create(
            title='Old',
            body='Old Body',
            created_at=timezone.now() - datetime.timedelta(days=1)
        )
        new_post = Post.objects.create(
            title='New',
            body='New Body',
            created_at=timezone.now()
        )
        response = self.client.get('/')
        posts = list(response.context['posts'])
        self.assertEqual(posts[0], new_post)
        self.assertEqual(posts[1], old_post)







class DraftTest(TestCase):

    def setUp(self):
        self.client=Client()


    def test_draft_saved_for_unauthenticated_user(self):

        self.client.post('/create',{
            'title':"Test Title",
            'body':'Test Body'
        })

        self.assertIn('draft_post',self.client.session)


    def test_draft_saved_after_create_and_then_login(self):
        
        session=self.client.session
        session['draft_post']={'title':"Test Title",
            'body':'Test Body'}
        session.save()

        response=self.client.get('/create')
        self.assertContains(response,'Test Title')
        self.assertContains(response, 'Test Body')

    
    def test_draft_saved_after_login_redirect(self):
        
        self.client.post('/create',{
            'title':"Test Title",
            'body':'Test Body'
        })

        self.assertIn('draft_post',self.client.session)

    def test_draft_gets_clear_after_submit(self):
        
        user=User.objects.create_user(username='test',password='Test@12345')
        self.client.login(username='test',password='Test@12345')

        session=self.client.session
        session['draft_post'] = {'title': 'Draft', 'body': 'Draft Body'}
        session.save()

        self.client.post('/create', {
            'title': 'Final Title',
            'body': 'Final Body'
        })

        self.assertNotIn('draft_post', self.client.session)


class PostDetailTest(TestCase):

    def setUp(self):
        self.post=Post.objects.create(
            title='Test Post',
            body='Test Body',
            created_at=timezone.now()
        )

    def test_valid_post_returns_200(self):
        response = self.client.get(f'/post/{self.post.id}')
        self.assertEqual(response.status_code, 200)


    def test_post_detail_title_and_body(self):
        response = self.client.get(f'/post/{self.post.id}')
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Body')


    def test_post_detail_without_login(self):
        response = self.client.get(f'/post/{self.post.id}')
        self.assertEqual(response.status_code, 200)
    
    





    


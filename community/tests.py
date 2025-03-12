# This file contains the tests for the community app.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib import messages


class CommunityTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

        # Create a second test user
        self.user2 = User.objects.create_user(username='testuser2',
                                              password='testpassword2')

        # Create a test post by the test user
        self.post = Post.objects.create(author=self.user, content='Test '
                                        'post content')

        # Create a test client
        self.client = Client()

    def test_community_page_get(self):
        """Test that community page loads correctly."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('community'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/community.html')
        self.assertIn('posts', response.context)

    def test_community_page_post_valid(self):
        """Test creating a valid post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('community'),
                                    {'content': 'New test post'})
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        # Check that a new post was created
        self.assertEqual(Post.objects.count(), 2)
        self.assertRedirects(response, reverse('community'))

        # Check success message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Post submitted successfully!")

    def test_community_page_post_invalid(self):
        """Test creating an invalid (empty) post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('community'), {'content': ''})
        self.assertEqual(response.status_code, 302)  # Redirect even with error
        self.assertEqual(Post.objects.count(), 1)
        self.assertRedirects(response, reverse('community'))

        # Check error message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Post can't be empty.")

    def test_edit_post_get(self):
        """Test loading the edit post page."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/edit_post.html')
        self.assertEqual(response.context['post'], self.post)

    def test_edit_post_post_valid(self):
        """Test submitting a valid edit to a post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_post', args=[self.post.id]),
                                    {'content': 'Updated test post'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('community'))
        self.post.refresh_from_db()  # Reload the post from the database
        self.assertEqual(self.post.content, 'Updated test post')

        # Check success message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Post updated successfully!")

    def test_edit_post_post_invalid(self):
        # Test submitting an invalid (empty) edit to a post.
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_post', args=[self.post.id]),
                                    {'content': ''})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('community'))
        self.post.refresh_from_db()
        # Content should not change
        self.assertEqual(self.post.content, 'Test post content')

        # Check error message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Post content can't be empty.")

    def test_edit_post_unauthorized(self):
        """Test that a user can't edit someone else's post."""
        self.client.login(username='testuser2', password='testpassword2')
        response = self.client.get(reverse('edit_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "You can only edit your "
                         "own posts.")

    def test_delete_post_get(self):
        """Test loading the delete post confirmation page."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/confirm_delete.html')
        self.assertEqual(response.context['post'], self.post)

    def test_delete_post_post(self):
        """Test deleting a post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_post',
                                            args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('community'))
        self.assertEqual(Post.objects.count(), 0)

        # Check success message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Post deleted successfully!")

    def test_delete_post_unauthorized(self):
        """Test that a user can't delete someone else's post."""
        self.client.login(username='testuser2', password='testpassword2')
        response = self.client.post(reverse('delete_post',
                                            args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)  # Post should still exist
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "You can only delete your "
                         "own posts.")

    def test_add_comment_post(self):
        """Test adding a comment to a post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_comment',
                                            args=[self.post.id]),
                                    {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('community'))
        self.assertEqual(Comment.objects.count(), 1)

        # Check success message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Comment added successfully!")

    def test_add_comment_post_invalid(self):
        """Test adding an invalid (empty) comment to a post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_comment', args=[self.post.id]),
                                    {'content': ''})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('community'))
        self.assertEqual(Comment.objects.count(), 0)

        # Check error message
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Comment can't be empty.")

from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser





# Create your tests here.
class MailSendingResult( TestCase ):
      
      # The function needs to start with "test_" in order for django to understand that this is a test_function!!!
      def test_homepage_exists( self ):
            response = self.client.get( reverse( "home" ) )
            self.assertEqual( response.status_code, 200 )  # does the signup page exist
            self.assertTemplateUsed( response, "users/home.html" )  # does the signup page use the correct template
      
      
      
      def test_signup_with_new_user( self ):
            userdata = {
                  'email':      'test@xxx.com',
                  'first_name': 'test',
                  'last_name':  'test',
                  'username':   'test@xxx.com',
                  'password1':  'password123',
                  'password2':  'password123',
            }
            response = self.client.post( reverse( "users:signup" ), userdata, format='text/html' )
            self.assertEqual( response.status_code, 200 )  # the code for a redirect is 302 and NOT 200 --> we should see an error (apart from that the signup page is not existing)
            # if we have a signup a signals should be fired --> and create an entry for the user in the database
            response = self.client.get( reverse( "userprofile" ), args=[ userdata[ 'email' ] ] )
            self.assertEqual( response.status_code, 200 )





class BaseSetup( TestCase ):
      
      # Class to be inherited from by other classes --> for the profile change page
      
      def setup( self ):
            """
            Setup function to be used by other tests, which need a user to be registered
            in order to be run. This function registers a user with the given userdata
            and then logs in. The userdata is as follows:
            
            userdata = {
                  'email':      'test@xxx.com',
                  'first_name': 'test',
                  'last_name':  'test',
                  'username':   'test@xxx.com',
                  'password1':  'password123',
                  'password2':  'password123',
            }
            
            Note: This function does NOT login the user after registration. If you want
            to login the user, you have to call the login function explicitly.
            """
            userdata = {
                  'email':      'test@xxx.com',
                  'first_name': 'test',
                  'last_name':  'test',
                  'username':   'test@xxx.com',
                  'password1':  'password123',
                  'password2':  'password123',
            }
            response = self.client.post( reverse( "users:signup" ), userdata, format='text/html' )





class ProfileEditClass( BaseSetup ):
      
      def test_profile_edit_page( self ):
            self.client.logout()  # if we want to logout (as we logged in, in the super() class)
            response = self.client.get( reverse( 'user:profile_edit' ) )
            self.assertEqual( response.status_code, 200 )  # Check if the page exists
            
            # perform a test by changing the first_name of the newly created user
            form_data = {
                  'first_name': 'Franz',
            }
            response = self.client.post( reverse( 'user:profile_edit' ), data=form_data )
            self.assertEqual( response.status_code, 302 )  # We should get another redirect for this function
            self.user = CustomUser.objects.get( email='test@xxx.com' )
            self.assertEqual( self.user.first_name, form_data.get( 'first_name' ) )
            
            # # if we use signals we should also have a second model for the user profile
            # profile = Profile.objects.get( user=self.user )
            # self.assertEqual( profile.email = 'test@xxx.com' )





class PostCreateTest( BaseSetup ):
      
      def test_createPost( self ):
            response = self.client.get( reverse( 'user:post-create' ) )
            self.assertEqual( response.status_code, 200 )
            
            form_data = {
                  'url':  'https://example.com',
                  'body': 'Lorem Ipsum...',
            }
            # self.user = User.objects.get(username='test@xxx.com')
            post_data = {
                  'url':    form_data.url,
                  'body':   form_data.body,
                  'title':  'Test Title',
                  'image':  'https://picsum.photos/5000',
                  'artist': 'Steve',
                  'author': self.user,
            }
            # post = Post.objects.create( **post_data )
            # self.assertTrue( Post.objects.filter( title=post_data.title ).exists() )
            
            # check if the post with the title 'test' also exists on the homepage
            homepage = self.client.get( reverse( 'home' ) )
            self.assertContains( homepage, 'Test' )
            
            # Check if the post is also gone on the homepage if we delete the post
            # post.delete()
            homepage = self.client.get( reverse( 'home' ) )
            self.assertNotContains( homepage, 'Test' )

from django.contrib.auth import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse('users:singup'),
                         data={
                             'username':'tohirjon',
                             'first_name':'tohirjon1',
                             'last_name':"sadiqov",
                             'email':"sadiqovtohirjon@gmail.com",
                             'password':'20022020'
                            }
                         )
        user=CustomUser.objects.get(username='tohirjon')
        self.assertEqual(user.first_name,'tohirjon1')
        self.assertEqual(user.last_name,'sadiqov')
        self.assertEqual(user.email,'sadiqovtohirjon@gmail.com')
        self.assertNotEqual(user.password,'20022020')
        self.assertTrue(user.check_password('20022020'))

    def test_required_fields(self):
            response=self.client.post(
                reverse('users:singup'),
                data={
                    'first_name':'tohirjon',
                    'passsword':'20022020'
                }

            )
            count=CustomUser.objects.count()
            self.assertEqual(count,0)
            self.assertFormError(response,'form','username','This field is required.')
            self.assertFormError(response,'form','password','This field is required.')

    def test_invalid_email(self):
        reponse=self.client.post(reverse('users:singup'),
                         data={
                             'username':'tohirjon',
                             'first_name':'tohirjon1',
                             'last_name':"sadiqov",
                             'email':"sadiqovtohir",
                             'password':'20022020'
                            }
                         )
        count = CustomUser.objects.count()
        self.assertEqual(count, 0)
        self.assertFormError(reponse,'form','email','Enter a valid email address.')

    def test_unique_username(self):
        user=CustomUser.objects.create_user('tohirjon','tohirjon1')

        response=self.client.post(reverse('users:singup'),
                         data={
                             'username': 'tohirjon',
                             'first_name': 'tohirjon1',
                             'last_name': "sadiqov",
                             'email': "sadiqovtohirjon@gmail.com",
                             'password': '20022020'
                         }
                         )
        count = CustomUser.objects.count()
        self.assertEqual(count, 1)
        self.assertFormError(response,'form','username','A user with that username already exists.')


class PasgeTestCase(TestCase):
    def test_success_get(self):
        response=self.client.get(reverse('users:singup'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Registrtion Page')
        self.assertTemplateNotUsed(response,'singup.html')

class LoginTestCase(TestCase):
    def setUp(self):
        self.user_db = CustomUser.objects.create_user(username='tohirjon')
        self.user_db.set_password('20022020')
        self.user_db.save()

    def test_succsesful_login(self):


        self.client.post(reverse('users:login'),
            data={
            'username':'tohirjon',
            'first_name':'tohrion1',
            'last_name':'sadiqov',
            'email':'sadiqovtohirjon@gmail.com',
            'password':'20022020'
        })
        user=get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_login(self):

        self.client.post(
            reverse('users:login'),
            data={
                'username':'tohirjon1',
                'password':'200220201'
            }
        )
        user=get_user(self.client)
        self.assertFalse(user.is_authenticated)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):


        self.client.login(username='tohirjon',password='20022020')
        self.client.get(reverse('users:logout'))

        user=get_user(self.client)
        self.assertFalse(user.is_authenticated)


  
class ProfileTestCase(TestCase):
    def test_login_required(self):
        user=CustomUser.objects.create(username='tohirjon',first_name='tohirjon',last_name='sadiqov',email='Sadiqovtohirjon@gamil.com')
        user.set_password('20022020')
        user.save()

        self.client.login(username='tohirjon',password='20022020')
        response=self.client.get(reverse('users:profile'))

        self.assertEqual(response.status_code,200)
        self.assertContains(response,user.username)

    def test_required(self):
        respone=self.client.get(reverse('users:login'))

        self.assertEqual(respone.status_code,200)
    def test_update_user(self):
        user = CustomUser.objects.create(username='tohirjon', first_name='tohirjon', last_name='sadiqov',
                                   email='Sadiqovtohirjon@gamil.com')
        user.set_password('20022020')
        user.save()
        self.client.login(username='tohirjon', password='20022020')
        response=self.client.post(reverse('users:profile-edit'),
                    data={
                        'username':'tohirjon',
                        'first_name':'tohirjon',
                        'last_name':'Sadiqov1',
                        'email':'sadiqovtohirjon000@gmail.com'
                    }
                                  )

        user.refresh_from_db()

        self.assertEqual(user.last_name,'Sadiqov1')







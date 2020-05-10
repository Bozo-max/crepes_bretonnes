from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserTest(TestCase):
    def test_good_user(self):
        data = {
          'pseudo' : 'Bozo',
          'password' : 'coucou',
          'password2' : 'coucou',
          'is_author' : False,
          'email' : 'benjamin.fargeton@hotmail.fr'
        }

        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code,302)
        user = User.objects.get(username = data['pseudo'])

        self.assertTrue(user.check_password(data['password']))
        self.assertNotEqual(user.password, 'coucou')


# Create your tests here.

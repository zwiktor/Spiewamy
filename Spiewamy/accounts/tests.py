from django.test import TestCase
from selenium import webdriver

from .models import User

class StartHomrPageTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn('Spiewamy', self.driver.title)


class UsersRegisterTest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username="testUser", password="123qwe123", email="mail@gmail.com")
        User.objects.create_user(username="testerUssser", password="qwe12qwe", email="mail2@gmail.com")

    def tearDown(self) -> None:
        user1 = User.objects.filter(username='testUser')
        user2 = User.objects.filter(username='testerUssser')
        user1.delete()
        user2.delete()

    def test_is_user_created(self):
        user = User.objects.filter(username='testUser')
        obj_user = user[0]
        self.assertTrue(user.exists())
        self.assertFalse(obj_user.is_superuser)
        self.assertTrue(obj_user.is_authenticated)
        self.assertNotEqual(obj_user.password, '123qwe123')
# Create your tests here.

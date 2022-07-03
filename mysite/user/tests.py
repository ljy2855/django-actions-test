from django.test import TestCase
from .models import CustomUser
from django.contrib.auth.models import User
class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        u = User.objects.create_user("testname","test@example.com","password")
        if u:
            CustomUser.objects.create(user=u)
        return super().setUpTestData()

    def testCheckAllUser(self):
        self.assertIsNotNone(CustomUser.objects.all())
# Create your tests here.

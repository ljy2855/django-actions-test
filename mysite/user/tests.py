from django.test import TestCase
from models import CustomUser
from django.contrib.auth.models import User
class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        u, created = User.objects.create("testname","test@example.com","password")
        if created:
            CustomUser.objects.create(user=u)
        return super().setUpTestData()

    def testCheckAllUser(self):
        self.assertIsNone(CustomUser.objects.all())
# Create your tests here.

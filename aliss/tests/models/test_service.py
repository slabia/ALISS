from django.test import TestCase
from aliss.models import Organisation, ALISSUser, Service, Location
from aliss.tests.fixtures import Fixtures

class ServiceTestCase(TestCase):
    def setUp(self):
        t,u,c,_ = Fixtures.create_users()
        o = Fixtures.create_organisation(t, u, c)
        s = Service.objects.create(name="My First Service", description="A handy service", organisation=o, created_by=t, updated_by=u)

    def test_service_exists(self):
        s = Service.objects.get(name="My First Service")
        self.assertTrue(isinstance(s, Service))

    def test_service_slugs(self):
        s1 = Service.objects.get(name="My First Service")
        s2 = Service.objects.create(name="My First Service", description="A handy service", organisation=s1.organisation, created_by=s1.created_by)
        self.assertEqual(s1.slug, "my-first-service-0")
        self.assertEqual(s2.slug, "my-first-service-1")

    def test_user_delete_doesnt_cascade(self):
        ALISSUser.objects.get(email="tester@aliss.org").delete()
        ALISSUser.objects.get(email="updater@aliss.org").delete()
        self.test_service_exists()

    def test_org_delete_cascades(self):
        Organisation.objects.get(name="TestOrg").delete()
        s = Service.objects.filter(name="My First Service").exists()
        self.assertFalse(s)

    def test_is_edited_by(self):
        s = Service.objects.get(name="My First Service")
        rep    = ALISSUser.objects.get(email="claimant@user.org")
        editor = ALISSUser.objects.filter(is_editor=True).first()
        punter = ALISSUser.objects.create(name="Ms Random", email="random@random.org")
        staff  = ALISSUser.objects.create(name="Ms Staff", email="msstaff@aliss.org", is_staff=True)
        self.assertTrue(s.is_edited_by(s.organisation.created_by))
        self.assertTrue(s.is_edited_by(staff))
        self.assertTrue(s.is_edited_by(editor))
        self.assertTrue(s.is_edited_by(rep))
        self.assertFalse(s.is_edited_by(punter))
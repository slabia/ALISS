from django.test import TestCase, Client
from django.urls import reverse
from aliss.tests.fixtures import Fixtures
from aliss.models import Organisation, ALISSUser, Service, Location
from aliss.filters import OrganisationFilter

class OrganisationFilterTestCase(TestCase):
    def setUp(self):
        self.user, self.editor, self.claimant, self.staff = Fixtures.create_users()
        self.client.login(username='tester@aliss.org', password='passwurd')
        self.organisation = Fixtures.create_organisation(self.user, self.editor, self.claimant)
        self.org2 = Organisation.objects.create(
          name="Another's Test Org",
          description="A test description",
          created_by=self.user,
          published=True
        )

    def test_basic_query(self):
        f = OrganisationFilter({ "q": "test" })
        exists = f.qs.filter(pk=self.organisation.pk).exists()
        self.assertEqual(exists, True)
        self.assertEqual(f.qs.count(), 2)

    def test_space_query(self):
        f = OrganisationFilter({ "q": "te st" })
        exists = f.qs.filter(pk=self.organisation.pk).exists()
        self.assertEqual(exists, True)
        self.assertEqual(f.qs.count(), 2)

    def test_stripping_query(self):
        f = OrganisationFilter({ "q": "tes't" })
        exists = f.qs.filter(pk=self.organisation.pk).exists()
        self.assertEqual(exists, True)
        self.assertEqual(f.qs.count(), 2)

    def test_apostrophe_query(self):
        f = OrganisationFilter({ "q": "another\'s test" })
        exists = f.qs.filter(pk=self.org2.pk).exists()
        self.assertEqual(exists, True)
        self.assertEqual(f.qs.count(), 1)

    def test_no_apostrophe_query(self):
        f = OrganisationFilter({ "q": "anothers test" })
        f2 = OrganisationFilter({ "q": "anothers" })
        exists = f.qs.filter(pk=self.org2.pk).exists()
        exists2 = f2.qs.filter(pk=self.org2.pk).exists()
        self.assertEqual(exists, True)
        self.assertEqual(exists2, True)
        self.assertEqual(f.qs.count(), 1)
        self.assertEqual(f2.qs.count(), 1)

    def test_fail_query(self):
        f = OrganisationFilter({ "q": "test\'s test" })
        self.assertEqual(f.qs.count(), 0)

    def tearDown(self):
        for organisation in Organisation.objects.filter(name="Another's Test Org"):
            organisation.delete()
        for organisation in Organisation.objects.filter(name="TestOrg"):
            organisation.delete()

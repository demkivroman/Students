from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from students.models import Students, Group


class TestStudentList(TestCase):

    def setUp(self):
        # create groups
        group1, created = Group.objects.get_or_create(title="MtM-1")
        group2, created = Group.objects.get_or_create(title="MtM-2")

        # create 4 students: 1 for group1 and 3 for for group2
        Students.objects.get_or_create(
        first_name = "Vilaliy",
        last_name = "Podoba",
        birthday = datetime.today(),
        ticket = '12345',
        student_group = group1)

        Students.objects.get_or_create(
        first_name = "John",
        last_name = "Dobson",
        birthday = datetime.today(),
        ticket = '2345',
        student_group = group2)

        Students.objects.get_or_create(
        first_name = "Sam",
        last_name = "Stephenson",
        birthday = datetime.today(),
        ticket = '45678',
        student_group = group2)

        Students.objects.get_or_create(
        first_name = "Roman",
        last_name = "Demkiv",
        birthday = datetime.today(),
        ticket = '55555',
        student_group = group2)

        # remember test browser
        self.client = Client()


        self.url = reverse('home')

    def test_students_list(self):
        # make request to the server to get homepage page
        response = self.client.get(self.url)

        # have we receive OK status from the server?
        self.assertEqual(response.status_code, 200)

        # do we have student name on a page?
        self.assertIn('Podoba', response.content)

        # do we have link to student edit form?
        self.assertIn(reverse('students_edit',
            kwargs={'pk': Students.objects.all()[0].id}),
            response.content.decode('utf-8'))


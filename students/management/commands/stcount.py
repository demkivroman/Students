from django.core.management.base import BaseCommand

from students.models import Students, Group
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Prints to console number of students related objects in a database"
    models = (('student',Students),('group',Group),('user',User))

    def add_arguments(self, parser):
        parser.add_argument('db')
    
    def handle(self, *args, **options):
        for name, model in self.models:
            if name in options['db']:
                self.stdout.write('Number of %ss in database: %d' % (name, model.objects.count()))

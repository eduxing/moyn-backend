from django.core.management.base import BaseCommand
from communities.models import Community

class Command(BaseCommand):
    help = 'Empties the specified table'

    def handle(self, *args, **kwargs):
        Community.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully emptied the table'))

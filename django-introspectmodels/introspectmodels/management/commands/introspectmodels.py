from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Introspect models of your project'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("calling introspect models")


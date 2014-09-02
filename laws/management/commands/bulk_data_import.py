from django.core.management.base import BaseCommand, CommandError
from laws.models import Bill, Version, Document, Action, Title, Vote, Voter, Source, Sponsor

from optparse import make_option


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
            make_option('--directory',
                dest='directory',
                default='data',
                help='Directory which contains bulk OpenStates Data to load.'),
            )

    def handle(self, *args, **options):
        pass


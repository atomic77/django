from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Be very demanding with parameters"
    args = ''
    requires_system_checks = True

    def add_arguments(self, parser):
        parser.add_argument("integer", nargs='?', type=int, default=0)
        parser.add_argument("-s", "--style", default="Rock'n'Roll")
        parser.add_argument("-x", "--example")
        parser.add_argument("--opt-3", action='store_true', dest='option3')
        parser.add_argument("-n", "--need-me", required=True)
        parser.add_argument("-t", "--need-me-too", required=True, dest='needme2')

    def handle(self, *args, **options):
        example = options["example"]
        if example == "raise":
            raise CommandError()
        if options['verbosity'] > 0:
            self.stdout.write(','.join(options))
        if options['integer'] > 0:
            self.stdout.write("You passed %d as a positional argument." % options['integer'])

import json
import logging
from django.core.management.base import BaseCommand, CommandParser
from survey.models import StateMaster, DistrictMaster

logger = logging.getLogger("load_districts_logger")
logger.setLevel(level=logging.DEBUG)


class Command(BaseCommand):
    help = "Load the country and state fixture."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "json_file", type=str,
            help="Path for the json file consisting of district data."
        )

    def load_districts(self, districts_path: str):
        """
        Helper function to load districts according to states
        in the database.

        Args:
        ---------

        districts_path: str
            The path where districts json file exists.
        """

        with open(districts_path, 'r') as dist_file:
            dist_data = json.load(dist_file)
            self.stdout.write(self.style.SUCCESS(
                'Loaded the District JSON file succesfully!'))
            logger.info("Loaded the District JSON file succesfully!")

        for key, value in dist_data.items():
            try:
                state_obj = StateMaster.objects.get(state=key.capitalize())
                self.stdout.write(self.style.SUCCESS(
                    f"{state_obj.state} State obj loaded."))
                logger.info("State obj loaded.")
            except StateMaster.DoesNotExist:
                self.stdout.write(self.style.SUCCESS(
                    f"The {key} doesn't exist in database. creating the obj."))
                logger.info(
                    f"The {key} doesn't exist in database. creating the obj.")
                state_obj = StateMaster.objects.create(
                    state=key
                )
                state_obj.save()
                self.stdout.write(self.style.SUCCESS(
                    f"{key} state saved successfuly in the database."))
                logger.info(f"{key} state saved successfuly in the database.")

            for district in value:
                district_obj = DistrictMaster.objects.create(
                    district=district,
                    state=state_obj
                )
                self.stdout.write(self.style.SUCCESS(
                    f"{district_obj.district} district in {key} state created successfuly."))
                district_obj.save()
                self.stdout.write(self.style.SUCCESS(
                    f"{district_obj.district} district in {key} state saved successfuly in the database."))
                logger.info(
                    f"{district_obj.district} district in {key} state saved successfuly in the database.")

    def handle(self, *args, **options):
        file = options['json_file']
        if not file.endswith('.json'):
            self.stdout.write("The file should be a json file.")
            return

        self.load_districts(file)

        self.stdout.write(self.style.SUCCESS(
            'Loaded Districts succesfully!'))

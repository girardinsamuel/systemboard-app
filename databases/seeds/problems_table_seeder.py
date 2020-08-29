"""Problems Table Seeder.

You can run this seeder in order to generate problems.
"""
import json
from os.path import join
from orator.seeds import Seeder

from config.application import BASE_DIRECTORY


class ProblemsTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        problems_file = join(
            BASE_DIRECTORY, "databases/seeds", "problems_tensionboard_08052020.json"
        )
        with open(problems_file) as json_file:
            data = json.load(json_file)
            for climb in data["PUT"]["climbs"]:
                if climb["hsm"] == 11:
                    self.db.table("problems").insert(
                        {
                            "title": climb["name"],
                            "placements": json.dumps(climb["placements"]),
                            "grade": "?",
                        }
                    )

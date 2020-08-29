"""Placements Table Seeder.

You can run this seeder in order to generate placements.
"""
import string
import json
from os.path import join
from orator.seeds import Seeder

from config.application import BASE_DIRECTORY


class PlacementsTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        problems_file = join(BASE_DIRECTORY, "databases/seeds", "holds_layouts.json")
        with open(problems_file) as json_file:
            data = json.load(json_file)
            # convert holes to list easily indexable
            holes = {}
            for hole in data["PUT"]["holes"]:
                holes[hole["id"]] = hole
            for placement in data["PUT"]["placements"]:
                # get hole data
                hole = holes[placement["hole_id"]]
                import pdb

                if "KB" in hole["name"]:
                    xx, yy = hole["name"].split(",")
                    if yy == "KB1":
                        y = 0
                    else:
                        y = "0.5"
                    if "." in xx:
                        letter, _ = xx.split(".")
                        x = f"{list(string.ascii_uppercase).index(letter) + 1}.5"
                    else:
                        x = f"{list(string.ascii_uppercase).index(xx) + 1}.5"
                elif "." in hole["name"]:
                    continue
                else:
                    x, y = hole["name"].split(",")
                    x = f"{list(string.ascii_uppercase).index(x) + 1}"
                self.db.table("placements").insert(
                    {
                        "id": placement["id"],
                        "hole_id": placement["hole_id"],
                        "hold_id": placement["hold_id"],
                        "mirrored_hole_id": hole["mirrored_hole_id"],
                        "coords": json.dumps({"x": x, "y": y}),
                        "rotation": placement["rotation"],
                        "position": hole["position"],
                        "mirrored_position": holes[hole["mirrored_hole_id"]][
                            "position"
                        ],
                    }
                )

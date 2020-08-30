"""A ProblemsController Module."""
import json
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse

try:
    import board
    import neopixel
except:
    print("not on a RPI, skipping importing board")

from app.Problem import Problem
from app.Placement import Placement


class ProblemsController(Controller):
    """ProblemsController Controller Class."""

    def __init__(self, request: Request):
        """ProblemsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request
        try:
            self.pixels = neopixel.NeoPixel(board.D18, 30)
        except:
            pass

    def show(self, view: InertiaResponse):
        problems = Problem.all().take(300)
        return view.render("Problems", {"problems": problems.serialize()})

    def single(self, view: InertiaResponse):
        problem = Problem.find(int(self.request.param("id")))
        # get placements
        placements_json = json.loads(problem.placements)
        placements_id = [p["placement_id"] for p in placements_json]
        placements = Placement.all().filter(lambda p: p.id in placements_id)
        problem_data = problem.serialize()
        problem_data["placements"] = json.loads(problem_data["placements"])
        for pl in problem_data["placements"]:
            try:
                pl["coords"] = json.loads(
                    placements.where("id", pl["placement_id"]).first().coords
                )

                #         "coords": placements.where("id", pl["placement_id"])
                #         .first()
                #         .coords,
                #     }
                # )

            except:
                pass
            # pl['placement'] = placements[]
        # replcae placement_id with the object but let role_id
        # problem["placements"] add here the role id in each placements ...
        return view.render(
            "Problem", {"title": "Problem detail", "problem": problem_data}
        )

    def single_details(self, view: InertiaResponse):

        return view.render(
            "ProblemDetail",
            {
                "details": {
                    "id": self.request.param("id"),
                    "title": "Problem",
                    "grade": "6b",
                    "setter": "Sam",
                }
            },
        )

    def toggle_light(self, view: InertiaResponse):
        problem = Problem.find(int(self.request.param("id")))
        # get placements
        placements = json.loads(problem.placements)
        placements_id = [p["placement_id"] for p in placements]
        placements = Placement.all().filter(lambda p: p.id in placements_id)

        print("Light : ", [placement.position for placement in placements])
        for pos in [placement.position for placement in placements]:
            self.pixels[pos] = (255, 255, 0)
        self.pixels.show()
        return view.render("Problem")

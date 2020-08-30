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


def get_color(role_id):
    if role_id == 1:
        return (0, 255, 0)
    elif role_id == 2:
        return (0, 0, 255)
    elif role_id == 3:
        return (255, 0, 0)
    else:
        return (248, 2, 252)


class ProblemsController(Controller):
    """ProblemsController Controller Class."""

    def __init__(self, request: Request):
        """ProblemsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request
        try:
            self.pixels = neopixel.NeoPixel(board.D18, 220, brightness=0.3)
        except:
            pass
        self.indexes = list(range(43)) + list([None]*18)
        for i in range(1, 11):
            self.indexes += list(range(25+i*18, 25+(i+1)*18)) + list([None]*18)
        
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
        should_light = self.request.input("light")
        try:
            self.pixels.fill((0, 0, 0))
        except:
            print("Error lighting ! or not on a RPI")
        if not should_light:
            return view.render("Problem")

        problem = Problem.find(int(self.request.param("id")))
        # get placements
        placements = json.loads(problem.placements)
        placements_id = [p["placement_id"] for p in placements]
        placements = Placement.all().filter(lambda p: p.id in placements_id)
        problem_placements = json.loads(problem.placements)
        print("Light : ", [placement.position for placement in placements])
        for index, placement in enumerate(placements.all()):
            role_id = problem_placements[index]["role_id"]
            color = get_color(role_id)
            try:
                real_position = self.indexes[placement.position]
                print(real_position, placement.position, color)
                if real_position:
                    self.pixels[real_position] = color
            except:
                pass
        self.pixels.show()
        return view.render("Problem")

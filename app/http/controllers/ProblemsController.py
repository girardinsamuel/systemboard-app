"""A ProblemsController Module."""
import json
import time
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse

try:
    from rpi_ws281x import Color, Adafruit_NeoPixel
except:
    print("not on a RPI, skipping importing board")

from app.Problem import Problem
from app.Placement import Placement


def get_color(role_id):
    if role_id == 1:
        return Color(255, 0, 0)
    elif role_id == 2:
        return Color(0, 0, 255)
    elif role_id == 3:
        return Color(0, 255, 0)
    else:
        return Color(2, 248, 252)


class ProblemsController(Controller):
    """ProblemsController Controller Class."""

    def __init__(self, request: Request):
        """ProblemsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request
        self.indexes = list(range(23))
        for i in range(0, 11):
            col = list(range(23 + i * 18, 23 + (i + 1) * 18))
            if i % 2 != 0:
                col.reverse()
            self.indexes += col + list([None] * 17)

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
            strip = Adafruit_NeoPixel(220, 18)
            strip.setBrightness(40)
            strip.begin()
        except:
            print("Error lighting ! or not on a RPI")
        if not should_light:
            try:
                strip.show()
            except:
                print("Error lighting ! or not on a RPI")
            return view.render("Problem")

        problem = Problem.find(int(self.request.param("id")))
        # get placements
        placements = json.loads(problem.placements)
        placements_id = [p["placement_id"] for p in placements]
        placements = Placement.all().filter(lambda p: p.id in placements_id)
        problem_placements = json.loads(problem.placements)
        #print("Light : ", [placement.position for placement in placements])
        for index, placement in enumerate(placements.all()):
            real_position = self.indexes[placement.mirrored_position]
            print(real_position, placement.position, placement.mirrored_position)
            if real_position is not None:
                role_id = problem_placements[index]["role_id"]
                color = get_color(role_id)
                print(role_id)
            try:
                #pixels[real_position - 1] = color
                strip.setPixelColor(real_position, color)
            except:
                print("not on a RPI OR light led error")
                pass
        strip.show()
        return view.render("Problem")

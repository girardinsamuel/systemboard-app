"""A SyncController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class SyncController(Controller):
    """SyncController Controller Class."""

    def __init__(self, request: Request):
        """SyncController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render("admin.sync")

    def sync(self, view: View):
        self.request.session.flash("success", "Problems synced !")
        return view.render("admin.sync")

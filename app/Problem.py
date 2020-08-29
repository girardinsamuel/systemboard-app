"""Problem Model."""

from config.database import Model


class Problem(Model):
    """Problem Model."""
    __table__ = "problems"
    __fillable__ = ["title", "grade", "placements"]
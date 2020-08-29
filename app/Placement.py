"""Placement Model."""

from config.database import Model


class Placement(Model):
    """Placement Model."""

    __table__ = "placements"
    __fillable__ = [
        "id",
        "hold_id",
        "hole_id",
        "mirrored_hole_id",
        "rotation",
        "position",
        "mirrored_position",
    ]

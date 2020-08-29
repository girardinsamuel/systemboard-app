from orator.migrations import Migration


class CreatePlacementsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("placements") as table:
            table.integer("id")
            table.primary("id")
            table.json("coords")
            table.integer("hold_id")
            table.integer("hole_id")
            table.integer("mirrored_hole_id")
            table.integer("position")
            table.integer("mirrored_position")
            table.integer("rotation")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("placements")

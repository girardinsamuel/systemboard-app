from orator.migrations import Migration


class CreateProblemsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('problems') as table:
            table.increments('id')
            table.string('title')
            table.string('grade')
            table.json('placements')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('problems')

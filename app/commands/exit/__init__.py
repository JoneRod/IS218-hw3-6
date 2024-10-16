import sys
import app.commands import Command

class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")
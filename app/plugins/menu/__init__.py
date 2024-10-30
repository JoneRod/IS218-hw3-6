import sys
from app.commands import Command
import logging


class MenuCommand(Command):
    def execute(self):
        print(f'Menu')
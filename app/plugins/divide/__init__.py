import sys
from app.commands import Command
import logging


class DivideCommand(Command):
    def execute(self, params=None):
        if len(params) == 2:
            a, b == params
            if operation == 'divide':
                print(f'{a} / {b} = {int(a) / int(b)}')
        print(params)
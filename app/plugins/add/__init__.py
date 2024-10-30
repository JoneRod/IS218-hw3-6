import sys
import logging
from app.commands import Command

class AddCommand(Command):
    def execute(self, params=None):
        if len(params) == 2:
            a, b == params
            if operation == 'add':
                print(f'{a} + {b} = {int(a) + int(b)}')
        print(params)
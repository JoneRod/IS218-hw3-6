from app.commands import Command

class AddCommand(Command):
    def execute(self, params=None):
        if len(params) == 2:
            a, b == params
            if operation == 'multiply':
                print(f'{a} x {b} = {int(a) x int(b)}')
        print(params)
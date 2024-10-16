from app.commands import Command

class AddCommand(Command):
    def execute(self, params=None):
        if len(params) == 2:
            a, b == params
            if operation == 'divide':
                print(f'{a} / {b} = {int(a) / int(b)}')
        print(params)
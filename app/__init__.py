import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_dir = 'app.commands'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_dir.replace('.', '/')]):
            if not is_pkg:
                try:
                    plugin_module = importlib.import_module(f'plugins.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                    
                        if isinstance(item, type) and issubclass(item, Command): 
                            self.command_handler.register_command(plugin_name, item())   
                except ImportError as e:
                    print(f"Error Importing plugin {plugin_name}: {e}")
                except Exception as e:
                    print(f"Error loading plugin {plugin_name}: {e}")

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input == 'exit':
                break
            self.command_handler.execute_command(user_input)

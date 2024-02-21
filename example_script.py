import importlib

print("Hello World!")
print("This script was called by the LLM agent and will run a Sudoku solver!")

def execute_python_file(file_path):
   try:
      module_name = file_path.replace('.py', '')
      module = importlib.import_module(module_name)
      module.main()
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")
   except ModuleNotFoundError:
      print(f"Error: The module '{module_name}' could not be found.")
   except ImportError as e:
      print(f"Error: Unable to import '{module_name}': {e}")

print("Running the Sudoku solver...")
execute_python_file('sudoku_solver.py')
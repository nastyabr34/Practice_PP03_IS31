import tkinter as tk
from ui import ImageConverterUI
import time
import sys
from memory_profiler import profile

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def run_app():
    root = tk.Tk()
    app = ImageConverterUI(root)
    root.mainloop()

if name == "__main__":
    run_app()
for module_name, module in sys.modules.items():
    if hasattr(module, '__file__'):
        print(f"{module_name}: {module.__file__}, Size: {os.path.getsize(module.__file__)} bytes")

import os
import sys


current_dir = os.path.abspath(__file__)

# backend_dir = os.path.normpath(os.path.join(current_dir, "../../backend"))
# if backend_dir not in sys.path:
#     sys.path.insert(0, backend_dir)


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

common_dir = os.path.normpath(os.path.join(current_dir, "common"))
if common_dir not in sys.path:
    sys.path.insert(0, common_dir)

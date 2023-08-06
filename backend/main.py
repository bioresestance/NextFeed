"""
@brief This file is the entry point for the backend server.
@details This file is the entry point for the backend server. 
         It is responsible for creating the web server and running it.
@file main.py
"""

import os
import sys
import logging
import threading
import uvicorn


# Update the path before importing the rest of the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from api import get_web_server
from database import initialize as initialize_database, uninitialize as uninitialize_database
from app.app import app_main


logging.basicConfig(level=logging.INFO, format="%(levelname)s (%(name)s) : %(message)s")
web_server = get_web_server(starting_event=initialize_database, stopping_event=uninitialize_database)


if __name__ == "__main__":
    thread_stop = threading.Event()
    thread = threading.Thread(target=app_main, args=(thread_stop,))
    thread.start()
    uvicorn.run("main:web_server", reload=True, host="0.0.0.0", port=8000)
    thread_stop.set()
    thread.join()

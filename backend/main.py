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
import time
import uvicorn

# Update the path before importing the rest of the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from server import get_web_server
from database import initialize as initialize_database, uninitialize as uninitialize_database

logging.basicConfig(level=logging.INFO, format="%(levelname)s (%(name)s) : %(message)s")
web_server = get_web_server(starting_event=initialize_database, stopping_event=uninitialize_database)

thread_stop = False

def update_feed():
    logging.info("Starting feed update thread")
    while not thread_stop:

        time.sleep(1)
    
    logging.info("Stopping feed update thread")


if __name__ == "__main__":
    thread = threading.Thread(target=update_feed)
    thread.start()
    uvicorn.run("main:web_server", reload=True)
    thread_stop = True
    thread.join()

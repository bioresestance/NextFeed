"""
@brief This file is the entry point for the backend server.
@details This file is the entry point for the backend server. 
         It is responsible for creating the web server and running it.
@file main.py
"""

# Python voodoo to make imports work for the backend module.
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import uvicorn
from server import get_web_server
import feed_parser
import logging
import threading
import time

from database import initialize as initialize_database

logging.basicConfig(level=logging.INFO, format="%(levelname)s (%(name)s) : %(message)s")
web_server = get_web_server(starting_event=initialize_database)

thread_stop = False

def update_feed():
    logging.info("Starting feed update thread")
    while thread_stop == False:

        time.sleep(1)
    
    logging.info("Stopping feed update thread")


if __name__ == "__main__":
    thread = threading.Thread(target=update_feed)
    thread.start()
    uvicorn.run("main:web_server", reload=True)
    thread_stop = True
    thread.join()

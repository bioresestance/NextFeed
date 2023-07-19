"""
@brief This file is the entry point for the backend server.
@details This file is the entry point for the backend server. 
         It is responsible for creating the web server and running it.
@file main.py
"""

import uvicorn
from server import get_web_server


web_server = get_web_server()

if __name__ == "__main__":
    uvicorn.run("main:web_server", reload=True)

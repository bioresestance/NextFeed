"""
@brief This file is the entry point for the backend server.
@details This file is the entry point for the backend server. 
         It is responsible for creating the web server and running it.
@file main.py
"""

from server import get_web_server


web_server = get_web_server()
print("Web Server Created")

web_server.run(debug=True)

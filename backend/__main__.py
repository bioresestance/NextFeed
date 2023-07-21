"""
@brief This file is the entry point for the backend server.
@details This file is the entry point for the backend server. 
         It is responsible for creating the web server and running it.
@file __main__.py
"""

from server import get_web_server


web_server = get_web_server()



if __name__ == "__main__":
    web_server.run(use_reloader=True, host="0.0.0.0", debug=True)

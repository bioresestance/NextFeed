from Server import get_web_server


web_server = get_web_server()



if __name__ == "__main__":
    web_server.run(use_reloader=False, host="0.0.0.0", debug=True)
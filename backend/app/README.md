# NextFeed App

This is a seperate application that runs in parrellel to the web API. It is responsible for various tasks, such as updating feeds that users are subscribed to, cleaning up old posts, etc.

For Dev work, both the App and the API are run from main.py, but in prod, each will be a seperate docker container(s)

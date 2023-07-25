# Feed Parser

This module is designed to be ran in a separate thread from the REST API webserver. Feed Parser will be responsible for reading in new RSS (and other types) feeds and properly storing them in the DB. It is designed to not run continuously, but instead, run on a schedule to collect, parse, filter and store the results.

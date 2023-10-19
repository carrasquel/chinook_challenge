#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from wsgiref.simple_server import make_server

from app import create_app

if __name__ == "__main__":
    app = create_app()

    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()

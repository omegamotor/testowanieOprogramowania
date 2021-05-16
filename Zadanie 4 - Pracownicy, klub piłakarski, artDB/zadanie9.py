import unittest
import requests
import json


def gl_url():
    return 'https://reqres.in'

def test_valid_login():
    url = gl_url() + "/api/login/"
    email = "eve.holt@reqres.in"
    password = "cityslicka"
    token = "QpwL5tke4Pnpja7X4"



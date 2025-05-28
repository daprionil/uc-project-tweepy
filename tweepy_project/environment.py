from os import getenv

environment = {"bearer_token": getenv("BEARER_TOKEN", "")}

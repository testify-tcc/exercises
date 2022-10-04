import os

CLIENT_DEV_ENDPOINT = "http://localhost:8080"
CLIENT_PROD_ENDPOINT = "http://testify.surge.sh"
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
SECTIONS_PATH = f"{ROOT_PATH}/definitions/sections"
EXERCISES_PATH = f"{ROOT_PATH}/definitions/exercises"
EXERCISES_JSON_FILE_PATH = f"{ROOT_PATH}/exercises.json"

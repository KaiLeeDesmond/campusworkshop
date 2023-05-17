"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7ofbhp8u7g2eeg5g0-a.oregon-postgres.render.com",
        database="todo_s55f",
        user="ogkrishna",
        password="c90Iqzzo2rWm5XJ0Hr8k7zJkSvL6WPf5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

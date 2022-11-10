import os
import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
from dotenv import dotenv_values

TOKEN = "c0lbzahp_nyDCF3QJLWYAjAowXfMajByEPMjwP3ay"

# Initialize with a project key
deta = Deta(TOKEN)

# This is how to create/connect a database
db = deta.Base("imagesdata")

def insert_period(add_name, gender, age, user_time):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": add_name, "gender": gender, "age": age, "datetime": user_time})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)
import os
import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
from dotenv import dotenv_values

temp = dotenv_values(".env")

TOKEN = temp["DETA_KEY"] 

# Initialize with a project key
deta = Deta(TOKEN)

# This is how to create/connect a database
db = deta.Base("imagesdata")


def insert_imagesdata(add_name, gender, age, user_time):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": add_name, "gender": gender, "age": age, "datetime": user_time})


def fetch_all_imagesdata():
    """Returns a dict of all imagesdata"""
    res = db.fetch()
    return res.items


def get_imagesdata(imagesdata):
    """If not found, the function will return None"""
    return db.get(imagesdata)

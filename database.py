import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = "c0lbzahp_nyDCF3QJLWYAjAowXfMajByEPMjwP3ay"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("imagesdata")


def insert_period(idate, iname):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"ID": idate, "imagename": iname})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

idate = "2022-11-10"
iname = "image_test"

insert_period(idate,iname)
fetch_all_periods()
get_period("2002-11-10")

#!/usr/bin/python3
""" Creates class Review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines class City """

    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""Defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Sets the name of an amenity.

    Attributes:
        name(str): Name of the amenity.
    """

    name = ""

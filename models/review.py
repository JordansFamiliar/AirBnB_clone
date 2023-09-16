#!/usr/bin/python3
"""Definition of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review"""

    user_id = ""
    text = ""
    place_id = ""

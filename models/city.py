#!/usr/bin/python3
"""Definition of the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city.

    Attributes:
        state_id(str): State id.
        name(str): Name of the city.
    """

    state_id = ""
    name = ""

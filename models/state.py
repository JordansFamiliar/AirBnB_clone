#!/usr/bin/python3
"""Definition of the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a state

    Attributes:
        name(str): Name of the state.
    """

    name = ""

#!/usr/bin/python3
"""State Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the Review model"""
    place_id = ""
    user_id = ""
    text = ""

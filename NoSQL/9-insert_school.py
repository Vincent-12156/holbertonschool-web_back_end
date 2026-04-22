#!/usr/bin/env python3
"""
Module that provides a function to insert a document in a collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

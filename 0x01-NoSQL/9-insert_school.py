#!/usr/bin/env python3
"""
A function that inserts a new document in a collectionn based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Returns the _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

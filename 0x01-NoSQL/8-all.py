#!/usr/bin/env python3
"""
Function to list all documents in a collection in MongoDB
"""


def list_all(mongo_collection):
    """
    Returns a list of all documents in a collection or an empty list if none
    """
    docs_list = list(mongo_collection.find())

    if len(docs_list) is None:
        return []
    return docs_list

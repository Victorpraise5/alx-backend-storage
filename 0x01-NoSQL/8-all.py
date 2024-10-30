#!/usr/bin/env python3

def list_all(mongo_collection):
    """
    lists all documents in a given MongoDB collection

    Returns:
    -A lis of all documents in the collection, or an empty list if no document is found
    """
    doc_list = list(mongo_collection.find())

    if len(doc_list) is None:
        return []
    return doc_list

import pymongo

def list_all(mongo_collection):
    """
    lists all documents in a given MongoDB collection

    Returns:
    -A lis of all documents in the collection, or an empty list if no document is found
    """
    return list(mongo_collection.find())

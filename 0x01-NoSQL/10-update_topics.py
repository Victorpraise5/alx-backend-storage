#!/usr/bin/env python3
"""
A function that changes all topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Returns: none
    """
       name_to_update = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(name_to_update, new_topics)

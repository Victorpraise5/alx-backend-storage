#!/usr/bin/env python3
"""
A function that returns the list of school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns: List of school having a specific topic
    """
    result = list(mongo_collection.find({"topics": {"$in": [topic]}}))
    return result

#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

#connecting to the MongoDB client
client = MongoClient("mongodb://localhost:27017/")

#Accessing the logs db and nginx collection
db = client["logs"]
nginx_collection = db["nginx"]


def nginx_stats():
    """
    Prints statistics about nginx logs stored in MongoDB
    """

    #counting the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    #counting the logs for each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    #count logs with metho=GET and path=/status
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

#execute function
if __name__ == "__main__":
    nginx_stats()

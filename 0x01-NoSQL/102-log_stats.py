#!/usr/bin/env python3
"""
improve log_stats by adding the top 10 of the most present IPs
"""

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["logs"]
nginx_collection = db["nginx"]

def nginx_stats():
    """
    Print statistics about Nginx logs stored in MongoDB, includein the top 10 IPs
    """

    #counting the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    #count the logs for each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    #counting logs
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    #dinf the top 10 most frequent IPs
    print("IPs:")
    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
            ]

    #executing the aggregation pipeline
    top_ips = nginx_collection.aggregate(pipeline)

    #print each ip and its count
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    nginx_stats()

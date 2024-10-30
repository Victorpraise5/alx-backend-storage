#!/usr/bin/env python3
"""
improve log_stats by adding the top 10 of the most present IPs
"""

from pymongo import MongoClient


def main():
    """
    Print statistics about Nginx logs stored in MongoDB, includein the top 10 IPs
    """
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx

    total = nginx.count_documents({})
    print("{} logs".format(total))

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    ips = list(nginx.aggregate(pipeline))
    print("IPs:")
    for ip in ips:
        print("\t{}: {}"
              .format(ip.get('_id'), ip.get('count')))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Module for updating school topics in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Change all topics of school documents matching a given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

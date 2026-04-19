#!/usr/bin/env python3
"""Module for inserting a document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document and return its _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

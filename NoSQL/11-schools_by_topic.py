#!/usr/bin/env python3
"""Module for retrieving schools by topic from MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools that have a specific topic."""
    return list(mongo_collection.find({"topics": topic}))

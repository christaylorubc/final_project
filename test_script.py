#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 5, 2024

@author: Chris Taylor

This function creates a helper data to test the script created for 
the solution to the Python Programming for Data Science project.
"""

from script import group_stats
import pandas as pd


def test_group_stats():

    raw = {
        "movie_title": ["Saw", "Saw II", "Saw III", "Saw IV"],
        "genre": ["Horror", "Horror", "Horror", "Horror"],
        "gross": [300, 250, 100, 150],
    }

    helper_data = pd.DataFrame.from_dict(raw)

    res = group_stats(helper_data, "genre", "gross")

    assert res.shape == (1, 4)
    assert "genre" in res.columns
    assert "sum" in res.columns
    assert "mean" in res.columns
    assert "count" in res.columns
    assert res["sum"].item() == 800
    assert res["mean"].item() == 200
    assert res["count"].item() == 4

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 5, 2024

@author: Chris Taylor

"""


def group_stats(data, grouping_col, stats_col, stats=["sum", "mean", "count"]):
    import pandas as pd

    """
    Given a dataframe, a column and an action, return a dataframe that has been
    grouped by the column and a aggregate function applied.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    grouping_col : str
        The column to group the data on
    stats_col : str
        After grouping, the column to calculate stats for
    stats : list, optional
        The stats to calculate on specified stats_col. By default sum, mean,  
        and count are calculated.      
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and columns for each stat.
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    TypeError
        If the input argument stats is not of type list
    AssertError
        If the input argument grouping_col is not in the data columns
    AssertError
        If the input argument action_col is not in the data columns
    
    Examples
    --------
    >>> group_stats(helper_data, 'tree_type', 'tree_count', ['sum', 'mean', 'count'])
    tree_type   sum     mean    count
    Cherry      40      4       10
    Oak         20      5       4

    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    if not isinstance(stats, list):
        raise TypeError("The stats argument is not of type list")

    assert (
        grouping_col in data.columns
    ), "The grouping column does not exist in the dataframe"
    assert stats_col in data.columns, "The stats column does not exist in the dataframe"

    stats_df = data.groupby(grouping_col).agg({stats_col: stats}).loc[:, stats_col]

    # Convert all stats columns to int for easier analysis
    for column in stats:
        stats_df[column] = stats_df[column].astype(int)

    stats_df = pd.DataFrame(stats_df)
    stats_df = stats_df.reset_index()
    return stats_df

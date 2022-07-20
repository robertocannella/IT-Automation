#!/usr/bin/env python3

# This module to hold queries for car sales

import pandas as pd

def get_total_revenue(df):
    return df.sort_values(by=['total_revenue'], ascending=False)

def get_top_revenue(df, number):
    report = df.sort_values(by=['total_revenue'], ascending=False)[:number]
    return report

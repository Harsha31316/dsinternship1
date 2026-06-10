"""
Data Cleaning & Visualization Project
A comprehensive Python project for data preprocessing, analysis, and visualization
"""

__version__ = "1.0.0"
__author__ = "Data Science Lab"

from .data_loader import load_data, inspect_data, print_inspection
from .data_cleaner import DataCleaner, clean_sales_data
from .visualizer import *

__all__ = [
    'load_data',
    'inspect_data',
    'print_inspection',
    'DataCleaner',
    'clean_sales_data',
    'plot_missing_data_heatmap',
    'plot_missing_value_percentages',
    'plot_numeric_distributions',
    'plot_boxplots',
    'plot_sales_trends',
    'plot_category_analysis',
    'plot_region_analysis',
    'plot_correlation_heatmap',
    'create_summary_dashboard',
]

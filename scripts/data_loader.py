"""
Data Loading Module
Handles loading and initial inspection of datasets
"""

import pandas as pd
import os


def load_data(filepath):
    """
    Load CSV data from file
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataset
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    df = pd.read_csv(filepath)
    return df


def inspect_data(df):
    """
    Provide initial data inspection and summary statistics
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset to inspect
        
    Returns:
    --------
    dict
        Dictionary containing inspection results
    """
    inspection = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'missing_percentage': (df.isnull().sum() / len(df) * 100).round(2).to_dict(),
        'duplicates': df.duplicated().sum(),
        'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # in MB
    }
    return inspection


def print_inspection(inspection):
    """
    Print formatted data inspection results
    """
    print("=" * 60)
    print("DATA INSPECTION REPORT")
    print("=" * 60)
    print(f"\nDataset Shape: {inspection['shape'][0]} rows × {inspection['shape'][1]} columns")
    print(f"Memory Usage: {inspection['memory_usage']:.2f} MB")
    print(f"Duplicate Rows: {inspection['duplicates']}")
    
    print("\n--- Missing Values ---")
    for col, count in inspection['missing_values'].items():
        pct = inspection['missing_percentage'][col]
        print(f"  {col}: {count} ({pct}%)")
    
    print("\n--- Data Types ---")
    for col, dtype in inspection['dtypes'].items():
        print(f"  {col}: {dtype}")

"""
Data Cleaning Module
Handles missing values, outliers, duplicates, and data type conversions
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


class DataCleaner:
    """Main data cleaning class"""
    
    def __init__(self, df):
        """
        Initialize cleaner with dataframe
        
        Parameters:
        -----------
        df : pd.DataFrame
            The dataset to clean
        """
        self.df = df.copy()
        self.cleaning_log = []
    
    def remove_duplicates(self, subset=None, keep='first'):
        """
        Remove duplicate rows
        
        Parameters:
        -----------
        subset : list, optional
            Column names to consider for duplicates
        keep : str
            Which duplicates to keep ('first', 'last', False)
        """
        initial_rows = len(self.df)
        self.df = self.df.drop_duplicates(subset=subset, keep=keep)
        removed = initial_rows - len(self.df)
        self.cleaning_log.append(f"Removed {removed} duplicate rows")
        return self
    
    def handle_missing_numeric(self, columns=None, method='mean'):
        """
        Handle missing values in numeric columns
        
        Parameters:
        -----------
        columns : list, optional
            Columns to fill. If None, processes all numeric columns
        method : str
            'mean', 'median', 'forward_fill', or 'drop'
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        for col in columns:
            if self.df[col].isnull().any():
                if method == 'mean':
                    fill_value = self.df[col].mean()
                    self.df[col].fillna(fill_value, inplace=True)
                elif method == 'median':
                    fill_value = self.df[col].median()
                    self.df[col].fillna(fill_value, inplace=True)
                elif method == 'forward_fill':
                    self.df[col].fillna(method='ffill', inplace=True)
                elif method == 'drop':
                    self.df.dropna(subset=[col], inplace=True)
                
                self.cleaning_log.append(f"Filled missing values in '{col}' using {method}")
        
        return self
    
    def handle_missing_categorical(self, columns=None, method='mode'):
        """
        Handle missing values in categorical columns
        
        Parameters:
        -----------
        columns : list, optional
            Columns to fill
        method : str
            'mode' or 'drop'
        """
        if columns is None:
            columns = self.df.select_dtypes(include=['object']).columns
        
        for col in columns:
            if self.df[col].isnull().any():
                if method == 'mode':
                    fill_value = self.df[col].mode()[0]
                    self.df[col].fillna(fill_value, inplace=True)
                elif method == 'drop':
                    self.df.dropna(subset=[col], inplace=True)
                
                self.cleaning_log.append(f"Filled missing values in '{col}' using {method}")
        
        return self
    
    def remove_outliers(self, columns=None, method='iqr', threshold=1.5):
        """
        Remove outliers from numeric columns
        
        Parameters:
        -----------
        columns : list, optional
            Columns to check for outliers
        method : str
            'iqr' (Interquartile Range) or 'zscore'
        threshold : float
            Threshold for outlier detection
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        initial_rows = len(self.df)
        
        for col in columns:
            if method == 'iqr':
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
                
            elif method == 'zscore':
                z_scores = np.abs((self.df[col] - self.df[col].mean()) / self.df[col].std())
                self.df = self.df[z_scores < threshold]
        
        removed = initial_rows - len(self.df)
        if removed > 0:
            self.cleaning_log.append(f"Removed {removed} outlier rows using {method}")
        
        return self
    
    def convert_data_types(self, type_dict):
        """
        Convert column data types
        
        Parameters:
        -----------
        type_dict : dict
            Dictionary mapping column names to desired data types
        """
        for col, dtype in type_dict.items():
            if col in self.df.columns:
                try:
                    self.df[col] = self.df[col].astype(dtype)
                    self.cleaning_log.append(f"Converted '{col}' to {dtype}")
                except Exception as e:
                    self.cleaning_log.append(f"Failed to convert '{col}' to {dtype}: {str(e)}")
        
        return self
    
    def fix_revenue_values(self):
        """
        Fix revenue column by calculating from Quantity * Price when missing
        """
        # Calculate missing Revenue values
        missing_revenue = self.df['Revenue'].isnull()
        if missing_revenue.any():
            self.df.loc[missing_revenue, 'Revenue'] = \
                self.df.loc[missing_revenue, 'Quantity'] * self.df.loc[missing_revenue, 'Price']
            self.cleaning_log.append(f"Calculated {missing_revenue.sum()} missing Revenue values")
        
        return self
    
    def get_log(self):
        """Return cleaning operation log"""
        return self.cleaning_log
    
    def get_cleaned_data(self):
        """Return cleaned dataframe"""
        return self.df


def clean_sales_data(df):
    """
    Complete cleaning pipeline for sales data
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw sales data
        
    Returns:
    --------
    pd.DataFrame, list
        Cleaned dataframe and cleaning log
    """
    cleaner = DataCleaner(df)
    
    # Step 1: Remove duplicates
    cleaner.remove_duplicates(subset=['Date', 'Product', 'Customer_ID', 'Quantity'])
    
    # Step 2: Handle missing values
    cleaner.handle_missing_numeric(columns=['Quantity', 'Price'], method='mean')
    cleaner.handle_missing_categorical(columns=['Status'], method='mode')
    
    # Step 3: Fix revenue calculations
    cleaner.fix_revenue_values()
    
    # Step 4: Convert data types
    type_conversions = {
        'Date': 'datetime64[ns]',
        'Quantity': 'int32',
        'Price': 'float32',
        'Revenue': 'float32'
    }
    cleaner.convert_data_types(type_conversions)
    
    # Step 5: Remove outliers (excessive quantities)
    cleaner.remove_outliers(columns=['Quantity', 'Price'], method='iqr', threshold=1.5)
    
    return cleaner.get_cleaned_data(), cleaner.get_log()

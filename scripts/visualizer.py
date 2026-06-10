"""
Visualization Module
Creates various plots and visualizations for data analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
import os


# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10


def plot_missing_data_heatmap(df, figsize=(12, 6)):
    """
    Create a heatmap showing missing data patterns
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset
    figsize : tuple
        Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create missing data visualization
    missing = df.isnull()
    sns.heatmap(missing, cbar=True, yticklabels=False, cmap='viridis', ax=ax)
    
    ax.set_title('Missing Data Pattern', fontsize=14, fontweight='bold')
    ax.set_xlabel('Columns')
    
    return fig


def plot_missing_value_percentages(df, figsize=(10, 6)):
    """
    Create bar plot of missing value percentages
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset
    figsize : tuple
        Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    missing_pct = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
    missing_pct = missing_pct[missing_pct > 0]
    
    if len(missing_pct) > 0:
        missing_pct.plot(kind='barh', ax=ax, color='coral')
        ax.set_xlabel('Percentage Missing (%)', fontsize=11)
        ax.set_title('Missing Values by Column', fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'No missing values', ha='center', va='center', fontsize=12)
        ax.set_title('Missing Values by Column', fontsize=14, fontweight='bold')
    
    return fig


def plot_numeric_distributions(df, figsize=(14, 10)):
    """
    Create distribution plots for all numeric columns
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset
    figsize : tuple
        Figure size
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    n_cols = len(numeric_cols)
    
    if n_cols == 0:
        return None
    
    n_rows = (n_cols + 2) // 3
    fig, axes = plt.subplots(n_rows, 3, figsize=figsize)
    axes = axes.flatten()
    
    for idx, col in enumerate(numeric_cols):
        axes[idx].hist(df[col], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'Distribution: {col}', fontweight='bold')
        axes[idx].set_xlabel(col)
        axes[idx].set_ylabel('Frequency')
        axes[idx].grid(alpha=0.3)
    
    # Hide empty subplots
    for idx in range(len(numeric_cols), len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    return fig


def plot_boxplots(df, figsize=(14, 6)):
    """
    Create boxplots for numeric columns to detect outliers
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset
    figsize : tuple
        Figure size
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    n_cols = len(numeric_cols)
    
    if n_cols == 0:
        return None
    
    fig, axes = plt.subplots(1, n_cols, figsize=figsize)
    
    if n_cols == 1:
        axes = [axes]
    
    for idx, col in enumerate(numeric_cols):
        axes[idx].boxplot(df[col].dropna(), vert=True)
        axes[idx].set_title(f'Boxplot: {col}', fontweight='bold')
        axes[idx].set_ylabel(col)
        axes[idx].grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_sales_trends(df, figsize=(14, 6)):
    """
    Create time series plot of sales trends
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset (must contain 'Date' and 'Revenue')
    figsize : tuple
        Figure size
    """
    if 'Date' not in df.columns or 'Revenue' not in df.columns:
        return None
    
    # Convert to datetime if needed
    if df['Date'].dtype != 'datetime64[ns]':
        df = df.copy()
        df['Date'] = pd.to_datetime(df['Date'])
    
    daily_revenue = df.groupby('Date')['Revenue'].sum().sort_index()
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(daily_revenue.index, daily_revenue.values, marker='o', 
            linewidth=2, markersize=6, color='#2E86AB')
    ax.set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Revenue ($)')
    ax.grid(alpha=0.3)
    fig.autofmt_xdate()
    
    return fig


def plot_category_analysis(df, figsize=(14, 6)):
    """
    Create subplots for category-wise analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset (must contain 'Category')
    figsize : tuple
        Figure size
    """
    if 'Category' not in df.columns:
        return None
    
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Revenue by category
    category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
    category_revenue.plot(kind='bar', ax=axes[0], color='#A23B72')
    axes[0].set_title('Total Revenue by Category', fontweight='bold')
    axes[0].set_xlabel('Category')
    axes[0].set_ylabel('Revenue ($)')
    axes[0].tick_params(axis='x', rotation=45)
    axes[0].grid(alpha=0.3, axis='y')
    
    # Quantity by category
    category_qty = df.groupby('Category')['Quantity'].sum().sort_values(ascending=False)
    category_qty.plot(kind='bar', ax=axes[1], color='#F18F01')
    axes[1].set_title('Total Quantity by Category', fontweight='bold')
    axes[1].set_xlabel('Category')
    axes[1].set_ylabel('Quantity')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig


def plot_region_analysis(df, figsize=(14, 6)):
    """
    Create subplots for region-wise analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset (must contain 'Region')
    figsize : tuple
        Figure size
    """
    if 'Region' not in df.columns:
        return None
    
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Revenue by region
    region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
    region_revenue.plot(kind='bar', ax=axes[0], color='#06A77D')
    axes[0].set_title('Total Revenue by Region', fontweight='bold')
    axes[0].set_xlabel('Region')
    axes[0].set_ylabel('Revenue ($)')
    axes[0].tick_params(axis='x', rotation=45)
    axes[0].grid(alpha=0.3, axis='y')
    
    # Number of transactions by region
    region_count = df.groupby('Region').size().sort_values(ascending=False)
    region_count.plot(kind='bar', ax=axes[1], color='#D62828')
    axes[1].set_title('Transaction Count by Region', fontweight='bold')
    axes[1].set_xlabel('Region')
    axes[1].set_ylabel('Count')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig


def plot_correlation_heatmap(df, figsize=(10, 8)):
    """
    Create correlation heatmap for numeric columns
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataset
    figsize : tuple
        Figure size
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.shape[1] < 2:
        return None
    
    fig, ax = plt.subplots(figsize=figsize)
    correlation = numeric_df.corr()
    
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, 
                fmt='.2f', square=True, ax=ax, cbar_kws={'label': 'Correlation'})
    ax.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
    
    return fig


def save_figure(fig, filepath):
    """
    Save figure to file
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to save
    filepath : str
        Path to save the figure
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Saved: {filepath}")


def create_summary_dashboard(df_before, df_after, output_dir='output'):
    """
    Create a comprehensive summary dashboard comparing before/after cleaning
    
    Parameters:
    -----------
    df_before : pd.DataFrame
        Raw data
    df_after : pd.DataFrame
        Cleaned data
    output_dir : str
        Directory to save outputs
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Create summary statistics
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Before/After record counts
    axes[0, 0].bar(['Before', 'After'], [len(df_before), len(df_after)], color=['#FF6B6B', '#51CF66'])
    axes[0, 0].set_title('Record Count: Before vs After', fontweight='bold')
    axes[0, 0].set_ylabel('Number of Records')
    axes[0, 0].grid(alpha=0.3, axis='y')
    
    # Missing values comparison
    before_missing = df_before.isnull().sum().sum()
    after_missing = df_after.isnull().sum().sum()
    axes[0, 1].bar(['Before', 'After'], [before_missing, after_missing], color=['#FF6B6B', '#51CF66'])
    axes[0, 1].set_title('Total Missing Values: Before vs After', fontweight='bold')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].grid(alpha=0.3, axis='y')
    
    # Data quality score
    before_quality = 100 * (1 - before_missing / (df_before.shape[0] * df_before.shape[1]))
    after_quality = 100 * (1 - after_missing / (df_after.shape[0] * df_after.shape[1]))
    axes[1, 0].bar(['Before', 'After'], [before_quality, after_quality], color=['#FF6B6B', '#51CF66'])
    axes[1, 0].set_title('Data Quality Score', fontweight='bold')
    axes[1, 0].set_ylabel('Quality %')
    axes[1, 0].set_ylim([0, 105])
    axes[1, 0].grid(alpha=0.3, axis='y')
    for i, v in enumerate([before_quality, after_quality]):
        axes[1, 0].text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')
    
    # Duplicates removed
    duplicates_before = df_before.duplicated().sum()
    axes[1, 1].bar(['Duplicates Before', 'Duplicates After'], 
                   [duplicates_before, 0], color=['#FF6B6B', '#51CF66'])
    axes[1, 1].set_title('Duplicate Records', fontweight='bold')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    save_figure(fig, os.path.join(output_dir, 'data_cleaning_summary.png'))
    plt.close()

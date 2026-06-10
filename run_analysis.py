"""
Example script demonstrating how to use the data cleaning & visualization modules
Run this to process the raw data and generate visualizations
"""

import sys
import os
sys.path.insert(0, './scripts')

from data_loader import load_data, inspect_data, print_inspection
from data_cleaner import clean_sales_data
from visualizer import (
    plot_missing_data_heatmap,
    plot_missing_value_percentages,
    plot_numeric_distributions,
    plot_boxplots,
    plot_sales_trends,
    plot_category_analysis,
    plot_region_analysis,
    plot_correlation_heatmap,
    create_summary_dashboard,
    save_figure
)
import matplotlib.pyplot as plt


def main():
    """Main execution function"""
    
    print("\n" + "="*70)
    print("DATA CLEANING & VISUALIZATION PROJECT - EXAMPLE SCRIPT")
    print("="*70)
    
    # Step 1: Load and inspect data
    print("\n[STEP 1] Loading raw data...")
    df_raw = load_data('./data/raw_sales_data.csv')
    print(f"✓ Loaded {df_raw.shape[0]} records with {df_raw.shape[1]} columns")
    
    # Step 2: Inspect data
    print("\n[STEP 2] Inspecting data structure...")
    inspection = inspect_data(df_raw)
    print_inspection(inspection)
    
    # Step 3: Clean data
    print("\n[STEP 3] Cleaning data...")
    df_clean, log = clean_sales_data(df_raw)
    print(f"✓ Cleaned dataset has {df_clean.shape[0]} records")
    print("Cleaning operations:")
    for operation in log:
        print(f"  • {operation}")
    
    # Step 4: Generate visualizations
    print("\n[STEP 4] Generating visualizations...")
    os.makedirs('./output', exist_ok=True)
    
    # Save individual visualizations
    visualizations = [
        ("Missing Data Heatmap", plot_missing_data_heatmap(df_raw), 'missing_heatmap.png'),
        ("Missing Values (%)", plot_missing_value_percentages(df_raw), 'missing_percentage.png'),
        ("Numeric Distributions", plot_numeric_distributions(df_clean), 'distributions.png'),
        ("Boxplots (Outliers)", plot_boxplots(df_clean), 'boxplots.png'),
        ("Sales Trends", plot_sales_trends(df_clean), 'sales_trends.png'),
        ("Category Analysis", plot_category_analysis(df_clean), 'category_analysis.png'),
        ("Region Analysis", plot_region_analysis(df_clean), 'region_analysis.png'),
        ("Correlation Matrix", plot_correlation_heatmap(df_clean), 'correlation_heatmap.png'),
    ]
    
    for name, fig, filename in visualizations:
        if fig is not None:
            save_figure(fig, f'./output/{filename}')
            print(f"  ✓ {name}")
            plt.close(fig)
    
    # Step 5: Create summary dashboard
    print("\n[STEP 5] Creating summary dashboard...")
    create_summary_dashboard(df_raw, df_clean, './output')
    print("  ✓ Dashboard created")
    
    # Step 6: Save cleaned data
    print("\n[STEP 6] Saving cleaned data...")
    output_path = './data/processed_sales_data.csv'
    df_clean.to_csv(output_path, index=False)
    print(f"  ✓ Saved to {output_path}")
    
    # Step 7: Generate summary report
    print("\n[STEP 7] Generating summary report...")
    summary = f"""
DATA CLEANING SUMMARY REPORT
{'='*70}

DATASET STATISTICS:
  Before Cleaning:
    - Records: {len(df_raw)}
    - Missing Values: {df_raw.isnull().sum().sum()}
    - Duplicates: {df_raw.duplicated().sum()}
    - Quality Score: {100 * (1 - df_raw.isnull().sum().sum() / (df_raw.shape[0] * df_raw.shape[1])):.2f}%
  
  After Cleaning:
    - Records: {len(df_clean)}
    - Missing Values: {df_clean.isnull().sum().sum()}
    - Duplicates: {df_clean.duplicated().sum()}
    - Quality Score: {100 * (1 - df_clean.isnull().sum().sum() / (df_clean.shape[0] * df_clean.shape[1])):.2f}%

BUSINESS METRICS:
  - Total Revenue: ${df_clean['Revenue'].sum():,.2f}
  - Average Order Value: ${df_clean['Revenue'].mean():,.2f}
  - Total Units Sold: {df_clean['Quantity'].sum():,}
  - Unique Customers: {df_clean['Customer_ID'].nunique()}
  - Date Range: {df_clean['Date'].min()} to {df_clean['Date'].max()}

TOP PRODUCTS:
  {df_clean.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head()}

TOP REGIONS:
  {df_clean.groupby('Region')['Revenue'].sum().sort_values(ascending=False).head()}

ORDER STATUS:
  {df_clean['Status'].value_counts()}

GENERATED FILES:
  - Cleaned data: ./data/processed_sales_data.csv
  - Dashboard: ./output/data_cleaning_summary.png
  - Visualizations: ./output/*.png
  - Report: ./output/summary_report.txt
{'='*70}
"""
    print(summary)
    
    # Save report
    with open('./output/execution_report.txt', 'w') as f:
        f.write(summary)
    
    print("\n✓ PROJECT COMPLETED SUCCESSFULLY!")
    print(f"All outputs saved to: ./output/")
    print("="*70 + "\n")


if __name__ == '__main__':
    main()

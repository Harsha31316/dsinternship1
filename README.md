# Data Cleaning & Visualization Project

A comprehensive project demonstrating data preprocessing, analysis, and visualization techniques using Python.

## Project Structure

```
├── data/
│   ├── raw_sales_data.csv          # Raw dataset with issues
│   └── processed_sales_data.csv    # Cleaned dataset
├── notebooks/
│   └── data_analysis.ipynb         # Main analysis notebook
├── scripts/
│   ├── data_loader.py              # Load data
│   ├── data_cleaner.py             # Cleaning functions
│   └── visualizer.py               # Visualization functions
├── output/
│   └── reports/                    # Generated reports and charts
├── requirements.txt                # Python dependencies
└── README.md                        # This file
```

## Key Learning Outcomes

- **Data Cleaning**: Handle missing values, outliers, and duplicates
- **Data Processing**: Transform and prepare data for analysis
- **Visualization**: Create meaningful charts and dashboards
- **Storytelling**: Communicate insights through visualizations

## Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter notebook:
   ```bash
   jupyter notebook notebooks/data_analysis.ipynb
   ```

## Dataset Overview

The `raw_sales_data.csv` contains sales transaction data with intentional data quality issues:
- Missing values in various columns
- Duplicate entries
- Outliers in price and quantity
- Inconsistent data formats

## Analysis Steps

1. **Data Exploration**: Understand dataset structure and identify issues
2. **Data Cleaning**: Remove/handle missing values, duplicates, outliers
3. **Data Transformation**: Create new features and aggregations
4. **Visualization**: Generate insights through charts and dashboards
5. **Reporting**: Document findings and recommendations

## Visualizations Included

- Distribution plots for numeric columns
- Missing data heatmaps
- Box plots for outlier detection
- Sales trends over time
- Category-wise analysis
- Correlation heatmaps

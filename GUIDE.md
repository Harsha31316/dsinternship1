# Getting Started Guide

## Quick Start

### 1. Environment Setup

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Analysis

**Option A: Using Jupyter Notebook (Recommended for Learning)**

```bash
cd notebooks
jupyter notebook data_analysis.ipynb
```

**Option B: Run Python Scripts**

```bash
cd scripts
python -c "from data_loader import load_data; df = load_data('../data/raw_sales_data.csv'); print(df.head())"
```

### 3. View Results

Check the `/output` directory for:
- `data_cleaning_summary.png` - Before/after data quality comparison
- `summary_report.txt` - Key metrics and statistics
- Other generated visualizations

Processed data: `/data/processed_sales_data.csv`

---

## Project Overview

### Data Cleaning Pipeline

1. **Load Raw Data** → Inspect structure and identify issues
2. **Handle Missing Values** → Use mean/mode imputation
3. **Remove Duplicates** → Keep first occurrence
4. **Treat Outliers** → Use IQR method to remove extreme values
5. **Transform Features** → Create new columns, convert types
6. **Validate Output** → Ensure data quality

### Visualization Techniques

| Chart Type | Use Case |
|-----------|----------|
| Heatmap | Visualize missing data patterns |
| Histograms | Distribution of numeric columns |
| Box Plots | Identify and visualize outliers |
| Scatter Plots | Relationships between variables |
| Bar Charts | Category comparisons |
| Time Series | Trends over time |
| Correlation Matrix | Relationships between all variables |

---

## File Structure Reference

```
ds lab-1/
├── data/
│   ├── raw_sales_data.csv              # Input data with quality issues
│   └── processed_sales_data.csv        # Cleaned output
├── notebooks/
│   └── data_analysis.ipynb             # Main interactive analysis
├── scripts/
│   ├── __init__.py                     # Package initialization
│   ├── data_loader.py                  # Load & inspect functions
│   ├── data_cleaner.py                 # Cleaning pipeline
│   └── visualizer.py                   # Visualization functions
├── output/
│   ├── data_cleaning_summary.png       # Summary dashboard
│   └── summary_report.txt              # Key findings
├── requirements.txt                    # Dependencies
└── README.md                           # Project documentation
```

---

## Data Cleaning Steps Explained

### Step 1: Remove Duplicates
- **Why**: Duplicate records skew analysis and inflate metrics
- **Method**: Keep first occurrence of identical records
- **Example**: Same customer placing identical order twice

### Step 2: Handle Missing Values
- **Numeric columns** (Quantity, Price): Fill with column mean
- **Categorical columns** (Status): Fill with column mode
- **Why**: Missing data could represent avg behavior or most common status

### Step 3: Remove Outliers
- **Method**: Interquartile Range (IQR) with threshold 1.5
- **Formula**: Remove values outside [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
- **Example**: Order with Quantity=100 (far from typical 1-9 range)

### Step 4: Feature Engineering
- **Temporal features**: Extract year, month, day from dates
- **Categorical bins**: Group prices into Low/Medium/High
- **Why**: These features improve analysis and modeling

---

## Key Metrics & KPIs

- **Data Quality Score**: % of non-null values
- **Total Revenue**: Sum of all transactions
- **Average Order Value**: Total revenue ÷ number of orders
- **Customer Lifetime Value**: Total revenue per customer
- **Completion Rate**: % of completed orders
- **Regional Performance**: Revenue by geographic area

---

## Learning Outcomes

After completing this project, you will understand:

✓ How to identify and handle data quality issues  
✓ Appropriate techniques for different data types  
✓ Creating meaningful visualizations for data exploration  
✓ Feature engineering for improved analysis  
✓ Building data pipelines with Python  
✓ Communicating insights through dashboards  

---

## Troubleshooting

**Issue**: Jupyter notebook won't start  
**Solution**: Ensure you're in the correct directory and have jupyter installed: `pip install jupyter`

**Issue**: Import errors in notebook  
**Solution**: Verify scripts folder is in the path. The notebook adds `../scripts` to sys.path automatically.

**Issue**: Missing visualizations  
**Solution**: Check that matplotlib backend is set correctly. Try `%matplotlib inline` in Jupyter.

**Issue**: Data not loading  
**Solution**: Verify the CSV file exists at `../data/raw_sales_data.csv` with correct path.

---

## Advanced Extensions

1. **Automated Data Quality Monitoring**
   ```python
   # Monitor data quality metrics over time
   # Alert when quality score drops below threshold
   ```

2. **Advanced Outlier Detection**
   ```python
   # Use Isolation Forest or Local Outlier Factor
   # More sophisticated than IQR for multivariate data
   ```

3. **Predictive Modeling**
   ```python
   # Forecast future sales using cleaned data
   # Perform regression or time series analysis
   ```

4. **Interactive Dashboards**
   ```python
   # Create web-based dashboards with Plotly/Dash
   # Real-time data updates and filters
   ```

---

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/gallery.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Data Cleaning Best Practices](https://www.kaggle.com/learn/data-cleaning)

---

**Happy Data Cleaning! 📊**

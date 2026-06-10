# Project Configuration & Settings

## Data Cleaning Parameters

### Missing Value Handling
- **Numeric columns**: mean imputation
- **Categorical columns**: mode imputation
- **Threshold**: Fill if < 50% of data missing

### Outlier Detection
- **Method**: Interquartile Range (IQR)
- **Threshold**: 1.5 × IQR
- **Formula**: Remove if value < Q1 - 1.5×IQR or value > Q3 + 1.5×IQR

### Duplicate Detection
- **Subset columns**: Date, Product, Customer_ID, Quantity
- **Keep**: First occurrence

## Visualization Settings

### Plot Defaults
- **Figure size**: 14 × 8 inches
- **DPI**: 300 (for saved images)
- **Style**: Seaborn whitegrid
- **Font size**: 10pt

### Color Schemes
- Primary: Viridis colormap
- Categorical: Named colors (skyblue, coral, green, etc.)
- Heatmap: Coolwarm diverging colors

## Feature Engineering Rules

### Temporal Features
- Extract: Year, Month, Day, DayOfWeek, Week
- From: Date column

### Categorical Bins
- **Price Category**: Low (0-25), Medium (25-40), High (40+)
- **Quantity Category**: Low (0-3), Medium (3-7), High (7+)

## Data Quality Metrics

- **Completeness**: % of non-null values
- **Accuracy**: Validated against business rules
- **Consistency**: Format and type consistency
- **Timeliness**: Data recency

## Output Formats

### Visualizations
- **Format**: PNG at 300 DPI
- **Location**: `/output/`
- **Naming**: Descriptive with underscores

### Data Exports
- **Format**: CSV (UTF-8 encoded)
- **Location**: `/data/`
- **Delimiter**: Comma

### Reports
- **Format**: Text file (.txt)
- **Location**: `/output/`
- **Encoding**: UTF-8

## Performance Optimization

### Memory Usage
- Use `int32` for integer columns
- Use `float32` for decimal columns
- Use `category` dtype for repeated strings

### Processing Speed
- Vectorized operations (NumPy/Pandas)
- Avoid Python loops where possible
- Chunked processing for large datasets (>1M rows)

## Error Handling

### Common Issues & Solutions
1. **File not found**: Verify path and file permissions
2. **Memory error**: Reduce chunk size or sample data
3. **Invalid values**: Check data encoding (UTF-8)
4. **Type mismatch**: Explicit dtype conversion

## Logging & Monitoring

- All cleaning operations logged
- Timestamps recorded
- Record counts before/after each step
- Quality metrics computed and saved

## Version Control

- **Version**: 1.0.0
- **Python**: 3.8+
- **Dependencies**: See requirements.txt
- **Last Updated**: 2024

## Extensibility

### Easy Customizations
1. Modify cleaning parameters in `data_cleaner.py`
2. Add new visualizations in `visualizer.py`
3. Create data_loader variants for different sources
4. Extend feature engineering in `run_analysis.py`

### Advanced Features (Future)
- Real-time data streaming
- Database integration
- API data sources
- Automated scheduling
- Multi-file processing

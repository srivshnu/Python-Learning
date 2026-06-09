# -------------------------------------------------------------
#DAY 25 - PANDAS DATA ANALYSIS
# -------------------------------------------------------------

# =============================================================
# 📘 Introduction to Pandas
# =============================================================

# Pandas is an open-source, high-performance library providing elegant 
# data structures and data analysis tools for the Python programming language.
# It introduces the two foundational data structures used in modern 
# data processing workflows: Series (1D) and DataFrames (2D).
# Key capabilities include: alignment, handling missing data, merging, 
# reshaping, slicing, and statistical aggregations.

# --- Installation via terminal ---
# pip install pandas

# --- Importing standard data stack dependencies ---
import pandas as pd
import numpy as np

# =============================================================
# 📘 Working with Pandas Series
# =============================================================
# A Series is a labeled, one-dimensional array capable of holding any data type.
# It can be thought of as a single column in a structural spreadsheet.

# --- 1. Series with Default Numeric Index ---
scores = [85, 92, 78, 90, 88]
series_scores = pd.Series(scores)
print('Default Index Series:\n', series_scores)

# --- 2. Series with Custom Explict Labels ---
series_custom = pd.Series(scores, index=['User_A', 'User_B', 'User_C', 'User_D', 'User_E'])
print('\nCustom Index Series:\n', series_custom)

languages = ['Python', 'Golang', 'Rust']
lang_series = pd.Series(languages, index=[101, 102, 103])
print('\nLanguages Series:\n', lang_series)

# --- 3. Series Generation from Python Dictionaries ---
metadata_dict = {'project_id': 'PRJ-901', 'status': 'Active', 'lead': 'Sarah'}
series_meta = pd.Series(metadata_dict)
print('\nDictionary-derived Series:\n', series_meta)

# --- 4. Scalar Constant Initialization ---
series_constant = pd.Series(5.5, index=['metric_1', 'metric_2', 'metric_3'])
print('\nConstant Value Series:\n', series_constant)

# --- 5. Series Construction using NumPy Sequences ---
series_linspace = pd.Series(np.linspace(10, 50, 5))
print('\nLinspace-derived Series:\n', series_linspace)


# =============================================================
# 📘 Construction of DataFrames
# =============================================================
# A DataFrame represents a tabular, spreadsheet-like data structure 
# containing an ordered collection of columns (Series).

# --- 1. DataFrame from Matrix / List of Lists ---
matrix_data = [
    ['Engineering', 'DevOps', 'Mumbai'],
    ['Product', 'Design', 'Bengaluru'],
    ['Analytics', 'Data Science', 'Hyderabad']
]
df_matrix = pd.DataFrame(matrix_data, columns=['Department', 'Role', 'Hub'])
print('\nDataFrame from Matrix:\n', df_matrix)

# --- 2. DataFrame from Dictionary of Equal-Length Lists ---
dict_data = {
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Experience_Yrs': [4, 7, 2],
    'Remote_Status': [True, False, True]
}
df_dict = pd.DataFrame(dict_data)
print('\nDataFrame from Dictionary:\n', df_dict)

# --- 3. DataFrame from List of Struct Dictionaries ---
struct_data = [
    {'Asset': 'Server_01', 'Uptime_Pct': 99.98, 'Risk_Level': 'Low'},
    {'Asset': 'Server_02', 'Uptime_Pct': 94.12, 'Risk_Level': 'High'},
    {'Asset': 'Server_03', 'Uptime_Pct': 98.50, 'Risk_Level': 'Medium'}
]
df_struct = pd.DataFrame(struct_data)
print('\nDataFrame from Struct List:\n', df_struct)


# -------------------------------------------------------------
# IO Operations & Structural Exploration
# -------------------------------------------------------------
# Local file operations can be processed natively via pandas engine.
# Example payload pulling:
# curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv

# df_csv = pd.read_csv('weight-height.csv')

# --- Inspection APIs ---
# print(df_csv.head(10))     # Inspect initial N records
# print(df_csv.tail(10))     # Inspect trailing N records
# print(df_csv.shape)        # Dimension footprint tuple (rows, columns)
# print(df_csv.columns)      # Index array of explicit columns
# print(df_csv.info())       # Memory allocation, schema, missing-value map

# --- Structural Extraction ---
# series_extracted = df_csv['Height']
# print(series_extracted.describe()) # Full statistical matrix summary


# -------------------------------------------------------------
# Mutation & Feature Engineering
# -------------------------------------------------------------
raw_metrics = [
    {"Host_Node": "Node_Alpha", "Region": "US-East", "Base_Load": 450},
    {"Host_Node": "Node_Beta", "Region": "EU-West", "Base_Load": 600},
    {"Host_Node": "Node_Gamma", "Region": "AP-South", "Base_Load": 310}
]
df_compute = pd.DataFrame(raw_metrics)

# --- Adding New Columns (Feature Assignment) ---
peak_offsets = [120, 240, 95]
df_compute['Peak_Offset'] = peak_offsets

scaling_factor = [1.25, 1.30, 1.12]
df_compute['Scaling_Factor'] = scaling_factor
print('\nDataFrame Post Feature Addition:\n', df_compute)

# --- Vectorized Transform Operations ---
# Modifying inline column values elements without iteration loops
df_compute['Peak_Offset'] = df_compute['Peak_Offset'] * 1.5

# --- Complex Multi-Column Calculated Fields ---
def evaluate_total_capacity():
    load = df_compute['Base_Load']
    offset = df_compute['Peak_Offset']
    factor = df_compute['Scaling_Factor']
    capacity_arr = []
    for l, o, f in zip(load, offset, factor):
        calculated_metric = (l + o) * f
        capacity_arr.append(calculated_metric)
    return capacity_arr

df_compute['Total_Capacity'] = evaluate_total_capacity()

# --- Formatting Elements Row-Wise ---
df_compute['Total_Capacity'] = round(df_compute['Total_Capacity'], 2)
print('\nDataFrame Post Vectorized Evaluation:\n', df_compute)

# --- Dynamic Structural Type Alteration ---
provision_year = ['2021', '2023', '1905']  # Note: 1905 is an extreme tracking outlier
current_epoch = pd.Series(2026, index=[0, 1, 2])

df_compute['Provision_Year'] = provision_year
df_compute['Current_Epoch'] = current_epoch

print('\nDatatypes before structural casting:\n', df_compute.dtypes)

# Converting object/string fields to explicit numerical representations
df_compute['Provision_Year'] = df_compute['Provision_Year'].astype('int32')
df_compute['Current_Epoch'] = df_compute['Current_Epoch'].astype('int32')

# Evaluating delta age of active hardware assets using vectorized math
df_compute['Asset_Lifespan_Yrs'] = df_compute['Current_Epoch'] - df_compute['Provision_Year']
print('\nMutated DataFrame with System Age Calculation:\n', df_compute)


# -------------------------------------------------------------
# Masking & Boolean Indexing Filters
# -------------------------------------------------------------
# Querying and isolating rows based on logical criteria

print('\nIsolating Outlier Anomalies (Lifespan > 50 Years):\n', 
      df_compute[df_compute['Asset_Lifespan_Yrs'] > 50])

print('\nIsolating Valid Standard Running Assets (Lifespan <= 50 Years):\n', 
      df_compute[df_compute['Asset_Lifespan_Yrs'] <= 50])

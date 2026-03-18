import pandas as pd
import numpy as np   

def detect_outliers(series):
  # using Interquartile Range
  Q1 = series.quantile(0.25)
  Q3 = series.quantile(0.75)
  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5*IQR
  upper_bound = Q3 + 1.5*IQR

  outliers = series[(series < lower_bound) | (series > upper_bound)]

  return {
      'outlier_count': len(outliers),
      'outlier_ratio': len(outliers) / len(series) if len(series) > 0 else 0,
      'bounds': (lower_bound, upper_bound)
  }
  



# =======================================================================


def calculate_skewness(series):
  return series.skew()



# =======================================================================


def infer_feature_type(series, categorical_threshold = 20):
  if series.nunique() <= 1: 
    return 'constant'

  if pd.api.types.is_numeric_dtype(series):
    if series.nunique() < categorical_threshold:
      return 'numeric_categorical'
    return 'numeric'

  if pd.api.types.is_datetime64_any_dtype(series):
    return 'datetime'

  return 'categorical'




# =======================================================================




def get_missing_stats(series):
  """
  return nan_count & nan_ratio
  """
  nan_count = series.isnull().sum()
  return {
      'nan_count': nan_count,
      'nan_ratio': nan_count / len(series) if len(series) > 0 else 0
  }




# ============================================================================





def get_cardinality_stats(series):
  """
  checking data type diversity using a relative ratio
  """

  distinct_count = series.nunique()
  total_count = len(series)

  distinct_ratio = distinct_count / total_count if total_count > 0 else 0

  is_high = (distinct_ratio > 0.3) or (distinct_count > 50)
  
  return {
      'distinct_count': distinct_count,
      'distinct_ratio': distinct_ratio,
      'is_high_cardinality': is_high 
  }




# ============================================================================





def check_class_imbalance(series):
  """
  categorical target only
  """

  counts = series.value_counts(normalize = True)
  imbalanced_ratio = counts.min() / counts.max() # min / max
  return {
      'class_distribution': counts.to_dict(),
      'is_imbalanced': imbalanced_ratio < 0.2 # 1:5
  }




# ============================================================================

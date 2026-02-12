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
  checking data type diversity 
  """

  distinct_count = series.nunique()
  return {
      'distinct_count': distinct_count,
      'is_high_cardinality': distinct_count > 50 
  }




# ============================================================================





def check_class_imbalance(series):
  """
  categorical target only
  """

  counts = series.value_counts(normalize = True)
  imbalance_ratio = counts.min() / count.max() # min / max
  return {
      'class_distribution': counts.to_dict(),
      'is_imbalanced': imbalanced_ration < 0.2 # 1:5
  }




# ============================================================================

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
  }   'bounds': (lower_bound, upper_bound)



def calculate_skewness(series):
  return series.skew()

from sklearn.preprocessing import StandardScaler, RobustScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer

def apply_scaling(series, method = 'standard'):
  if method == 'robust_scale':
    scaler = RobustScaler()

  else: 
    scaler = StandardScaler()

  return scaler.fit_transform(series.values.reshape(-1, 1))





# ============================================================================





def apply_imputation(series, dtype):
  strategy = 'median' if dtype = 'numeric' else 'most_frequent'
  imputer = SimpleImputer(strategy = strategy)

  return imupter.fit_transform(series.values.reshape(-1, 1))

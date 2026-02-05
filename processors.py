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





# ============================================================================





def apply_onehot_encoding(series, col_name):

  encoder = OneHotEncoder(handle_unknown = 'ignore', sparse_output = False)

  encoded_data = encoder.fit_transform(series.values.reshape(-1, 1))

  new_col_names = [f"{col_name}_{cat}" for cat in encoder.categories_[0]]

  encoded_df = pd.DataFrame(encoded_data, columns = new_col_names, index = series.index)

  return encoded_df, encoder

import numpy as np
import pandas as pd

class toolbox:
  def __init__ (self):
    self.data = None
    self.target = None
    self.metadata = None
    self.config = {}

  

  def setup(self, data, target, ignore_features=None, numeric_feature=None, categorical_feature=None):
    """
    initialize my metadata and config
    """

    print('--- INITIALIZING SETUP ---')
    self.data = data.copy()
    self.target = target
    self.config['ignore'] = ignore_features or []

    #1. remove ignore columns before analyzing
    features_to_analyze = [c for c in self.data.columns if c not in self.config and c != target]

    #2. metadata function
    self.metadata = self._extract_metadata(self.data[features_to_analyze])

    #3. override metadata for users' calling
    if numeric_features:
      for col in numeric_features:
        if col in self.metadata: self.metadata[col]['type'] = 'numeric'
    
    if categorical_features:
      for col in categorical_features:
        if col in self.metadata: self.metadata[col]['type'] = 'categorical'

  

  def _extract_metadata(self, df):
    """ay
    metadata is created here
    """
    meta = {}

    for col in df.columns:
      if pd.api.types.is_numeric_dtype(df[col]):
        dtype = 'numeric'
      else:
        dtype = 'categorical'

      meta[col] = {
                'type': dtype,
                'nan_ratio': df[col].isnull().mean(),
                'unique_count': df[col].nunique(),
                'suggested_imputer': 'mean' if dtype == 'numeric' else 'most_frequent',
                'suggested_scaler': 'standard' if dtype == 'numeric' else None
      }

      return meta



    def show_metadata(self):
      return pd.DataFrame(self.metadat).T

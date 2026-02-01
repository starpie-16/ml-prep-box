import numpy as np
import pandas as pd
import utils

class toolbox:
  def __init__ (self):
    self.data = None
    self.target = None
    self.metadata = None
    self.config = {}
    self.custom_registry = {}



  def setup(self, data, target, ignore_features=None, numeric_features=None, categorical_features=None):
    """
    initialize my metadata and config
    """

    print('--- INITIALIZING SETUP ---')
    self.data = data.copy()
    self.target = target
    self.config['ignore'] = ignore_features or []

    features_to_analyze = [c for c in self.data.columns if c not in self.config['ignore'] and c != target]

    overrides = {}

    if numeric_features:
        for col in numeric_features: overrides[col] = 'numeric'

    if categorical_features:
        for col in categorical_features: overrides[col] = 'categorical'

    self.metadata = self._extract_metadata(self.data[features_to_analyze], overrides)


  def _extract_metadata(self, df):
    """
    metadata is created here
    """
    meta = {}

    for col in df.columns:
      series = df[col]

      col_type = overrides.get(col) or utils.infer_feature_type(series) #categorical or numeric

      missing_stats = utils.get_missing_stats(series)
      cardinality_stats = utils.get_cardinality_stats(series)

      meta[col] = {
                'type': col_type,
                'nan_ratio':missing_stats['nan_ratio'],
                'distinct_values': cardinality_stats['distinct_count'],
                'is_high_cardinality': cardinality_stats['is_high_cardinality'],
                'is_constant': col_type == 'constant'
      }

      if col == self.target and col_type == 'categorical':
        meta[col]['imbalance_info'] = utils.check_class_imbalance(series)


      if col_type == 'numeric':
        meta[col].update({
            'skew': utils.calculate_skewness(series),
            'outlier_ratio': utils.detect_outliers(series)['outlier_ratio']
        })

      meta[col]['action'] = self. _get_suggested_action(meta[col])

    return meta


  
  def _get_suggested_action(self, col_meta):

    # --- 1. global rules ---
      if col_meta.get('is_constant') or col_meta.get('nan_ratio', 0) > 0.5:
        return 'drop'

    # --- 2. numeric precess ---

      if col_meta['type'] == 'numeric':
        outlier_ratio = col_meta.get('outlier_ratio', 0)
        skew_val = col_meta.get('skew', 0)

        if outlier_ratio > 0.05 or abs(skew_val) > 1.0:
          return 'robust_scale'
        return 'standard_scale'

    # --- 3. categorical process ---
      if col_meta['type'] == 'categorical':
        if col_meta.get('is_high_cardinality'):
          return 'label_encode'
        return 'onehot_encode'

      return 'passthrough'

      

  def _register_custom_action(self, action_name, func):
      self.custom_registry[action_name] = func
      print(f" Registered custom action: {action_name}")

  def show_metadata(self):
      return pd.DataFrame(self.metadata).T

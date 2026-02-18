# test_run.py (nằm ngoài folder datawise)
from datawise import toolbox
import pandas as pd

df = pd.read_csv('dataset/raw/titanic.csv')
prep = toolbox()
# Chạy thử thôi!
prep.setup(df, target='Survived')
prep.suggest()
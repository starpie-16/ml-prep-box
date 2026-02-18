from datawise import toolbox
import pandas as pd

df = pd.read_csv('dataset/raw/titanic.csv')
prep = toolbox()
prep.setup(df, target='Survived')
prep.suggest()

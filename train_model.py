import pandas as pd
import statsmodels.api as sm
import joblib

df = pd.read_csv('mtcars.csv')
y = df['mpg']
X = df.drop(columns=['mpg'])

columns = sm.add_constant(X).columns.tolist()
joblib.dump(columns, 'columns.pkl')

X_const = sm.add_constant(X)
model = sm.OLS(y, X_const).fit()

joblib.dump(model, 'model.pkl')

print("Model and columns saved.")
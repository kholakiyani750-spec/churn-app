import joblib
model = joblib.load('churn_best_model.joblib')
columns = joblib.load('churn_columns.joblib')
print(type(model))
print(columns)

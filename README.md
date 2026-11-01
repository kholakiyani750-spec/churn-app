# Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to leave (churn) or stay. The project includes a full notebook with model comparison and a Streamlit web app for live predictions.

**Live app:** https://churn-app-a3qmdbtpx9wn587kod53ev.streamlit.app/

**Notebook:** [notebooks/churn-prediction-with-ml-algorithms.ipynb](notebooks/churn-prediction-with-ml-algorithms.ipynb)

## Project Overview

Customer churn means a customer stops using a company's service. Predicting churn early lets a company offer discounts or support to keep customers. This project trains several classification models on customer data and deploys the best one in a simple web interface.

## Dataset

The data is a customer churn dataset from Kaggle (Telco Customer Churn style). Each row is one customer, with features such as:

- Senior citizen status
- Tenure (months with the company)
- Monthly and total charges
- Gender, partner, and dependents
- Phone and internet services
- Contract type

The target is `Churn`: `1` means the customer left, `0` means the customer stayed.

## Approach

1. Explored the data and checked the churn rate.
2. Encoded categorical columns using one-hot encoding.
3. Built preprocessing and modeling pipelines with scikit-learn.
4. Compared several classifiers, including Logistic Regression, Random Forest, AdaBoost, Gradient Boosting, and XGBoost.
5. Kept the best-performing model and saved it with `joblib`, along with the training column names.
6. Built a Streamlit app that takes customer inputs and returns a churn prediction with probability.

## Key Insights

- Customers with short tenure are more likely to churn.
- Month-to-month contracts show a higher churn risk than one-year or two-year contracts.
- Customers with fiber optic internet showed higher churn in the model's predictions.

## Repository Structure

```text
churn-app/
├── notebooks/
│   └── churn-prediction-with-ml-algorithms.ipynb   # Full analysis notebook
├── app.py                      # Streamlit web app
├── churn_best_model.joblib     # Trained model pipeline
├── churn_columns.joblib        # Training column names
├── check_model.py              # Script to inspect the saved model
├── requirements.txt            # Python libraries needed
└── .gitignore                  # Files Git should ignore
```

## Notebook

The full analysis, including data exploration, model training, and evaluation, is in `notebooks/churn-prediction-with-ml-algorithms.ipynb`. You can open it on GitHub to view the code and outputs, or run it in Jupyter or Kaggle.

## How to Run the App Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/kholakiyani750-spec/churn-app.git
   cd churn-app
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open `http://localhost:8501` in your browser.

## Technologies Used

- Python
- scikit-learn
- pandas and NumPy
- XGBoost
- joblib
- Streamlit

## Notes

- The model was trained with scikit-learn 1.6.1. Using the same version avoids compatibility warnings.
- This project is for learning and demonstration. Predictions should not be used as the only basis for business decisions.

## Author

Khola Noor Kiyani
GitHub: [@kholakiyani750-spec](https://github.com/kholakiyani750-spec)

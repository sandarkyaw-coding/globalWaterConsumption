# import pandas as pd

# # load dataset
# df = pd.read_csv("global_water_consumption_2000_2025.csv")

# # print(df.head())
# # print(df.info())

# # Encode Scarcity Level
# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()
# df["Water Scarcity Level"] = le.fit_transform(df["Water Scarcity Level"])


# # Classification Model
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

# X = df.drop(["Country", "Water Scarcity Level"], axis=1)
# y = df["Water Scarcity Level"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# print("Accuracy:", model.score(X_test, y_test))

# # Forecast Future Consumption
# from sklearn.ensemble import RandomForestRegressor

# X_reg = df.drop(["Country", "Water Scarcity Level", "Total Water Consumption (Billion m3)"], axis=1)
# y_reg = df["Total Water Consumption (Billion m3)"]

# model_reg = RandomForestRegressor()
# model_reg.fit(X_reg, y_reg)

# # save model
# import joblib

# # Save classification model
# joblib.dump(model, "water_scarcity_classifier.pkl")

# # Save regression model
# joblib.dump(model_reg, "water_consumption_regressor.pkl")

# # Save label encoder
# joblib.dump(le, "label_encoder.pkl")

# print("Models saved successfully!")

# import numpy as np

# # Get last year data (2025)
# last_year = df[df["Year"] == 2025]

# future_years = [2026, 2027, 2028, 2029, 2030]

# future_predictions = []

# for year in future_years:
#     future_data = last_year.copy()
#     future_data["Year"] = year

#     # Drop columns not used in regression
#     X_future = future_data.drop(
#         ["Country", "Water Scarcity Level", "Total Water Consumption (Billion m3)"],
#         axis=1
#     )

#     prediction = model_reg.predict(X_future)
    
#     future_predictions.append({
#         "Year": year,
#         "Predicted Consumption": np.mean(prediction)
#     })

# future_df = pd.DataFrame(future_predictions)

# print(future_df)


import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score

# 1. Load Dataset
df = pd.read_csv("global_water_consumption_2000_2025.csv")

# 2. Encoding
le = LabelEncoder()
df["Water Scarcity Level"] = le.fit_transform(df["Water Scarcity Level"])

# --- MODEL 1: CLASSIFICATION (Scarcity Level) ---
X_clf = df.drop(["Country", "Water Scarcity Level"], axis=1)
y_clf = df["Water Scarcity Level"]
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

clf_model = RandomForestClassifier(n_estimators=200, random_state=42)
clf_model.fit(X_train_c, y_train_c)

# Calculate Classification Accuracy
y_pred_c = clf_model.predict(X_test_c)
clf_accuracy = accuracy_score(y_test_c, y_pred_c)

# --- MODEL 2: REGRESSION (Consumption Amount) ---
X_reg = df.drop(["Country", "Water Scarcity Level", "Total Water Consumption (Billion m3)"], axis=1)
y_reg = df["Total Water Consumption (Billion m3)"]
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg_model = RandomForestRegressor(n_estimators=200, random_state=42)
reg_model.fit(X_train_r, y_train_r)

# Calculate Regression Accuracy (R2 Score)
y_pred_r = reg_model.predict(X_test_r)
reg_accuracy = r2_score(y_test_r, y_pred_r)
mae = mean_absolute_error(y_test_r, y_pred_r)

# 3. Print Accuracy Report
print("-" * 30)
print("ACCURACY REPORT")
print("-" * 30)
print(f"Scarcity Classifier Accuracy: {clf_accuracy * 100:.2f}%")
print(f"Consumption Regressor Accuracy (R2): {reg_accuracy * 100:.2f}%")
print(f"Average Error (MAE): {mae:.4f} Billion m3")
print("-" * 30)

# 4. Save
joblib.dump(clf_model, "water_scarcity_classifier.pkl")
joblib.dump(reg_model, "water_consumption_regressor.pkl")
joblib.dump(le, "label_encoder.pkl")

# --- Save Accuracy Metrics for UI ---
metrics = {
    "clf_accuracy": clf_accuracy,
    "reg_accuracy": reg_accuracy,
    "mae": mae
}
joblib.dump(metrics, "model_metrics.pkl")
print("Metrics saved successfully!")
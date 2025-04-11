import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json

# Read the CSV file
df = pd.read_csv('JEE_Dropout_After_Class_12.csv')

# Convert categorical variables to numerical using label encoding
categorical_columns = ['school_board', 'coaching_institute', 'family_income', 
                      'parent_education', 'location_type', 'peer_pressure_level', 
                      'mental_health_issues', 'admission_taken']
                      
for column in categorical_columns:
    df[column] = pd.Categorical(df[column]).codes

# Separate features and target
X = df.drop(['dropout'], axis=1)
y = df['dropout']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save the model using pickle instead of joblib
with open('model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

# Save feature names and categorical mappings for Django
feature_config = {
    'feature_names': X.columns.tolist(),
    'categorical_mappings': {}
}

# Store category mappings for each categorical column
for column in categorical_columns:
    unique_values = df[column].unique()
    mapping = {str(i): i for i in range(len(unique_values))}
    feature_config['categorical_mappings'][column] = mapping

# Save the configuration
with open('model_config.json', 'w') as f:
    json.dump(feature_config, f)

# Make predictions
y_pred = rf_model.predict(X_test)

# Generate plots
plt.figure(figsize=(15, 10))

# 1. Confusion Matrix Heatmap
plt.subplot(2, 2, 1)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')

# 2. Feature Importance Plot
plt.subplot(2, 2, 2)
importances = pd.DataFrame({'features': X.columns, 'importance': rf_model.feature_importances_})
importances = importances.sort_values('importance', ascending=False)
sns.barplot(x='importance', y='features', data=importances.head(10))
plt.title('Top 10 Feature Importance')

# 3. Correlation Matrix
plt.subplot(2, 2, 3)
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')

# 4. Distribution Plot of Numerical Features
plt.subplot(2, 2, 4)
sns.histplot(data=df, x='jee_main_score', hue='dropout', bins=30)
plt.title('Distribution of JEE Main Scores by Dropout Status')

plt.tight_layout()
plt.savefig('analysis_plots.png')
plt.close()

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Print model accuracy
print(f"\nModel Accuracy: {rf_model.score(X_test, y_test):.2%}")
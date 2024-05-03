from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from imblearn.over_sampling import SMOTE
import pandas as pd
import numpy as np

# Load the merged dataframe
merged_df = pd.read_csv(r'../../datasets/cleaned datasets/merged_cleaned.csv')
word_frequencies = pd.read_csv(r'../../datasets/feature engineered datasets/word_frequencies.csv')
sentiment_scores = pd.read_csv(r'../../datasets/feature engineered datasets/sentiment_scores.csv')
tfidf_representations = pd.read_csv(r'../../datasets/vectorized datasets/tfidf_vectorized.csv')
spacy_representations = pd.read_csv(r'../../datasets/vectorized datasets/spacy_vectorized.csv')

# Split features and target
Y = merged_df['priority'].values  # The target

# The type column
type_feature = merged_df['type'].values
# Reshape it before concatenation
type_feature = type_feature.reshape(-1, 1)

# Concatenate the features
X = np.hstack((spacy_representations, tfidf_representations, type_feature, word_frequencies, sentiment_scores))

# X_df = pd.DataFrame(X)   #to see the training data as a whole
# X_df.to_csv('../../datasets/X_df.csv', index=False)

# Split data into train-test-validation sets
X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val, test_size=0.25, random_state=42)  # 0.25 x 0.8 = 0.2

# Perform SMOTE to balance the minority class on the training set
smote = SMOTE(random_state=42)
X_train_resampled, Y_train_resampled = smote.fit_resample(X_train, Y_train)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_resampled)
X_test_scaled = scaler.transform(X_test)

# Create RandomForestClassifier with class weighting
rf_model = RandomForestClassifier(min_samples_leaf=10, min_samples_split=5, n_estimators=50, max_features=0.6, max_depth=5)

# Perform cross-validation
cv_scores = cross_val_score(rf_model, X_train_scaled, Y_train_resampled, cv=5)

# Print cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean Accuracy:", np.mean(cv_scores))

# Train the model on the entire training set
rf_model.fit(X_train_scaled, Y_train_resampled)

# Evaluate the model on the test set
Y_pred = rf_model.predict(X_test_scaled)
accuracy = accuracy_score(Y_test, Y_pred)
print("\nAccuracy on Test Set:", accuracy)

print('\nConfusion Matrix:\n', confusion_matrix(Y_test, Y_pred))
print('\nClassification Report:\n', classification_report(Y_test, Y_pred))


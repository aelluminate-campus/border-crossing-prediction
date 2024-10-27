import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("datasets/processed.csv")

data['date'] = pd.to_datetime(data['date'], errors='coerce')
data['year'] = data['date'].dt.year

X = data[['value', 'year']]
y = data['border'].factorize()[0]

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_filenames = ["Data/Logistic_Regression.pkl", "Data/Random_Forest.pkl", "Data/SVM.pkl", "Data/Decision_Tree.pkl", "Data/K-Nearest_Neighbors.pkl"]
results = {}

for model_file in model_filenames:
    
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
        
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred, target_names=data['border'].unique(), output_dict=True)
    border_crossing = model_file.replace('.pkl', '').replace('_', ' ')
    results[border_crossing] = {
        "accuracy": accuracy,
        "classification_report": class_report
    }
    
    print(f"Model: {border_crossing}")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data['border'].unique(), yticklabels=data['border'].unique())
    plt.title(f'Confusion Matrix for {border_crossing}')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()


eval_df = pd.DataFrame.from_dict({
    border_crossing: {
        "Accuracy": res['accuracy'],
        "Precision": res['classification_report']['weighted avg']['precision'],
        "Recall": res['classification_report']['weighted avg']['recall'],
        "F1-Score": res['classification_report']['weighted avg']['f1-score']
    }
    for border_crossing, res in results.items()
}, orient='index')

eval_df.to_csv('datasets/model_evaluation_results.csv', index=False)
print("\nModel Evaluation Results saved to 'datasets/model_evaluation_results.csv'.")
print(eval_df)

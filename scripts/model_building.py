import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def build_model(input_path):
    
    # Load cleaned/processed data
    data = pd.read_csv(input_path)

    # Change String data values to categorical 
    data['species'] = data['species'].astype('category').cat.codes
    data['island'] = data['island'].astype('category').cat.codes
    data['sex'] = data['sex'].astype('category').cat.codes

    # Separate data on species and removed sex
    X = data.drop('species', axis = 1)
    y = data['species']

    # Split into training and test model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Set model (Random Forest Classifier)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict model
    y_pred = model.predict(X_test)
    
    # Print classification model
    print(classification_report(y_test, y_pred))

    # Print completion message
    print("Model building completed.")

if __name__ == "__main__":
    build_model('data/processed/penguins_processed.csv')
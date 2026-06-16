import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib

def main():
    print("Loading data...")
    df = pd.read_csv("Unemployment in India.csv", skipinitialspace=True)
    
    print("Initial shape:", df.shape)
    
    # Clean column names
    df = df.rename(columns={
        'Estimated Unemployment Rate (%)': 'Unemployment_rate',
        'Estimated Employed': 'Employed',
        'Estimated Labour Participation Rate (%)': 'Labour_participation'
    })
    
    # Drop missing values
    df = df.dropna().copy()
    print("Shape after dropping NaNs:", df.shape)
    
    # Date preprocessing
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    
    # Define features and target
    categorical_features = ['Region', 'Frequency', 'Area']
    numerical_features = ['Employed', 'Labour_participation', 'Month', 'Year']
    
    X = df[categorical_features + numerical_features]
    y = df['Unemployment_rate']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Preprocessing for numerical data
    numeric_transformer = StandardScaler()
    
    # Preprocessing for categorical data
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    # Bundle preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Define model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Bundle preprocessing and modeling code in a pipeline
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                          ('model', model)
                         ])
    
    print("Training model...")
    # Preprocessing of training data, fit model 
    clf.fit(X_train, y_train)
    
    print("Evaluating model...")
    # Preprocessing of validation data, get predictions
    preds = clf.predict(X_test)
    
    # Evaluate the model
    rmse = mean_squared_error(y_test, preds) ** 0.5
    mae = mean_absolute_error(y_test, preds)
    
    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")
    
    # Save the pipeline
    print("Saving model to model.joblib...")
    joblib.dump(clf, 'model.joblib')
    print("Done!")

if __name__ == "__main__":
    main()


import pandas as pd
import seaborn

def clean_data(input_path, output_path):
    # Load raw data
    data = seaborn.load_dataset("penguins")
    
    # Renaming columns
    data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]
        
    # Remove rows that have null value(s)
    data = data.dropna(how='any',axis=0) 
    
    # Save processed data
    data.to_csv(output_path, index=False)
    
    print("Data cleaning completed and saved to", output_path)

if __name__ == "__main__":
    filepath = "https://raw.githubusercontent.com/Jokoisme/penguins-classification/main/data/raw/penguins.csv"

    clean_data('penguins.csv', 'data/processed/penguins_processed.csv')

print("Data cleaning completed and saved to data/processed/iris_processed.csv")
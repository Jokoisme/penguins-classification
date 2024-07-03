
import pandas as pd
import seaborn

# Example cleaning: renaming columns

penguins = seaborn.load_dataset("penguins")
type(penguins)

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
    clean_data('penguins.csv', 'penguins_processed.csv')

data.to_csv('iris_processed.csv', index=False)

print("Data cleaning completed and saved to data/processed/iris_processed.csv")

import pandas as pd
import seaborn

def clean_data(input_path, output_path):
    # Load raw data
    data = seaborn.load_dataset("penguins")
    
    # Renaming columns
    data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]
        
    # Remove rows that have null value(s)
    data = data.dropna(how='any',axis=0) 

    # Change String data values to categorical 
    data['species'] = data['species'].astype('category').cat.codes
    data['island'] = data['island'].astype('category').cat.codes
    data['sex'] = data['sex'].astype('category').cat.codes

    # Change string data values to int
    # Island
    # Torgersen = 1, Biscoe = 2, Dream = 3
    # data.loc[data["island"] == "Torgersen", "island"] = 1
    # data.loc[data["island"] == "Biscoe", "island"] = 2
    # data.loc[data["island"] == "Dream", "island"] = 3

    # Sex
    # Male = 1, Female =2
    # data.loc[data["sex"] == "Male", "sex"] = 1
    # data.loc[data["sex"] == "Female", "sex"] = 2

    # Save processed data
    data.to_csv(output_path, index=False)
    
    print("Data cleaning completed and saved to", output_path)

if __name__ == "__main__":
    filepath = "https://raw.githubusercontent.com/Jokoisme/penguins-classification/main/data/raw/penguins.csv"

    clean_data('penguins.csv', 'data/processed/penguins_processed.csv')

print("Data cleaning completed and saved to data/processed/iris_processed.csv")
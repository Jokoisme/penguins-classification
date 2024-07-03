import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def perform_eda(input_path):
    # Change to processed data
    #data = sns.load_dataset("penguins")
    data = pd.read_csv(input_path)

    # Basic statistics
    print(data.describe())

    # Correlation
    
    # Change String data values to categorical 
    data['species'] = data['species'].astype('category').cat.codes
    data['island'] = data['island'].astype('category').cat.codes
    data['sex'] = data['sex'].astype('category').cat.codes

    dataplot = sns.heatmap(data.corr(), cmap="YlGnBu", annot=True) 
    plt.savefig("results/figures/correlation.png") 
    
    print("EDA completed. Correlation plot saved to results/figures.correlation.png")

if __name__ == "__main__":
    perform_eda('data/processed/penguins_processed.csv')
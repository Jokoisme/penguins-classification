import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def perform_eda(input_path):
    # Change to processed data
    #data = sns.load_dataset("penguins")
    data = pd.read_csv(input_path)

    # Get species per gender count 
    sex_column = data['sex']
    data.groupby(["species", sex_column]).size().unstack(level=1).plot(kind='bar')
    plt.xlabel("Species") 
    plt.ylabel("Number of penguins") 
    plt.title("Number of penguins for each species by gender") 
    plt.legend() 

    plt.savefig("results/figures/speciesCount.png")
    plt.show()

    # Basic statistics
    print(data.describe())

    # Set Seaborn style
    sns.set_style("darkgrid")

    # Identify numerical columns
    numerical_columns = data.select_dtypes(include=["int64", "float64"]).columns

    # Plot distribution of each numerical feature
    plt.figure(figsize=(14, len(numerical_columns) * 3))
    for idx, feature in enumerate(numerical_columns, 1):
        plt.subplot(len(numerical_columns), 2, idx)
        sns.histplot(data[feature], kde=True)
        plt.title(f"{feature} | Skewness: {round(data[feature].skew(), 2)}")

    # Adjust layout and show plots
    plt.tight_layout()
    plt.savefig("results/figures/numericalPlot.png") 
    plt.show()
    
    # Correlation
    
    # Change String data values to categorical 
    data['species'] = data['species'].astype('category').cat.codes
    data['island'] = data['island'].astype('category').cat.codes
    data['sex'] = data['sex'].astype('category').cat.codes

    dataplot = sns.heatmap(data.corr(), cmap="YlGnBu", annot=True) 
    plt.savefig("results/figures/correlation.png") 
    
    print("EDA completed. All plot saved to results/figure")

if __name__ == "__main__":
    perform_eda('data/processed/penguins_processed.csv')
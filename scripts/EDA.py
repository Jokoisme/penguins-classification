import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(input_path):
    # Change to processed data
    #data = sns.load_dataset("penguins")
    data = pd.read_csv(input_path)

    # Basic statistics
    print(data.describe())

    # Correlation
    sns.pairplot(data, hue = "species")
    plt.savefig("results/figures/pairplot.png") 
    
    print("EDA completed. Pairplot saved to results/figures/pairplot.png")

if __name__ == "__main__":
    perform_eda('penguins_processed.csv')
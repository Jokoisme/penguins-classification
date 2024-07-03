import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visualizations(input_path):
    
    # Load cleaned/processed data
    data = pd.read_csv(input_path)
    
    # Example visualization: Pairplot
    sns.pairplot(data, hue='species')
    plt.savefig('results/figures/pairplot.png')
    
    print("Visualizations created and saved to results/figures/pairplot.png")

if __name__ == "__main__":
    create_visualizations('data/processed/penguins_processed.csv')

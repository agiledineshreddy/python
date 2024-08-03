import pandas as pd
import matplotlib.pyplot as plt

# Load data
train = pd.read_csv("train.csv")
columns = ['buying_price', 'maintainence_cost', 'number_of_doors', 'number_of_seats', 'luggage_boot_size', 'safety_rating']

# Create scatter plots for each feature against popularity
for column in columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(train[column], train['popularity'], alpha=0.5, color='grey')
    plt.title(f'Relationship between {column} and Popularity')
    plt.xlabel(column)
    plt.ylabel('Popularity')
    plt.grid(True)
    plt.show()

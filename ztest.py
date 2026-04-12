import pandas as pd
import numpy as np
from scipy.stats import norm

df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")

sample = df['Sales']

sample_mean = np.mean(sample)
population_mean = df['Sales'].mean()
std_dev = np.std(sample)

n = len(sample)

z_score = (sample_mean - population_mean) / (std_dev / np.sqrt(n))

p_value = norm.cdf(z_score)

print("Sample Mean:", sample_mean)
print("Population Mean:", population_mean)
print("Z-Score:", z_score)
print("P-Value:", p_value)

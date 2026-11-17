

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:/Users/AWOPETU/Desktop/IMPLEMENTATION/TRAINING/Dengue_clinical_dataset.csv")



# FEATURES AND TARGET


df = pd.get_dummies(
    df,
    columns=['Location'],
)

cols = [col for col in df.columns if col != 'Outcome'] + ['Outcome']

df = df[cols]

correlation_matrix = df.corr(method='pearson')
plt.figure(figsize=(11,8))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Pearson Correlation Heatmap")

plt.tight_layout()

plt.show()
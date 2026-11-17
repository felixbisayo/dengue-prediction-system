import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:/Users/AWOPETU/Desktop/IMPLEMENTATION/TRAINING/Dengue_clinical_dataset.csv")
# print(df['Outcome'].unique)
df['Diagnosis'] = df['Outcome'].map({
    1: 'Positive',
    0: 'Negative'
})
order = ['Negative', 'Positive']

sns.set_style("whitegrid")

ax = sns.countplot(x='Diagnosis', data=df)
for container in ax.containers:
    ax.bar_label(container)


# plt.title("Distribution of Dengue-Positive and Negative Cases")
# plt.xlabel("Outcome")
# plt.ylabel("Number of Cases")
# plt.tight_layout()

plt.figure(figsize=(5,4))

sns.stripplot(
    x='Diagnosis',
    y='Platelet Count',
    data=df,
    order=order,
    jitter=True,
    alpha=0.5
)
median_values_p = df.groupby('Diagnosis')['Platelet Count'].median()
lowest_p = df.groupby('Diagnosis')['Platelet Count'].min()
highest_p = df.groupby('Diagnosis')['Platelet Count'].max()

# for i, (label, median) in enumerate(median_values_p.items()):

#     # Horizontal median line
#     plt.axhline(
#     y=median,
#     linestyle='--',
#     linewidth=0.5,
#     label=f'Median ({label})'
#     )

#     plt.text(
#     i,
#     -2000,   # adjust depending on your dataset scale
#     f'Median:\n{median:.1f}',
#     ha='center'
#     )

# sns.stripplot(
#     x='Diagnosis',
#     y='WBC',
#     data=df,
#     jitter=True,
#     order=order,
#     alpha=0.5
# )
# median_values_w = df.groupby('Diagnosis')['WBC'].median()
# lowest_w = df.groupby('Diagnosis')['WBC'].min()
# highest_w = df.groupby('Diagnosis')['WBC'].max()


for i, (label, median) in enumerate(median_values_p.items()):

    # Horizontal median line
    plt.axhline(
    y=median,
    linestyle='--',
    linewidth=0.5,
    label=f'Median ({label})'
    )

    plt.text(
    i,
    1000,   # adjust depending on your dataset scale
    f'Median:\n{median:.1f}',
    ha='center'
    )
print("MINIMUN VALUE: \n", lowest_p)
print("HIGHEST VALUE: \n", highest_p)
# plt.title("Distribution of WBCby Dengue Class")

counts = df['Outcome'].value_counts()

print(counts)

median_values = df.groupby('Diagnosis')[['Platelet Count', 'WBC']].median()
print("MEDIAN: \n", median_values)


# plt.show()

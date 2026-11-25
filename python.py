import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')

# clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# fill missing ratings
df['review_rating'] = df['review_rating'].fillna(
    df.groupby('category')['review_rating'].transform('median')
)

# age groups
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# purchase frequency in days
frequency_mapping = {
    'Fortnightly': 14, 'Weekly': 7, 'Monthly': 30, 'Quarterly': 90,
    'Bi-Weekly': 14, 'Annually': 365, 'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# save the cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("Saved cleaned_data.csv")
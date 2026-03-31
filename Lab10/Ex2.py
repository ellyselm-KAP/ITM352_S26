import pandas as pd

ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# Create list of tuples
age_gender = list(zip(ages, gender))
print(age_gender)

# Create dataframe
df = pd.DataFrame(age_gender, index=names, columns=["Age", "Gender"])

print("\nDataFrame:")
print(df)

# Summary stats
print("\nSummary:")
print(df.describe())

# Average age by gender
avg_age = df.groupby("Gender")["Age"].mean()
print("\nAverage age by gender:")
print(avg_age)


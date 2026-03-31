import pandas as pd

# a) Read CSV + show dimensions and first 10 rows
df = pd.read_csv("/Users/ellysemcchesney/Documents/GitHub/ITM352_S26/Lab10/homes_data.csv")

print("Dimensions:")
print(df.shape)

print("\nFirst 10 rows:")
print(df.head(10))


# b) Filter properties with 500+ units
filtered_df = df[df["units"] >= 500]

print("\nFiltered (500+ units):")
print(filtered_df.head(10))

#Part C
print(df.dtypes)

df["units"] = pd.to_numeric(df["units"], errors="coerce")
df["sale_price"] = pd.to_numeric(df["sale_price"], errors="coerce")
df["land_sqft"] = pd.to_numeric(df["land_sqft"], errors="coerce")
df["gross_sqft"] = pd.to_numeric(df["gross_sqft"], errors="coerce")

print(df.dtypes)
print(df.head(10))


# d) Drop nulls and duplicates
clean_df = df.dropna().drop_duplicates()

print("\nAfter removing nulls and duplicates:")
print(clean_df.head(10))


# e) Filter out 0 sales + average price
sales_df = clean_df[clean_df["sale_price"] > 0]

print("\nFiltered sales (>0):")
print(sales_df.head(10))

avg_price = sales_df["sale_price"].mean()

print("\nAverage sales price:")
print(avg_price)
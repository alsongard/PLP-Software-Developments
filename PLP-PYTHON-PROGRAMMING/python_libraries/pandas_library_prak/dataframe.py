import pandas as pd
users = {
    "name" : ['John', 'Robert', 'Alice', 'Eva'],
    "age" : [25, 30, 35, 40],
    "city" : ['New York', 'Los Angeles', 'Chicago', 'Boston']
}
df = pd.DataFrame(users)
print(df)

#Selecting a column
print("Selecting a column")
print(df.name)
print(df["age"])

#Selecting multiple columns
print("Selecting multiple columns")
print(df[["name", "city"]])

#Selecting rows
print("Selecting rows")
print(df.loc[0]) # returned as a dataframe

#Selecting rows by condition
print("Selecting rows by condition")
print(df["age"] > 30) # returned boolen values
data = df["age"] > 30
print(df[data]) # returned as a dataframe
#or
print(df[df["age"] > 30])

# adding new column to df
print("Adding new column to df")
df["Salary"] = [1000, 2000, 3000, 4000]
print(df)


# Create a sample dataframe
data = {
    'Animal': ['Dog', 'Cat', 'Dog', 'Cat', 'Dog', 'Cat', 'Dog', 'Cat'],
    'Age': [2, 3, 3, 2, 1, 2, 3, 1],
    'Weight': [10, 15, 12, 12, 10, 13, 12, 10]
}

df = pd.DataFrame(data)

# Group the data by the 'Animal' column
grouped = df.groupby('Animal')

# Now you can perform operations on these groups
print(grouped.mean())
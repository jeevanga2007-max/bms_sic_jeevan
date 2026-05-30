import pandas as pd

df = pd.DataFrame({

    "marks": [10, 20, 30, 40]

})

total = df["marks"].sum()

print(total)
print (df)
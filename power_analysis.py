import pandas as pd

data = {
    "name": ["Goku", "Vegeta", "Gohan", "Piccolo", "Trunks", "Frieza"],
    "power_level": [9000, 8500, 7000, 6500, 7200, 12000],
    "age": [35, 40, 25, 45, 24, 70],
    "race": ["Saiyan", "Saiyan", "Saiyan", "Namekian", "Saiyan", "Alien"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nAverage Power Level by Race:")
print(df.groupby("race")["power_level"].mean())

print("\nTop 3 Strongest Fighters:")
print(df.sort_values(by="power_level", ascending=False).head(3))
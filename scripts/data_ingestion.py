import pandas as pd
from pathlib import Path

DATA_FOLDER = Path("../data/raw")

for file in DATA_FOLDER.glob("*.csv"):

    print("\n" + "=" * 60)
    print(f"Dataset: {file.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)
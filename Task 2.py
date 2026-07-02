import pandas as pd
import os

# Function to process CSV file
def process_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        print("\nOriginal Data:")
        print(df.head())

        # Data Cleaning
        df.drop_duplicates(inplace=True)
        df.fillna("Unknown", inplace=True)

        # Data Transformation
        df.columns = [col.strip().title() for col in df.columns]

        if "Age" in df.columns:
            df["Age"] = pd.to_numeric(df["Age"], errors="coerce").fillna(0).astype(int)

        # Save cleaned data
        output_file = "cleaned_data.csv"
        df.to_csv(output_file, index=False)

        print(f"\nCleaned data saved as '{output_file}'")

    except Exception as e:
        print("Error:", e)


# Function to process JSON file
def process_json(file_path):
    try:
        df = pd.read_json(file_path)

        print("\nOriginal Data:")
        print(df.head())

        # Data Cleaning
        df.drop_duplicates(inplace=True)
        df.fillna("Unknown", inplace=True)

        # Data Transformation
        df.columns = [col.strip().title() for col in df.columns]

        if "Age" in df.columns:
            df["Age"] = pd.to_numeric(df["Age"], errors="coerce").fillna(0).astype(int)

        # Save cleaned data
        output_file = "cleaned_data.json"
        df.to_json(output_file, orient="records", indent=4)

        print(f"\nCleaned data saved as '{output_file}'")

    except Exception as e:
        print("Error:", e)


# Main Program
print("===== Data Processing System =====")
print("1. Process CSV File")
print("2. Process JSON File")

choice = input("Enter your choice (1/2): ")

file_path = input("Enter file path: ")

if not os.path.exists(file_path):
    print("File not found!")
else:
    if choice == "1":
        process_csv(file_path)
    elif choice == "2":
        process_json(file_path)
    else:
        print("Invalid choice!")

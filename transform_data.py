import pandas as pd

def transform_data(input_file, output_file):
    """
    Performs a simple data transformation on a movie dataset.
    
    Args:
        input_file (str): The path to the raw movie data CSV file.
        output_file (str): The path where the transformed data will be saved.
    """
    print("Starting data transformation...")
    
    try:
        # Read the raw data from the CSV file
        df = pd.read_csv(input_file)
        
        # --- Transformation Steps ---
        # 1. Fill missing values in a "rating" column with a default value (e.g., 0)
        df['rating'] = df['rating'].fillna(0)
        
        # 2. Convert a 'release_year' column to an integer type
        df['release_year'] = df['release_year'].astype(int)
        
        # You can add more transformation steps here, like:
        # - Fixing date formats
        # - Removing duplicate rows
        # - Creating new calculated columns
        
        print("Transformation complete. Saving cleaned data...")
        
        # Save the transformed data to a new CSV file
        df.to_csv(output_file, index=False)
        
        print(f"Data successfully saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with your file names
transform_data('movies.csv', 'transformed_movies.csv')
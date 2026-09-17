# ==============================================================================
# NASA EXOPLANET ARCHIVE - DATA CLEANING & PREPARATION PIPELINE
# ==============================================================================
# This script processes raw NASA exoplanet archive data, filters it to the 29
# core columns, performs a robust two-stage median imputation for missing data,
# converts physical units, and exports a pristine dataset optimized for Power BI.
# ==============================================================================

import os
import pandas as pd
import numpy as np

def run_cleaning_pipeline(input_path='nasa_exoplanets.csv', output_path='cleaned_exoplanets.csv'):
    print("Starting data cleaning pipeline...")
    
    # 1. Load the raw dataset, skipping NASA's comment metadata lines starting with '#'
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' not found. Please place it in the same directory.")
        
    df = pd.read_csv(input_path, comment='#')
    print(f"Raw dataset loaded. Initial Shape: {df.shape[0]} rows, {df.shape[1]} columns.")
    
    # 2. Trim dataset to the 29 core visualization columns
    core_columns = [
        'pl_name', 'hostname', 'sy_snum', 'sy_pnum', 'sy_mnum', 'discoverymethod', 
        'disc_year', 'disc_facility', 'pl_orbper', 'pl_orbsmax', 'pl_rade', 'pl_radj', 
        'pl_bmasse', 'pl_bmassj', 'pl_bmassprov', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 
        'st_spectype', 'st_teff', 'st_rad', 'st_mass', 'st_met', 'st_metratio', 
        'st_logg', 'ra', 'dec', 'sy_dist', 'sy_gaiamag'
    ]
    df = df[core_columns].copy()
    print("Column trimming completed. Filtered to 29 core columns.")
    
    # 3. Remove duplicate rows (if any)
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_rows - len(df)
    print(f"Duplicates removed: {duplicates_removed} rows.")
    
    # 4. Separate columns by data type for structured imputation
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    # 5. Robust Two-Stage Imputation for Numeric Columns
    # Stage 1: Impute using median of the respective 'discoverymethod' group
    # (This preserves physical astronomical relationships: e.g. transit planets are typically smaller/closer)
    for col in numeric_cols:
        group_medians = df.groupby('discoverymethod')[col].transform('median')
        df[col] = df[col].fillna(group_medians)
        
        # Stage 2: Global median fallback for any remaining nulls (if entire discovery method group was null)
        global_median = df[col].median()
        if not pd.isna(global_median):
            df[col] = df[col].fillna(global_median)
        else:
            df[col] = df[col].fillna(0) # Ultimate fallback
            
    # 6. Fill categorical columns missing values with 'Unknown'
    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown")
    print("Missing value imputation completed successfully (0 null values remaining).")
    
    # 7. Type casting - ensure Discovery Year is integer
    df['disc_year'] = df['disc_year'].astype(int)
    
    # 8. Unit conversion - Convert distance from Parsecs to Light Years (1 Parsec = 3.26156 Light Years)
    # This makes the public-facing dashboard titles and axis labels much more intuitive
    df['sy_dist'] = df['sy_dist'] * 3.26156
    print("Unit conversion (Parsecs -> Light Years) and type casting completed.")
    
    # 9. Rename all 29 columns to clear, human-readable names for Power BI compatibility
    rename_dict = {
        'pl_name': 'Planet_Name',
        'hostname': 'Host_Star_Name',
        'sy_snum': 'Number_of_Stars',
        'sy_pnum': 'Number_of_Planets',
        'sy_mnum': 'Number_of_Moons',
        'discoverymethod': 'Discovery_Method',
        'disc_year': 'Discovery_Year',
        'disc_facility': 'Discovery_Facility',
        'pl_orbper': 'Orbital_Period_Days',
        'pl_orbsmax': 'Orbital_Distance_AU',
        'pl_rade': 'Planet_Radius_Earth_Units',
        'pl_radj': 'Planet_Radius_Jupiter_Units',
        'pl_bmasse': 'Planet_Mass_Earth_Units',
        'pl_bmassj': 'Planet_Mass_Jupiter_Units',
        'pl_bmassprov': 'Mass_Measurement_Type',
        'pl_orbeccen': 'Orbit_Eccentricity',
        'pl_insol': 'Insolation_Flux_Earth_Units',
        'pl_eqt': 'Equilibrium_Temperature_K',
        'st_spectype': 'Star_Spectral_Type',
        'st_teff': 'Star_Temperature_K',
        'st_rad': 'Star_Radius_Solar_Units',
        'st_mass': 'Star_Mass_Solar_Units',
        'st_met': 'Star_Metallicity',
        'st_metratio': 'Star_Metallicity_Ratio',
        'st_logg': 'Star_Surface_Gravity',
        'ra': 'Right_Ascension_Deg',
        'dec': 'Declination_Deg',
        'sy_dist': 'Distance_From_Earth_Light_Years',
        'sy_gaiamag': 'Star_Gaia_Magnitude'
    }
    df.rename(columns=rename_dict, inplace=True)
    print("Columns renamed to human-readable format.")
    
    # 10. Export pristine dataset
    df.to_csv(output_path, index=False)
    print(f"Pristine dataset successfully exported to '{output_path}'!")
    print(f"Final dataset shape: {df.shape[0]} rows, {df.shape[1]} columns.")

if __name__ == '__main__':
    run_cleaning_pipeline()

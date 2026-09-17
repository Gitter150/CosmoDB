# 🌌 Exoplanet Explorer: NASA Archive Intelligence Dashboard

A full-stack data analytics project that transforms raw NASA Exoplanet Archive data into an interactive, dark-themed Power BI dashboard. The pipeline spans Python-based data cleaning and imputation through to a 6-chart visual intelligence console built in Power BI.

![Dashboard Preview](Screenshot%202026-05-29%20160701.png)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Dashboard Highlights](#dashboard-highlights)
- [Project Structure](#project-structure)
- [Data Pipeline](#data-pipeline)
- [Dataset Schema](#dataset-schema)
- [Getting Started](#getting-started)
- [Technologies Used](#technologies-used)
- [Data Source](#data-source)

---

## Overview

This project analyses **6,291 confirmed exoplanets** from the NASA Exoplanet Archive. A Python cleaning pipeline processes the raw archive export, performs robust two-stage median imputation, converts units, and renames columns to human-readable labels. The cleaned dataset feeds a Power BI dashboard featuring six coordinated visualizations with interactive slicers for discovery year, host star type, and distance from Earth.

---

## Dashboard Highlights

The dashboard is built on a pure black canvas (`#000000`) with a neon-cyan and cosmic-purple accent palette. It includes:

| # | Visualization | Insight |
|---|---|---|
| 1 | **Cosmic Proximity vs Thermal Habitability** (Scatter) | Plots equilibrium temperature against distance on a logarithmic light-year scale, colored by habitability index |
| 2 | **Volumetric Cataloging by Planetary Gravity Class** (Treemap) | Breaks down planet counts across gravity classifications |
| 3 | **System Architectures: Multi-Planet Frequency** (Clustered Bar) | Reveals how common multi-planet star systems are |
| 4 | **The Telescope Space Race: Top 10 Facilities** (Funnel) | Ranks the top 10 discovery facilities by confirmed planet count |
| 5 | **Celestial Map: Spatial Coordinates** (Scatter) | Maps Right Ascension vs Declination to visualize telescope survey corridors |
| 6 | **Technological Shifts: Discovery Method Proportions** (Stacked Area) | Shows the transition from radial velocity to transit photometry over time |

**Interactive Filters:** Discovery Year range slider, Host Star Type selector, and Distance From Earth range slicer.

**KPI Cards:** Habitable Worlds count, Total Planets, and Unique Star Systems.

---

## Project Structure

```
POWER BI CosmoDB/
│
├── PSCompPars_2026.05.28_03.54.55.csv   # Raw full export from NASA Exoplanet Archive
├── nasa_exoplanets.csv                   # Working raw dataset (29-column subset source)
├── cleaned_exoplanets.csv                # Cleaned & imputed output (Power BI data source)
│
├── clean_data.py                         # Standalone Python cleaning pipeline script
├── DataCleaner.ipynb                     # Jupyter Notebook with step-by-step cleaning & reports
│
├── Dashboard.pbix                        # Power BI dashboard file
├── instructions.md                       # Detailed chart build instructions for Power BI
│
├── Screenshot 2026-05-29 160701.png      # Dashboard preview screenshot
└── README.md                             # This file
```

---

## Data Pipeline

The cleaning pipeline (`clean_data.py` / `DataCleaner.ipynb`) performs the following steps:

```
Raw NASA CSV (6,291 rows × 100+ columns)
        │
        ▼
  1. Load & skip NASA comment headers (#)
        │
        ▼
  2. Trim to 29 core visualization columns
        │
        ▼
  3. Remove duplicate rows
        │
        ▼
  4. Two-Stage Median Imputation
     ├── Stage 1: Group median by Discovery Method
     └── Stage 2: Global median fallback
        │
        ▼
  5. Fill categorical nulls with "Unknown"
        │
        ▼
  6. Type casting (Discovery Year → int)
        │
        ▼
  7. Unit conversion (Parsecs → Light Years × 3.26156)
        │
        ▼
  8. Rename all columns to human-readable labels
        │
        ▼
  Cleaned CSV (6,291 rows × 29 columns, 0 nulls)
```

### Why Two-Stage Imputation?

Transit-discovered planets tend to be smaller and closer than radial-velocity-discovered planets. Grouping by discovery method before imputing preserves these real astronomical relationships rather than flattening them with a single global median.

---

## Dataset Schema

The cleaned dataset contains **29 columns** organized into four categories:

### Planet Properties
| Column | Description | Unit |
|---|---|---|
| `Planet_Name` | IAU planet designation | — |
| `Planet_Radius_Earth_Units` | Planetary radius | R⊕ |
| `Planet_Radius_Jupiter_Units` | Planetary radius | R♃ |
| `Planet_Mass_Earth_Units` | Planetary mass | M⊕ |
| `Planet_Mass_Jupiter_Units` | Planetary mass | M♃ |
| `Mass_Measurement_Type` | Mass or Msini | — |
| `Orbital_Period_Days` | Orbital period | days |
| `Orbital_Distance_AU` | Semi-major axis | AU |
| `Orbit_Eccentricity` | Orbital eccentricity | 0–1 |
| `Insolation_Flux_Earth_Units` | Stellar energy received | S⊕ |
| `Equilibrium_Temperature_K` | Equilibrium temperature | K |

### Host Star Properties
| Column | Description | Unit |
|---|---|---|
| `Host_Star_Name` | Star name / catalog ID | — |
| `Star_Spectral_Type` | MK spectral classification | — |
| `Star_Temperature_K` | Effective temperature | K |
| `Star_Radius_Solar_Units` | Stellar radius | R☉ |
| `Star_Mass_Solar_Units` | Stellar mass | M☉ |
| `Star_Metallicity` | Metallicity [Fe/H] | dex |
| `Star_Metallicity_Ratio` | Metallicity ratio type | — |
| `Star_Surface_Gravity` | Surface gravity (log g) | cgs |
| `Star_Gaia_Magnitude` | Gaia G-band magnitude | mag |

### System & Discovery
| Column | Description | Unit |
|---|---|---|
| `Number_of_Stars` | Stars in the system | count |
| `Number_of_Planets` | Planets in the system | count |
| `Number_of_Moons` | Moons in the system | count |
| `Discovery_Method` | Detection technique | — |
| `Discovery_Year` | Year of discovery | year |
| `Discovery_Facility` | Observatory / spacecraft | — |

### Coordinates & Distance
| Column | Description | Unit |
|---|---|---|
| `Right_Ascension_Deg` | Sky longitude | degrees |
| `Declination_Deg` | Sky latitude | degrees |
| `Distance_From_Earth_Light_Years` | Distance to the system | ly |

---

## Getting Started

### Prerequisites

- **Python 3.8+** with `pandas` and `numpy`
- **Power BI Desktop** (free, Windows only)

### Run the Cleaning Pipeline

```bash
# Option A: Run the standalone script
python clean_data.py

# Option B: Open the Jupyter Notebook for step-by-step execution
jupyter notebook DataCleaner.ipynb
```

The script reads `nasa_exoplanets.csv` and outputs `cleaned_exoplanets.csv`.

### Open the Dashboard

1. Open `Dashboard.pbix` in Power BI Desktop.
2. If prompted, point the data source to `cleaned_exoplanets.csv` in this directory.
3. Use the slicers on the left panel to filter by discovery year, host star type, and distance.

---

## Technologies Used

| Tool | Purpose |
|---|---|
| **Python 3** | Data cleaning, imputation, and transformation |
| **pandas / NumPy** | DataFrame manipulation and numerical operations |
| **Jupyter Notebook** | Interactive, documented data cleaning walkthrough |
| **Power BI Desktop** | Interactive dashboard design and visualization |
| **NASA Exoplanet Archive** | Primary data source |

---

## Data Source

The raw dataset was exported from the [NASA Exoplanet Archive — Planetary Systems Composite Parameters](https://exoplanetarchive.ipac.caltech.edu/) on **May 28, 2026**. The archive is maintained by the NASA Exoplanet Science Institute (NExScI) at Caltech under contract with NASA.

---

<p align="center">
  Built with 🔭 curiosity and 📊 data
</p>

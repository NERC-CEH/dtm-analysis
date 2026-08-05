[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21297014.svg)](https://doi.org/10.5281/zenodo.21297014)


Initially authored by Rafa Barbedo (ex-UKCEH): this repo is a fork of https://github.com/gisflw/dtm-analysis.git. FDRI now maintains this repo.

# DTM & DSM Analysis  
This repository contains Jupyter notebooks and scripts for processing  
high-resolution Digital Terrain Models (DTM) and Digital Surface Models (DSM).

They demonstrate the use of merged 1m LiDAR data for England and Wales that is available at:
- The Environmental Information Data Centre (EIDC) (DOI): [COMING SOON] **Please cite here when using the dataset.**
- JASMIN public store
Note these are large files: >200GB each. For users only needing a small region, it's more efficient to programmatically subset the files using a shape file.
The notebooks demonstrate how to flexibly subset them. **You do not need to download the data from EIDC before running the notebooks.**

## 📂 Folder Structure
- **data/** → Raw & processed raster data (i.e. where output goes when running the notebook.)
- **notebooks/** → Jupyter notebooks for terrain analysis. **You need to run notebook 01 to get data**.  
- **src/** → Python & shell scripts for processing  

## 📂 List of Notebooks
| Notebook | Description |
|----------|-------------|
| [Notebook 01: Catchment Digital Terrain Models](https://github.com/NERC-CEH/dtm-analysis/blob/main/notebooks/01_extract_dtm_dsm.ipynb) | High-resolution terrain and elevation models from FDRI LiDAR surveys. |
| [Notebook 02: Catchment Terrain Analysis](https://github.com/NERC-CEH/dtm-analysis/blob/main/notebooks/02_terrain_analysis.ipynb) | Calculate and visualise slope, aspect, and other terrain characteristics. |
| [Notebook 03: Floodplain Micro-topography](https://github.com/NERC-CEH/dtm-analysis/blob/main/notebooks/03_hydrological_analysis.ipynb) | Explore fine-scale floodplain features, including channels and depressions. |
| [Notebook 04: Riparian Canopy Height](https://github.com/NERC-CEH/dtm-analysis/blob/main/notebooks/04_canopy_analysis.ipynb) | Analyse the height and structure of riverside trees and vegetation. |

## 🙋 Self-service to get additional data to run notebooks
- (notebook 01) You will need a shape file of a region within England and Wales. For example, you can download the boundary of a NRFA catchment [here](https://nrfa.ceh.ac.uk/data/search). Click on a station >> Catchment info tab >> Download catchment boundary.
- (notebook 03) You will need a shape file of water courses to verify your results. You could use the [OS Open Rivers Water courses dataset](https://www.ordnancesurvey.co.uk/products/os-open-rivers).

## 🚀 Getting Started  
To set up, install dependencies and run the notebooks.

To find more resources, go to https://fdri.org.uk

<img width="290" height="96.25" alt="download" src="https://github.com/user-attachments/assets/d7db24ad-0831-4b6a-87a1-11405af7fe20" />

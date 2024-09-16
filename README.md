# PALM_TREEs_heat_stress

Hello. This code will enable you to apply Lu and Romps' heat stress exposure metric to your study region.
Lu and Romps' (2022) algorithm is available in Python, R, and Fortran code at https://romps.berkeley.edu/papers/pubs-2020-heatindex.html#:~:text=To%20extend%20the%20heat%20index,observable%20measure%20of%20physiological%20stress.

To run the code, you will need some spatial data. I used ERA5-Land data at the hourly level for the Limpopo province of South Africa. This data can be acquired using step 1 below.
The following files need to be executed in order. 

# Historical heat stress exposure
- Step 1: Get your data
  - Step 1.1: Run the 'download_hourly_ERA5_data.py' file available at https://github.com/CLARE-PALM-TREEs/Download_ERA5_data
    - You will need a Copernicus (CDS) account and to specify your CDS API Key. See the following link for a tutorial: https://ecmwf-projects.github.io/copernicus-training-c3s/cds-tutorial.html
    - You can easily find the coordinate bounds using this helpful tool: https://boundingbox.klokantech.com/
  - Step 1.2: Acquire shapefiles for your region
    - Put these files in the 'shapefiles' folder
    - I acquired files for Limpopo Province from  https://data.humdata.org/dataset/cod-ab-zaf
- Step 2: Open _basic_info.py_ and change the file paths to your own
  - As you run each file below, you will notice that more files are added to _basic_info.py_. This was set to prevent you from having to repeatedly type in the filepaths you need each time you open a new file
- Step 3: Run _creating_and_concatenating_cubes.ipynb_
  - Creates Iris "cubes" from the individually requested files from Step 1
- Step 4: Run _cube_creation_frontend.ipynb_
  - Creates further files from the step 3 file required for further analyses
- Step 5: Run _lu_and_romps_algorithm.ipynb_
  - Creates the Lu and Romps (2022) cube
- Step 7: Run _data_analysis_frontend.ipynb_
  - Creates spatial plots and time series plots for historical data

# Projected heat stress exposure
- Step 1: Acquire projections data
  - Ask the Met Office for this for tas, rh, and when run on Lu and Romps (2022)
  - Organise the projections data into the _projections_data_ folder based on whether CMIP6 or CORDEX and time period
  - Alter the projections portion of the _basic_info.py_ file
-Step 2: 
- Step 2: Run _calculating_scaling_factor.ipynb_
  - Creates a 'scaling factor' to be used in step 9. This is necessary to create as the maximum daily heat indices are estimated with daily maximum air temperature and minimum relative humidity, while available projections only allow the creation of mean daily heat indices (a function of daily mean air temperature and mean relative humidity)
- Step 3: Run _projections.ipynb_ after changing the filepaths to suit you
- Step 4: Run _rh_projections_analysis.ipynb_ and _tas_projections_analysis_ipynb_ to understand what the models in step 9 predict for air temperature and humidity, and thus why the projected heat indices may differ between models

**Useful tips**
- Don't worry about the equivalent "backend" files unless you'd like to make some changes to the outputs
- The code is split into many files to prevent crashing regardless of device capabilities. If files still crash, batch process data by extracting subsets of the cubes and then concatenating them. See step 6's code for an example of how to do this.


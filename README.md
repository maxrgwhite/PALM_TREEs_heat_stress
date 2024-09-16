# PALM_TREEs_heat_stress

Hello. This code will enable you to apply Lu and Romps' heat stress exposure metric to your study region.
Lu and Romps' (2022) algorithm is available in Python, R, and Fortran code at https://romps.berkeley.edu/papers/pubs-2020-heatindex.html#:~:text=To%20extend%20the%20heat%20index,observable%20measure%20of%20physiological%20stress.

To run the code, you will need some spatial data. I used ERA5-Land data at the hourly level for the Limpopo province of South Africa. This data can be acquired using step 1 below.
The following files need to be executed in order. 

If you are uninterested in future heat stress, skip steps 1.2, 8, and 9.

- Step 1: Get your data
  - Step 1.1: Open the *data_requests* file and choose to download either ERA5 or ERA5–Land data.
    - You will need a Copernicus (CDS) account and to specify your CDS API Key. See the following link for a tutorial: https://ecmwf-projects.github.io/copernicus-training-c3s/cds-tutorial.html
    - You can easily find the coordinate bounds using this helpful tool: https://boundingbox.klokantech.com/.
  - Step 1.2: Acquire projections data (assuming projections are of interest)
    - Ask the Met Office for this.
    - Organise the projections data into the _projections_data_ folder based on whether CMIP6 or CORDEX and time period
  - Step 1.3: Acquire shapefiles for your region. I acquired mine for Limpopo Province from  https://data.humdata.org/dataset/cod-ab-zaf.
- Step 2: Open _basic_info.py_ and change the file paths to your own
  - As you run each file below, you will notice that more files are added to _basic_info.py_. This was set to prevent you from having to repeatedly type in the filepaths you need each time you open a new file.
- Step 3: Run _creating_and_concatenating_cubes.ipynb_
  - Creates Iris "cubes" from the individually requested files from Step 1.
- Step 4: Run _cube_creation_frontend.ipynb_
  - Creates further files from the step 3 file required for further analyses
- Step 5: Run _lu_and_romps_algorithm.ipynb_
  - Creates the Lu and Romps (2022) cube
- Step 7: Run _data_analysis_frontend.ipynb_
  - Creates spatial plots and time series plots for historical data
- Step 8: Run _calculating_scaling_factor.ipynb_
  - Creates a 'scaling factor' to be used in step 9. This is necessary to create as the maximum daily heat indices are estimated with daily maximum air temperature and minimum relative humidity, while available projections only allow the creation of mean daily heat indices (a function of daily mean air temperature and mean relative humidity).
- Step 9: Run _projections.ipynb_ after changing the filepaths to suit you.

**Useful tips**
- Don't worry about the equivalent "backend" files unless you'd like to make some changes to the outputs
- The code is split into many files to prevent crashing regardless of device capabilities. If files still crash, batch process data by extracting subsets of the cubes and then concatenating them. See step 6's code for an example of how to do this.


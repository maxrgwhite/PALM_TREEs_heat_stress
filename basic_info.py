############### CHANGE FILEPATHS ###############
directory_filepath = '/Users/maxwhite/Desktop/Lu_and_Romps' # Path to the directory where the files are stored
data_folder = '/Users/maxwhite/Desktop/Lu_and_Romps/Data' # Path to the directory where all data are stored (you may need to create this)
tas_files = '/Users/maxwhite/Desktop/Lu_and_Romps/Data/Limpopo/ERA5-Land/tas' # Path to the directory where air temperature files are stored (this should be in the 'data_folder'!)
td_files = '/Users/maxwhite/Desktop/Lu_and_Romps/Data/Limpopo/ERA5-Land/td' # Path to the directory where dew point temperature files are stored (this should be in the 'data_folder'!)

shapefile_folder = '/Users/maxwhite/Desktop/Lu_and_Romps/shapefiles'
shapefile_file = '/Users/maxwhite/Desktop/Lu_and_Romps/shapefiles/Limpopo_Boundaries.geojson'

location_name = 'Limpopo Province' # Name of your region of study. Necessary for plot titles
start_year = 1950 # First year included in your data
end_year = 2024 # Lasy year included in your data

# If using projections, change filepaths
projections_cmip6_baseline_heat_index = '/Users/maxwhite/Documents/Met_Office_Work/Heat_index_Algorithms/Python_code/Projections_data/Organised/CMIP6_ERA5_heat_index_1995_2014.nc' # Path to the CMIP6 basline projections data
projections_cordex_baseline_heat_index = '/Users/maxwhite/Documents/Met_Office_Work/Heat_index_Algorithms/Python_code/Projections_data/Organised/CORDEX_ERA5_heat_index_1995_2014.nc' # Path to the CORDEX basline projections data

projections_cmip6_baseline_tas = '/Users/maxwhite/Desktop/Lu_and_Romps/projections_data/tas_and_rh/tas/CMIP6/ERA5_daily_tas_hist_1995-2014.nc'
projections_cordex_baseline_tas = '/Users/maxwhite/Desktop/Lu_and_Romps/projections_data/tas_and_rh/tas/CORDEX/ERA5_daily_tas_hist_1995-2014.nc'

projections_cmip6_baseline_rh = '/Users/maxwhite/Desktop/Lu_and_Romps/projections_data/tas_and_rh/rh/CMIP6/ERA5_daily_hurs_hist_1995-2014.nc'
projections_cordex_baseline_rh = '/Users/maxwhite/Desktop/Lu_and_Romps/projections_data/tas_and_rh/rh/CORDEX/ERA5_daily_hurs_hist_1995-2014.nc'

############### DO NOT CHANGE ###############
projections_data_folder = directory_filepath + '/projections_data'
projections_cmip6_folder = directory_filepath + '/projections_data/CMIP6'
projections_cordex_folder = directory_filepath + '/projections_data/CORDEX'

scaled_projections_data_folder = projections_data_folder + '/scaled'
scaled_projections_cmip6_baseline = scaled_projections_data_folder + '/CMIP6_ERA5_heat_index_1995_2014.nc'
scaled_projections_cordex_baseline = scaled_projections_data_folder + '/CORDEX_ERA5_heat_index_1995_2014.nc'

tas_projections_data_folder = directory_filepath + '/projections_data/tas_and_rh/tas'
rh_projections_data_folder = directory_filepath + '/projections_data/tas_and_rh/rh'
########## Further filepaths will appear here as you run the code #########

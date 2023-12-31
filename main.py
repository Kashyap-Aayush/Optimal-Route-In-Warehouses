import numpy as np
import pandas as pd
from ast import literal_eval
import scipy
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

#import dataset
df_orderlines=pd.read_csv('df_lines.csv')
df_orderlines

# Function 
def simulation_wave(y_low, y_high, orders_number, df_orderlines, list_wid, list_dst, list_route, list_ord):

    # Create variable to store total distance
    distance_route = 0 
    # Create waves
    df_orderlines, waves_number = orderlines_mapping(df_orderlines, orders_number)
    # Loop all waves
    for wave_id in range(waves_number):
        # Listing of all locations for this wave 
        list_locs, n_locs = locations_listing(df_orderlines, wave_id)
        # Results
        wave_distance, list_chemin = create_picking_route(Loc_orn, list_locs, y_low, y_high)
        distance_route = distance_route + wave_distance
        # Append lists of results 
        list_wid.append(wave_id)
        list_dst.append(wave_distance)
        list_route.append(list_chemin)
        list_ord.append(orders_number)

    return list_wid, list_dst, list_route, list_ord, distance_route
#for plotting graph
list_xaxis=[]
list_yaxis=[]
# Test several values of orders per wave
for orders_number in range(1, 20):
    list_wid, list_dst, list_route, list_ord, distance_route = simulation_wave(y_low, y_high, orders_number, df_orderlines, list_wid, list_dst, list_route, list_ord)
    print("Total distance covered for {} orders/wave: {:,} m".format(orders_number, distance_route))
    
    list_xaxis.append(orders_number)
    
    list_yaxis.append(distance_route)

# Create df for results
df_results = pd.DataFrame({'Wave_Number': list_wid,
               'Distance_Route': list_dst,
               'Chemins': list_route,
               'OrderPerWave': list_ord})

print(df_results.head())

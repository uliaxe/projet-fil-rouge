import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Charger les données
carac = pd.read_csv('donnee_accident/Donnee_2005/caracteristiques-2005.csv', sep=';')
lieux = pd.read_csv('donnee_accident/Donnee_2005/lieux-2005.csv', sep=';')

# Fusionner sur le numéro d'accident
accidents = pd.merge(carac, lieux, on='Num_Acc')

# Garder uniquement l'année 2005 (normalement déjà le cas)
accidents_2005 = accidents

# Les colonnes 'lat' et 'long' sont en dixièmes de microdegré, il faut les convertir
accidents_2005['latitude'] = accidents_2005['lat'] / 1e6
accidents_2005['longitude'] = accidents_2005['long'] / 1e6

# Charger la carte de la France
france = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
france = france[france['name'] == 'France']

# Convertir en GeoDataFrame
gdf_accidents = gpd.GeoDataFrame(
    accidents_2005,
    geometry=gpd.points_from_xy(accidents_2005.longitude, accidents_2005.latitude),
    crs="EPSG:4326"
)

# Afficher la carte
fig, ax = plt.subplots(figsize=(8, 10))
france.plot(ax=ax, color='white', edgecolor='black')
gdf_accidents.plot(ax=ax, markersize=1, color='red', alpha=0.5)
plt.title('Carte des accidents en France en 2005')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
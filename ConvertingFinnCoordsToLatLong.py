import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

df = pd.read_csv("data-2014-2021.csv")
df.rename(columns={"x": "lat", "y": "lon"}, inplace=True)

def convert_to_wgs84_decimal(easting, northing, input_crs):
    gdf = gpd.GeoDataFrame(
        geometry=[Point(easting, northing)],
        crs=input_crs
    )
    gdf = gdf.to_crs("EPSG:4326")  # Convert to WGS84
    lat = round(gdf.geometry.y.values[0], 4)
    lon = round(gdf.geometry.x.values[0], 4)
    return lat, lon

input_crs = "EPSG:3067"

df[['lat', 'lon']] = df.apply(
    lambda row: pd.Series(convert_to_wgs84_decimal(row['lon'], row['lat'], input_crs)),
    axis=1
)

df.to_csv("data-2014-2021-fixed.csv", index=False)

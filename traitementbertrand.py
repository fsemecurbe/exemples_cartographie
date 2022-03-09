import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine


db_connection_url = "postgresql://sco_teruti:B1T]KdIQ!1koNLBm@stats-prod-postgres-8.zsg.agri:4000/teruti_2022"
engine = create_engine(db_connection_url)

sql = 'SELECT * FROM teruti_090.grille_250'
points = gpd.read_postgis (sql , engine , geom_col ='geom')
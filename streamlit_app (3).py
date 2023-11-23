import pandas as pd
import plotly.express as px
import streamlit as st

df_copy2=df_copy1.copy()

fig = px.scatter_mapbox(df_copy2, lat="Latitude", lon="Longitude_x",color="Life expectancy", size="Population",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=20,zoom=12)
#fig.show()
st.plotly_chart(fig, use_container_width=True)

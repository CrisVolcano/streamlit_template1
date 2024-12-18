import streamlit as st
import leafmap.foliumap as leafmap
from matplotlib.colors import ListedColormap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/CrisVolcano/streamlit_template1>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Visor de raster propios prueba 1")

# Colores para valores específicos
colors = ['white', '#7a982f', 'green', 'yellow', 'orange', 'blue', 'red']
#custom_cmap = ListedColormap(colors)

legend = {
    "No Data": "white",
    "Water": "blue",
    "Vegetation": "green",
    "Soil": "yellow",
    "Urban": "orange",
    "Burned Area": "red",
    "Other": "purple",
}


with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        clasi_uso = "https://github.com/CrisVolcano/streamlit_template1/releases/download/tag-1/2001_RF.tif"
        #after = "https://github.com/CrisVolcano/streamlit_template1/releases/download/tag-1/2001_RF.tif"

        # Añadir capas raster con colormap personalizado
        m.add_raster(clasi_uso, bands=1, palette=colors, layer_name="Clasificacion")
       # m.add_raster(after, bands=1, palette=custom_cmap, layer_name="After")

       # m.split_map(
       #     left_layer= before, right_layer=after
       # )

       

m.to_streamlit(height=700)

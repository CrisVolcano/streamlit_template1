import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/CrisVolcano/streamlit_template1>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.gifer.com/embedded/download/zqE.gif"
st.sidebar.image(logo)

# Customize page title
st.title("Prueba de apps de Cristian Aguilar")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/CrisVolcano/streamlit_template1).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/CrisVolcano/streamlit_template1) or [use it as a template](https://github.com/CrisVolcano/streamlit_template1/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

# Opciones de mapas base
basemaps = {
    "OpenStreetMap": "OpenStreetMap",
    "Satellite": "SATELLITE",
    "Terrain": "TERRAIN",
    "ESRI Satellite": "ESRI_Imagery"
}

selected_basemap = st.sidebar.selectbox("Select a basemap", list(basemaps.keys()))

# Crear y mostrar el mapa
m = leafmap.Map(minimap_control=True)
m.add_basemap(basemaps[selected_basemap])
m.to_streamlit(height=500)

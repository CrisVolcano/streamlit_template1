import streamlit as st
import leafmap.foliumap as leafmap
import os
import xarray as xr


st.set_page_config(layout="wide")

# Información del proyecto en la barra lateral
markdown = """
A Streamlit map template  
<https://github.com/CrisVolcano/streamlit_template1>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Título de la aplicación
st.title("Split-panel Map for Raster Visualization")

# Ruta de los archivos raster
raster_dir = "raster"
raster1 = os.path.join(raster_dir, "20210124_VH.tiff")
raster2 = os.path.join(raster_dir, "20210124_VV.tiff")

# Verificación de la existencia de archivos
if not os.path.exists(raster1) or not os.path.exists(raster2):
    st.error("Error: Raster files not found. Please check the file paths.")
else:
    # Mostrar el código fuente si el usuario lo desea
    with st.expander("See source code"):
        with st.echo():
            # Crear un mapa dividido
            m = leafmap.Map()
            
            # Agregar el raster VH con rango de valores [0, 0.5]
            m.add_raster(
                raster1,
                layer_name="VH Polarization",
                vmin=0,
                vmax=0.1,
            )
            
            # Agregar el raster VV con rango de valores [0, 0.1]
            m.add_raster(
                raster2,
                layer_name="VV Polarization",
                vmin=0,
                vmax=0.5,
            )
            
            # Dividir el mapa con las dos capas
            m.split_map(
                left_layer="VH Polarization",
                right_layer="VV Polarization",
            )

            # Añadir leyenda personalizada
            m.add_legend(title="Raster Visualization", legend_dict={
                "VH Polarization": "blue",
                "VV Polarization": "green"
            })

    # Mostrar el mapa en Streamlit
    m.to_streamlit(height=700)

import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/CrisVolcano/streamlit_template1>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "https://github.com/CrisVolcano/streamlit_template1/releases/download/tag-1/2001_RF.tif"
        after = "https://github.com/CrisVolcano/streamlit_template1/releases/download/tag-1/2001_RF.tif"

        m.split_map(
            left_layer=before, right_layer= after
        )
      

m.to_streamlit(height=700)

import pandas as pd
import numpy as np
import os
import glob
import streamlit as st
from datetime import date
import warnings
# hide future warnings (caused by st_aggrid)
warnings.simplefilter(action='ignore', category=FutureWarning)

#set page layout and define basic variables
st.set_page_config(layout="wide", page_icon='⚡', page_title="SCM-Demand Forecasting")
path = os.path.dirname(__file__)
today = date.today()

# Create a sidebar navigation bar
st.sidebar.header("Navigation")
# Add links or options to the navigation bar
selected_page = st.sidebar.radio("Select a Page", ["All Sku-Regions", "Selected SKU-Regions", "Settings"])

if selected_page=='All Sku-Regions':
    

    # Get list of HTML files
    sku_ids_list = glob.glob('../plots/*.html')
    sku_ids = [sku.split('/')[2].split('_')[0] for sku in sku_ids_list]
    region_ids = ["_".join(sku.split('/')[-1].split('.')[0].split('_')[1:]) for sku in sku_ids_list]
    region_ids = list(set(region_ids))


    sku_dictionay = {
    }
    for sku_id in sku_ids:
        path_list = glob.glob('../plots/*.html')
        existing_sku = ["_".join(path.split('/')[-1].split('.')[0].split('_')[1:]) for path in path_list if sku_id in path]
        # print(existing_sku)
        sku_dictionay[sku_id] = existing_sku

    # Streamlit UI
    st.title("Interactive Plot for SKU-Regions")

    col1,col2 = st.columns(2)
    with col1:
        # Dropdowns for sku_id and region_id
        selected_sku_id = st.selectbox("Select sku_id:", list(sku_dictionay.keys()))
        st.write(f"Selected sku_id: {selected_sku_id}")
    with col2:
        selected_region_id = st.selectbox("Select region_id:", sku_dictionay[selected_sku_id])
        st.write(f"Selected region_id: {selected_region_id}")
        



    # Display the corresponding plot using IFrame
    if selected_sku_id and selected_region_id:
        plot_url = f"../plots/{selected_sku_id}_{selected_region_id}.html"
        with open(plot_url, 'r') as file:
            html_plot = file.read()
            st.components.v1.html(html_plot,height=800,width=1800,scrolling=False)
if selected_page=='Selected SKU-Regions':
    st.write('Selected SKU-Regions')
    # making meta information for the desboard
    sku_ids_list = glob.glob('../plots/*.html')
    sku_ids = [sku.split('/')[2].split('_')[0] for sku in sku_ids_list]
    region_ids = [ "_".join(sku.split('/')[-1].split('.')[0].split('_')[1:]) for sku in sku_ids_list]
    region_ids = list(set(region_ids))



    selected_skus = ['BE20196', 'BE20222', 'BE20090', 'BE20198', 'BE20191']
    selected_sku_ids = {}
    for sku_id in sku_ids:
        path_list = glob.glob('../plots/*.html')
        existing_sku = ["_".join(path.split('/')[-1].split('.')[0].split('_')[1:]) for path in path_list if sku_id in path]    
        if sku_id in selected_skus:
            selected_sku_ids[sku_id] = existing_sku

    
    
    # Streamlit UI
    st.title("Interactive Plot for SKU-Regions")

    col1,col2 = st.columns(2)
    with col1:
        # Dropdowns for sku_id and region_id
        selected_sku_id = st.selectbox("Select sku_id:", list(selected_sku_ids.keys()))
        st.write(f"Selected sku_id: {selected_sku_id}")
    with col2:
        selected_region_id = st.selectbox("Select region_id:", selected_sku_ids[selected_sku_id])
        st.write(f"Selected region_id: {selected_region_id}")
        



    # Display the corresponding plot using IFrame
    if selected_sku_id and selected_region_id:
        plot_url = f"../plots/{selected_sku_id}_{selected_region_id}.html"
        with open(plot_url, 'r') as file:
            html_plot = file.read()
            st.components.v1.html(html_plot,height=800,width=1800,scrolling=False)



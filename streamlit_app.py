import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go
from numpy import log, sqrt, exp  # Make sure to import these
import matplotlib.pyplot as plt
import seaborn as sns

#######################
# Page configuration
st.set_page_config(
    page_title="Create and Forcast Portfolio Performance",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")


# Sidebar for User Inputs
with st.sidebar:
    st.title("📊 Stock Portfolio Creator")
    st.write("`Created by:`")
    linkedin_url = "https://www.linkedin.com/in/maksym-malynovskyi-227541182/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Maksym Malynovskyi, London`</a>', unsafe_allow_html=True)




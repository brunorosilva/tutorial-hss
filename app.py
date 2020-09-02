import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("App exemplo")

st.markdown("Isso vai ser um bloco de texto")

df = pd.DataFrame({
    "Dados":np.random.normal(0, 1, 1000)
})

plt.plot(df.Dados)
st.pyplot()

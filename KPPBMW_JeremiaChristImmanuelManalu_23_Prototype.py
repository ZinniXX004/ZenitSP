# Import important libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os

# Showing event and my name
st.header("KPP BMW")
st.subheader("Nama : Jeremia Christ Immanuel Manalu")
st.subheader("BME 23")

# Accessing ECG data and display it in streamlit web
ecg1 = np.loadtxt('Data_ECG.txt', dtype = 'float')
ecg = ecg1[10 : 500]
plt.figure(figsize = (18, 8))
plt.plot(ecg, "green")
st.pyplot(plt) 

# Display 
Ndata1 = len(ecg1)
ECG1 = np.arange(Ndata1)
plt.plot(ECG1, ecg1)
st.pyplot(plt)
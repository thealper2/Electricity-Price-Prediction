import streamlit as st
import numpy as np
import pandas as pd
import pickle
import datetime
from datetime import date, timedelta

model = pickle.load(open("model.pkl", "rb"))

today = date.today()
default_date_yesterday = today - timedelta(days=1)
complition_date = st.date_input("Date of completion", default_date_yesterday)
fwp = st.number_input("ForecastWindProduction")
slea = st.number_input("SystemLoadEA")
smpea = st.number_input("SMPEA")
orkt = st.number_input("ORKTemperature")
orkw = st.number_input("ORKWindSpeed")
coi = st.number_input("CO2Intensity")
awp = st.number_input("ActualWindProduction")
slep = st.number_input("SystemLoadEP2")


if st.button("Predict"):
	day = complition_date.day
	month = complition_date.month
	test = np.array([[day, month, fwp, slea, smpea, orkt, orkw, coi, awp, slep]])
	res = model.predict(test)
	print(res)
	st.success("Prediction: " + str(res[0]))


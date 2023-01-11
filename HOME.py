import streamlit as st
import time
from streamlit.errors import DuplicateWidgetID

import functions

infos = functions.get_info()
todos = functions.get_apply()

st.title("Elevator using Application list")

st.subheader("Please use this web to apply for the usage of elevator.")

st.markdown(" ")

for info in infos:
    st.write(info, key=info)

st.markdown(":mega::mega::mega::mega::mega::mega::mega::mega::mega::mega::mega::mega::mega::mega::mega::mega:")

st.write(" ")

for total in todos:
    st.warning(total)
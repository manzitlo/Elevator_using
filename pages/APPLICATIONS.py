import streamlit as st
import time
import data_cleaning
from streamlit.errors import DuplicateWidgetID

import functions

todos = functions.get_apply()
clock = time.strftime("%b %d - %Y, %H:%M")


def add_apply():
    new_apply = st.session_state["new_apply"] + " floor"
    print(new_apply)
    todos.append(new_apply)
    functions.write_apply(todos)


def add_time():
    new_apply_time = f" -- at {st.session_state['new_apply_time']}" + " "
    print(new_apply_time)
    todos.append(new_apply_time)
    functions.write_apply(todos)


def add_peoples_number():
    new_peoples_number = f" ({st.session_state['new_peoples_number']} people)\n"
    print(new_peoples_number)
    todos.append(new_peoples_number)
    functions.write_apply(todos)


st.markdown('**please follow the instructions**, wish you could have a great day!')
st.markdown("The following checkbox is telling you which **:blue[floor]** we plan to **:red[stop]**")
st.markdown(
    ":pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil::pencil:")
st.write(" ")

cnt = 0
for index, apply in enumerate(todos):
    cnt += 1
    checkbox = st.checkbox(apply, key=cnt)
    if checkbox:
        todos.pop(index)
        functions.write_apply(todos)
        del st.session_state[apply]
        st.experimental_rerun()

# with st.expander("Typing floor number & pickup time. Press 'Enter'"):
col1, col2, col3 = st.columns([1.0, 1.5, 1.0])

with col1:
    st.text_input(label=" ", placeholder="Add your floor number",
                  on_change=add_apply, key='new_apply')

with col2:
    st.text_input(label=" ", placeholder="Add the detailed time",
                  on_change=add_time, key='new_apply_time')

with col3:
    st.text_input(label=" ", placeholder="Add how many people",
                  on_change=add_peoples_number, key='new_peoples_number')

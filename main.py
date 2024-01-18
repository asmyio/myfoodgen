import streamlit as st
import numpy as np

st.set_page_config(page_title="MY Food Generator", page_icon="🥥", layout="centered", initial_sidebar_state="auto", menu_items=None)
nasi_goreng = ["oil", "onion", "garlic", "paste", "eggs", "rice", "vegetables"]
available = []
missing = []

st.title("Malaysian Food Generator (BETA)")

# Insert a chat message container.
with st.chat_message("user", avatar="🥥"):
    st.write("Welcome to Malaysian Food Generator")

# Display a chat input widget.
prompt = st.chat_input("What's in your fridge")

if prompt:
    prompt = prompt.lower()
    with st.chat_message("user", avatar="🥥"):
        st.write(f"You have: {prompt}")
        for word in nasi_goreng:
            if word in prompt:
                available.append(word)
            else:
                missing.append(word)

        available = ", ".join(available)
        missing = ", ".join(missing)
        st.write(f'You can make nasi goreng with: {available}')
        st.write(f'You are missing: {missing}')
        

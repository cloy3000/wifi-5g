


import streamlit as st
import time

st.set_page_config(page_title="Wifi 5g Editor", page_icon=":tada:")


st.subheader("Welcome, lets boost your wifi!")

with st.container():
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""
    if "my_input_2" not in st.session_state:
        st.session_state["my_input_2"] = ""
    if "my_input_3" not in st.session_state:
        st.session_state["my_input_3"] = ""
    
    my_input = st.text_input("Please enter the name of your wifi router.", st.session_state["my_input"])
    my_input_2 = st.text_input("Please enter your region.", st.session_state["my_input_2"])
    my_input_3 = st.text_input("Enter your wifi passkey.",  st.session_state["my_input_3"])


    





    

    







    boost = st.button("Boost")
    if boost:
       
       if my_input.isalnum() and my_input_2.isalnum() and my_input_3.isalnum():
            my_input = str(my_input)
            my_input_2 = str(my_input_2)
            my_input_3 = str(my_input_3)
            print(my_input, my_input_2, my_input)
            with st.spinner('Initializing 5g Network...'):
                time.sleep(2)
                with st.spinner("Fetching data configuration..."):
                    time.sleep(4)
                    with st.spinner("Checking network availability..."):
                        time.sleep(6)
                        def do_something_slow():
                            for i in range(100):
                                time.sleep(0.1)
                                yield i 
                            
                        progress_text = "Processing data..."
                        my_bar = st.progress(0, text=progress_text)

                        for percent_complete in do_something_slow():
                            my_bar.progress(percent_complete + 1)

                        st.success("Success!")  
      
      
      
       else:
        st.error("please enter a value!")

    
       
       
       
       
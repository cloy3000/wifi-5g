





import requests
from streamlit_lottie import st_lottie
from PIL import Image 
import streamlit as st 

st.set_page_config(page_title= "Wifi 5g Adapter", page_icon= "📱", layout="wide") 

st.sidebar.success("Select a page")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()



animation =  load_lottieurl("https://lottie.host/c3590327-f977-4948-88dc-eacea632ed7b/PqAJ59yBRi.json")

with st.container():
    st.title("Make your internet wifi connection more faster.")
    st.write("---")
    col1, col2 = st.columns(2)
    with col2:
        st_lottie(animation, key="WiFi")
    with col1:
        st.subheader('"Invisible threads weaving a world of knowledge and connection at your fingertips."')
        st.write("""      The story of Wi-Fi starts in Hawaii in 1971 with ALOHAnet, a wireless network connecting the islands. 
                 Though not Wi-Fi itself, it laid the groundwork. The key player, Vic Hayes, is considered the "father of Wi-Fi" 
                 for his work on setting the standards in the late 1970s. The 1980s saw the FCC open up radio frequencies for   
                 unlicensed use, which companies jumped on. The need for a common language led to the IEEE 802.11 standards in 
                 1997, but it wasn't until catchy branding arrived in 1999 with "Wi-Fi" that things really took off. That same 
                 year, Wi-Fi got a major boost when Apple included it in their iBook laptops, making it a mainstream consumer 
                 feature. Since then, Wi-Fi has continued to evolve, offering faster speeds and wider ranges, forever changing
                 the way we connect to the world.""")




        
    



    

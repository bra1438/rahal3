import streamlit as st
from utils import *

def main():

    # Congfiger the page attributes
    st.set_page_config(
    page_title='Ksa Vacation',
    page_icon=":Travel:",   
    layout="wide")

    # Set the background and the logo
    set_background('vacation.jpeg')
    add_logo("logo4.png")

    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Write down the title in the middle of the page
    _,col2,_= st.columns( [0.3,0.5, 0.1])
    with col2:
        st.markdown(f"""<h1 style="color:#41ba61;font-family: "Cooper Black";">رحــــــــــــال </h1>""", unsafe_allow_html=True)
        _,column2= st.columns( [0.1,3.4])
        with column2:
            st.markdown(f"""<h4 >Launch your joy</h4>""", unsafe_allow_html=True)

    
    st.divider()
    st.markdown(f"""<h2 style="color:#41ba61;font-family: "Cooper Black";">تطبيق يغير من ابعاد تنقا السائح\n\n</h2>""", unsafe_allow_html=True)
    st.empty()
    st.empty()
    st.markdown("<h4>If so, then you've come to the right place! Our website is your one-stop shop for all things Saudi Arabia tourism. We have everything you need to plan your perfect trip and information on the best places to visit .\n\n</h4>", unsafe_allow_html=True)



if __name__ == "__main__":
    main()

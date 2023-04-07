import streamlit as st

st.set_page_config(layout='wide')
st.header("Reference for Yoga Poses")

c1 , c2 , c3= st.columns(3)
d1 , d2 , d3= st.columns(3)
e1, e2, e3 = st.columns(3)


# Row-1
with c1:
    st.subheader("Dhanurasana")
    with st.expander("Dhanurasana"):
        #st.image("./Images/Dhanurasana.png")
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Dhanurasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
with c2:
    st.subheader("Bhujangasana")
    with st.expander("Bhujangasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Baddha%20Konasana.png" />
    </a>''',
    unsafe_allow_html=True)
    
         
with c3:
    st.subheader("Padmasana")
    with st.expander("Padmasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Padmasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
        
# Row-2
with d1:
    st.subheader("Utthita Parsvakonasana")
    with st.expander("Utthita Parsvakonasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Utthita%20Parsvakonasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
        
with d2:
    st.subheader("Surya Namaskar")
    with st.expander("Surya Namaskar"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Surya%20Namaskar.png" />
    </a>''',
    unsafe_allow_html=True)
       
with d3:
    st.subheader("Siddhasana")
    with st.expander("Siddhasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Siddhasana.png" />
    </a>''',
    unsafe_allow_html=True)
        

# Row-3
with e1:
    st.subheader("Vrikshasana (Tree Pose)")
    with st.expander("Vrikshasana (Tree Pose)"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Vrikshasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
with e2:
    st.subheader("Baddha Konasana")
    with st.expander("Baddha Konasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Baddha%20Konasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
with e3:
    st.subheader("Utkatasana")
    with st.expander("Utkatasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/lorem-ipsum20/Images/main/Utkatasana.png" />
    </a>''',
    unsafe_allow_html=True)
       


       

import streamlit as st
st.set_page_config(page_title='Mystreamlit',page_icon='shark')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png')
st.title('Pyhton Course')
st.header('Studied by Dipika Agrawall')
st.text('This is a tutorial on Streamlit Library')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=OSnHZDZoQv8')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('ENTER NAME')
        dob=st.date_input("choose DATE OF BIRTH")
        marks=st.slider('choose Mark')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',name,'DOB',dob,'MARKS:',marks)
elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the downloaded data','onlei.txt')

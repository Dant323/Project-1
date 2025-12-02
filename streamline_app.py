import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Dante Connell| Portfolio',
  page_icon='🎯',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', '💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home':
  st.markdown('<p class="main-header">Dante Connell</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring accountant | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.2', '📚')
  with col2:
      st.metric('Projects', '4', '💻')
  with col3:
      st.metric('Skills', '10+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
                I am an Accounting major with a strong interest in financial analysis, business strategy, and emerging financial technologies. 
               I am currently developing my skills in financal reportin, managerial accounting, and data driven decison making.
                🎯 **Current Focus:** Building interactive web applications with Streamlit
            
                📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
            
                🌱 **Fun Fact:** I have won 3 local yughio tournamnts!
            ''')
  with col2:
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/avinashjairam/cis211_project1/refs/heads/main/grumpy_cat.jfif', use_column_width=True)

# About Page
elif page == '🤠 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: Accounting
                - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: Dungeons and dragons game group , creates music, Member of book club
            ''')

  with st.expander('2023 - 2025: Kingsborough community college'):
    st.write('''
                - Graduated a member of student goverment
                - Member of gameing club 
                - was extremley active in the schools community
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Video games', 'Creating music', 'Photography', 'Basketball', 'Travel', 'Cooking new meals']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png', use_column_width = True)

    with col2:
        st.subheader('Worked in a intership with black to buisness')
        st.write('Created a discord server that allows young creatives to meet up and exchnage idea')
        st.caption('**Technologies:** Photoshop, Bandlab, Streamlit')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg', use_column_width = True)
    with col2:
      st.subheader('📊 Learned metohds to trcak automize tracking data using diffrent bots')
      st.write('used bots and othr shortcuts top automize tedious task to focous on the bigger picture')
      st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Profitable skills')

  skills_data = {
    'marketing' : 85,
    'Graphic design' : 70,
    'Team coordination' : 70,
    'analyzing Data' : 65,
    'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('Bandlab')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('my_resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** connell.dante2004@gmail.com

        🏢 **LinkedIn:** [linkedin.com/in/Danteconnell](https://linkedin.com)

        👩‍💻 **Github:** [https://github.com/Danteconnell](https://github.com)

        📷 **Instagram:** [@vizon09](https://instagram.com)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 learing new skills',
            '📕 Studying',
            '☕ drinking tea',
            '🎮 Gaming',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Avinash Jairam </center>',
        unsafe_allow_html = True
    )
    

import streamlit as st
import plotly.express as px
import pandas as pd
import geopandas as gpd
from python_files.hide_trade_marks import *
from python_files.html_files import *




#Hide all Streamlit menus and trade marks
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# data sets
elections="https://raw.githubusercontent.com/kasibanteg/datasets/master/election.csv"
elections_geojson="https://raw.githubusercontent.com/kasibanteg/datasets/master/election.geojson"
elections_df1=pd.read_csv(elections)
geoj1=gpd.read_file(elections_geojson)

elections_df = elections_df1
geoj=geoj1


def main():

	activities = ["Dashboard","EDA","Plots","About"]	
	choice = st.sidebar.selectbox("Select Activity",activities)

	if choice == 'Dashboard':
            st.title("Dashboard")
            st.success("Welcome To: Montreal Election Data")
            t = "<div><h3><font style = 'color:#266150;'>You can navigate via the side bar</font></h3><div>"
            st.markdown(t, unsafe_allow_html=True)
            
        
       

	elif choice == 'EDA':
            st.subheader("Exploratory Data Analysis")
            st.dataframe(elections_df.head(5))
            st.write(geoj.astype('object').head(5))               
            
     
	elif choice == 'Plots':
                st.subheader("Data Visualization")
                
                fig=px.choropleth_mapbox(elections_df,
                                geojson=geoj,
                                color='winner',
                                locations='district',
                                featureidkey='properties.district',
                                center={'lat':45.5517,'lon':-73.7073},
                                mapbox_style='carto-positron',
                                zoom=8.5,
                                title='Election Winner',
                                opacity=.3,
                                color_discrete_map={
                                'Bergeron':'cyan',
                                'Jolly':'magenta',
                                'Coderre':'Yellow'
                                    
                                    
                                }
                                
                                )
                st.plotly_chart(fig)
	
	elif choice == 'About':
     
                t = "<div><h3><font style = 'color:#266150;'>This is a demo version..</font></h3><div>"
                st.markdown(t, unsafe_allow_html=True)
                st.success("www.kasibante.com")
                st.write(" [Portfolio](https://www.kasibante.com)")


page_bg_img = '''
        <style>
        .stApp {
          padding: 4.5rem;
        margin: 0;
        background: #edc0bf;
        background: linear-gradient(90deg, #edc0bf 0,#c4caef 58%);
          }
        
        </style>
          ''' 
st.markdown(page_bg_img, unsafe_allow_html=True)

footer = """
<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background: linear-gradient(to bottom, #33ccff 0%, #ff99cc 100%);
color: white;
text-align: center;
}
</style>

<div class="footer">
<p>www.kasibante.com</p>
</div>

"""
st.markdown(footer, unsafe_allow_html=True)

if __name__ == '__main__':
	main()

#st.set_page_config(page_title="Montreal-Elections")
def set_page_title(title):
    st.sidebar.markdown(unsafe_allow_html=True, body=f"""
        <iframe height=0 srcdoc="<script>
            const title = window.parent.document.querySelector('title') \
                
            const oldObserver = window.parent.titleObserver
            if (oldObserver) {{
                oldObserver.disconnect()
            }} \

            const newObserver = new MutationObserver(function(mutations) {{
                const target = mutations[0].target
                if (target.text !== '{title}') {{
                    target.text = '{title}'
                }}
            }}) \

            newObserver.observe(title, {{ childList: true }})
            window.parent.titleObserver = newObserver \

            title.text = '{title}'
        </script>" />
    """)


set_page_title("Montreal-Elections")

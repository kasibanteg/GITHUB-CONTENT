#referance 
# https://blog.jcharistech.com/2019/10/20/streamlit-python-tutorial-crash-course/
import streamlit as st
import pandas as pd
import numpy as np
#Hide all Streamlit menus and trade marks
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#end all Streamlit menus and trade marks

#<div  style="background-color:#f9caa7">
html_temp="""
 <div>
 <img src="https://whogavethemmoney.com/wp-content/uploads/2017/07/walmart-spark-logo-57DC35C86C-seeklogo.com_.png"  width="150" height="120" />
<b><font size='+5'>Walmart Data Analysis</font></b>
</div>
<style>
      body {
        -webkit-animation: colorchange 20s infinite;
        animation: colorchange 20s infinite;
      }
      @-webkit-keyframes colorchange {
        0% {
          background: #fffef9;
        }
        25% {
          background: #eeeeee;
        }
        50% {
          background: #dddddd;
        }
        75% {
          background: #cccccc ;
        }
        100% {
          background: #bbbbbb;
        }
      }
      @keyframes colorchange {
        0% {
          background: #fffef9;
        }
        25% {
          background: #eeeeee;
        }
        50% {
          background: #dddddd;
        }
        75% {
          background: #cccccc ;
        }
        100% {
          background: #bbbbbb;
        }
      }
    </style
<div>&nbsp;</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

#Customise side bar
html = """
  <style>
    .reportview-container {
      flex-direction: row-reverse;
    }

    header > .toolbar {
      flex-direction: row-reverse;
      left: 1rem;
      right: auto;
    }

    .sidebar .sidebar-collapse-control,
    .sidebar.--collapsed .sidebar-collapse-control {
      left: auto;
      right: 0.5rem;
    }

    .sidebar .sidebar-content {
      transition: margin-right .3s, box-shadow .3s;
    }

    .sidebar.--collapsed .sidebar-content {
      margin-left: auto;
      margin-right: -21rem;
    }

    @media (max-width: 991.98px) {
      .sidebar .sidebar-content {
        margin-left: auto;
      }
    }
	
  </style>
"""

#st.markdown(html, unsafe_allow_html=True)
st.sidebar.text("I'm here now.")



#st.title('Walmart Data Analysis')
if st.checkbox('Data Exploration Analysis'):
    product_details = pd.read_csv("walmart_ca-ecommerce_product_details.csv")
    st. subheader('Raw data : List Only 10 records')
    st.write(product_details.head(10))
    st.subheader('Data set columns and Descriptions are dispalyed')
    st.write(product_details.dtypes)
    #st.write(product_details.isnull().count())
    st.subheader('Dropping Null Columns')
    #Columns to drop
    # 1. Package Size,Postal Code : these are null value columns so these should be dropped
    # 2. Uniq Id,Product Url,Gtin : These are unneccessary columns in our data set thus these should be dropped too
    # index location for the columns to be dropped
    #Package Size[10],Postal Code[12],Uniq Id[0],Product Url[2],Gtin[9]
    #Drop multiple columns by names
    st.info("Columns to be Dropped : Package Size,Postal Code,Uniq Id,Product Url,Gtin")
    product_details_drop=product_details.drop(columns=['Package Size','Postal Code','Uniq Id','Product Url','Gtin'], axis=1, inplace=True)
    #st.write(product_details_drop)
    st.write(product_details)
    st.subheader('Handle missing Data Columns')
    #Handle missing Data Columns
    #from the above info , Brand is the only column with missing data
    #Brand is object and its catergorical data there fore we can use mode()[]
    #st.write(product_details.Brand.mode())
    #st.write(product_details.Brand.mode()[0])
    #product_details['Brand'].fillna(product_details.Brand.mode()[0],axis=0,inplace=True)
    if product_details['Brand'].fillna(product_details.Brand.mode()[0],axis=0,inplace=True)==None:
       st.success("Missing Values Have been replaced : Action has been taken on Brand Serrie Using Mode")
       #st.warning("Action has been taken on Brand Serrie Using Mode")
    else :
       st.write(product_details['Brand'].fillna(product_details.Brand.mode()[0],axis=0,inplace=True))
    #st.write(product_details['Brand'].fillna(product_details.Brand.mode()[0],axis=0,inplace=True))
    #st.write(product_details)

    st.write('Find out whether there is misspelled Data which can result to duplicates')
    st.warning('Major coumns are: Brand  and Product Names')
    st.write("**Brand**")
    st.write("Get **Brand** Uniques'")
    get_brand_unique=product_details['Brand'].unique()
    st.write(get_brand_unique)
    # from the code above, You can still Clean further in the Brand Column
    st.info("**Ray-Ban** can be converted to **Ray Ban** , its a mistype")
    product_details['Brand'].replace(['Ray-Ban'],['Ray Ban'],inplace=True)
    st.write(product_details['Brand'].unique())
    st.success("Successfully replaced **Ray-Ban** with **Ray Ban**")
    st.write("**Product Name**")
    # Balloons
    st.balloons()
	
html_temp="""
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
st.markdown(html_temp, unsafe_allow_html=True)

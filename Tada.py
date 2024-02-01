# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def get_data():
    user_file = st.file_uploader("Upload your file", type=["csv", "xlsx"]) # User file

    if user_file is not None:
        # Display a progress bar while the file is being processed
        with st.spinner('Processing...'):
            st.success("File uploaded successfully")
            return user_file
    else:
        st.info("Please upload a file")
        return None

# With user data create visuals
def visuals(user_file):
    if user_file is not None:
        # Read the file into a pandas DataFrame
        data = pd.read_csv(user_file)

        # Check if the DataFrame is empty
        if data.empty:
            st.error("The uploaded file is empty.")
        else:
            user_df = pd.DataFrame(data)

            st.write("### Data Preview")
            st.write(user_df.head())    
            st.write("---")
            st.write("### Data Information")
            st.write(user_df.describe())
    

def run():
    st.set_page_config(
        page_title="Tada",
        page_icon="👋",
    )

    st.write("# Welcome to Tada! 👋")

    st.markdown(
        """
            ---
            ### What is TADA? 
        
            Welcome to TADA, the revolutionary platform that's set to transform your data science journey. 
            Say goodbye to the tedious and time-consuming initial stages of data work. With TADA, you can
            effortlessly import your tabular data and simplify your entire workflow, allowing you to focus
            on insights rather than technical intricacies. But that's not all – TADA goes above and beyond
            by seamlessly integrating intelligent recommendations into your data exploration process, empowering
            you to make data-driven decisions with unwavering confidence. Experience the future of data science
            today with TADA, where efficiency meets intellectual invigoration.
            
            ---
        """
    )

    user_file = get_data() # Get the user data
    
    # Display some charts
    visuals(user_file)


if __name__ == "__main__":
    run()

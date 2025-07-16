# streamlit run .\gen_data_dashboard.py

import io
import csv, random
import string
import time
import zipfile
import datetime

import streamlit as st
from faker import Faker

fake = Faker()


def generate_random_string():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))
    return random_string


def generate_random_number():
    random_digit = ''.join(random.choices(string.digits, k=5))
    return random_digit


# Function to generate a unique email using only random strings
def generate_unique_email(domain="rqimail.laerdalblr.in"):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))
    email = f"{random_string}@{domain}"
    return email


# Function to generate CSV files in memory and zip them
def generate_and_zip_csvs(env, num_files, num_records):
    generated_files = []

    # Generate the CSV files in memory
    for i in range(1, num_files + 1):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'DI_{env.upper()}_file{i}_{num_records}Records_{timestamp}.csv'

        # Create a BytesIO object to simulate the file content in memory
        output = io.StringIO()
        writer = csv.writer(output)

        if env == "rqi":

            writer.writerow(
                ['UserID', 'FirstName', 'MiddleName', 'LastName', 'Email', 'JobCode', 'JobName', 'HireDate',
                 'Status', 'DateOfBirth', 'Gender', 'YearsofExperiences', 'ActiveDate', 'InactiveDate'])

            for _ in range(num_records):
                randomString = generate_random_string()
                jobCodeName = random.choice(['Doctor', 'Physician', 'Nurse', 'LabAsst'])
                yoe = fake.random_int(min=0, max=99)
                gender = random.choice(['Male', 'Female', 'other', ''])
                writer.writerow(
                    [randomString, randomString, 'API', randomString + "ln", generate_unique_email(),
                     jobCodeName, jobCodeName, '06-03-2024', 'Active', '06-03-2003', gender, yoe, '', ''])

        elif env == "eu" or env == "au" or env == "cn":

            writer.writerow(
                ['UserID', 'FirstName', 'MiddleName', 'LastName', 'Email', 'JobCode', 'JobName', 'HireDate',
                 'Status', 'ActiveDate', 'InactiveDate'])

            for _ in range(num_records):
                randomString = generate_random_string()
                jobCodeName = random.choice(['Doctor', 'Physician', 'Nurse', 'LabAsst'])
                writer.writerow(
                    [randomString, randomString, 'API', randomString + "ln", generate_unique_email(),
                     jobCodeName, jobCodeName, '06-03-2024', 'Active', '', ''])

        # Get the CSV content as bytes
        file_content = output.getvalue().encode("utf-8")
        # Store the filename and content (for zip generation later)
        generated_files.append((filename, file_content))
        # Close the BytesIO buffer
        output.close()

    # Create a zip file in memory
    zip_buffer = io.BytesIO()

    # Write the files to the zip buffer
    with zipfile.ZipFile(zip_buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for filename, file_content in generated_files:
            zip_file.writestr(filename, file_content)

    # Move the cursor back to the start of the zip buffer for downloading
    zip_buffer.seek(0)

    return zip_buffer, generated_files


# Streamlit interface
def main():
    # Custom CSS to style the page
    st.markdown("""
            <style>
                .stButton>button {
                    background-color: #4CAF50;
                    color: white;
                    font-size: 16px;
                    border-radius: 10px;
                    padding: 10px 20px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    transition: background-color 0.3s;
                }
                .stButton>button:hover {
                    background-color: #45a049;
                }
            </style>
        """, unsafe_allow_html=True)

    st.set_page_config(page_title="Interactive CSV Generator", page_icon="💼", layout="wide")

    # Styled title section
    st.markdown("""
    <div style='text-align: center; margin-top: -40px;'>
        <h1 style='color:#4CAF50; font-size: 2em;'>
        💼 Interactive <span style='color:#2196F3;'>CSV Generator</span> with ZIP 📦 Download</h1>
        <p style='font-size: 1em; color: #6c757d;'>
        Easily create CSV files, and download everything in a ZIP – all from your browser.</p>
    </div>
    """, unsafe_allow_html=True)

    # Wrap in columns to limit width
    # col1, col2 = st.columns([4, 5])  # Adjust ratio as needed
    # with col1:
    #     st.markdown("<span style='color:#1f77b4;'>📁 <b>Select Environment</b></span>", unsafe_allow_html=True)
    #     env = st.selectbox(
    #         label="Environment",
    #         options=[
    #             "🌐 RQI (Global)",
    #             "🇪🇺 EU (Europe)",
    #             "🇦🇺 AU (Australia)",
    #             "🇨🇳 CN (China)"
    #         ],
    #         index=0,
    #         help="Choose the environment for the generated files.",
    #         label_visibility="collapsed"
    #     )
    # env = env.split()[1].lower() # Extract 'rqi', 'eu', etc.

    # Custom bold label
    st.markdown("<span style='color:#1f77b4;'>📁 <b>Select Environment</b></span>", unsafe_allow_html=True)
    env = st.radio(
        label="Environment",
        options=["🌐 RQI (Global)", "🇪🇺 EU (Europe)", "🇦🇺 AU (Australia)", "🇨🇳 CN (China)"],
        horizontal=True,
        label_visibility="collapsed"
    )
    env = env.split()[1].lower()

    # Conditional logic to reset the values upon changing environment
    # Reset the number of files and records when environment changes
    if 'env_selected' not in st.session_state or st.session_state.env_selected != env:
        st.session_state.env_selected = env
        st.session_state.num_files = 1  # Reset number of files to default value
        st.session_state.num_records = 5  # Reset number of records to default value

    col1, col2 = st.columns([4, 5])  # col1 = narrow, col2 = wide (empty)
    with col1:
        st.markdown("<span style='color:#1f77b4;'>📁 <b>Number of Files</b></span>", unsafe_allow_html=True)
        st.caption("💡 How many files do you want to generate?")
        num_files = st.number_input(
            label="Number of files",
            min_value=1,
            value=st.session_state.num_files,
            step=1,
            help="How many files do you want to generate?",
            label_visibility="collapsed"
        )
        st.markdown("<span style='color:#1f77b4;'>📁 <b>Records/File</b></span>", unsafe_allow_html=True)
        st.caption("💡 How many records would you like each file to have?")
        num_records = st.number_input(
            label="Number of records",
            min_value=1,
            value=st.session_state.num_records,
            step=1,
            help="How many records would you like each file to have?",
            label_visibility="collapsed"
        )

    # Save the selected values in the session state
    st.session_state.num_files = num_files
    st.session_state.num_records = num_records

    # Button to generate files and show download button
    if st.button("Generate CSV Files"):
        with st.spinner(f"Generating files..."):
            filename_placeholder = st.empty()
            # Generate CSVs and zip them
            zip_file, generated_files = generate_and_zip_csvs(env, num_files, num_records)

            for i, (filename, _) in enumerate(generated_files, 0):
                filename_placeholder.info(f"🚀 Generating: {filename}")
                time.sleep(0.5)
                filename_placeholder.empty()
                # time.sleep(0.5)

            st.success("✅ All files have been generated successfully!")

            # Allow user to download the ZIP file
            st.download_button(
                label="Download ZIP 📥",
                data=zip_file,
                file_name="generated_di_files.zip",
                mime="application/zip"
            )


# Run the Streamlit app
if __name__ == "__main__":
    main()

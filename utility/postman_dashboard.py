import streamlit as st
import pandas as pd
import json
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder

st.set_page_config(page_title="Postman Test Results Dashboard", layout="wide")
st.title("📊 Postman Test Results Dashboard")

uploaded_file = st.file_uploader("Upload Postman JSON Report", type="json")

if uploaded_file:
    data = json.load(uploaded_file)
    results = data.get("results", [])

    records = []

    for entry in results:
        name = entry.get("name", "Unnamed Request")
        url = entry.get("url", "")
        response_time = entry.get("time", 0)
        status_code = entry.get("responseCode", {}).get("code", "N/A")

        tests = entry.get("tests", {})
        test_errors = entry.get("testPassFailCounts", {})

        if tests:
            for test_name, passed in tests.items():
                error_msg = "-"
                if not passed:
                    count_info = test_errors.get(test_name, {})
                    error_msg = f"Failed count: {count_info.get('fail', 1)}"
                records.append({
                    "Request Name": name,
                    "URL": url,
                    "Status Code": status_code,
                    "Response Time (ms)": response_time,
                    "Test Case": test_name,
                    "Result": "Pass" if passed else "Fail",
                    "Error": error_msg
                })
        else:
            records.append({
                "Request Name": name,
                "URL": url,
                "Status Code": status_code,
                "Response Time (ms)": response_time,
                "Test Case": "No test executed",
                "Result": "Skipped",
                "Error": "-"
            })

    if records:
        df = pd.DataFrame(records)

        # Filter section
        st.sidebar.header("🔍 Filters")
        request_filter = st.sidebar.multiselect("Select Request(s)", options=df["Request Name"].unique(),
                                                default=df["Request Name"].unique())
        status_code_filter = st.sidebar.multiselect("Select Status Code(s)", options=df["Status Code"].unique(),
                                                    default=df["Status Code"].unique())

        filtered_df = df[(df["Request Name"].isin(request_filter)) & (df["Status Code"].isin(status_code_filter))]

        # Metrics
        st.subheader("📈 Summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Requests", df["Request Name"].nunique())
        col2.metric("Total Tests", len(filtered_df))
        col3.metric("Passed Tests", (filtered_df["Result"] == "Pass").sum())
        col4.metric("Failed Tests", (filtered_df["Result"] == "Fail").sum())

        st.subheader("📊 Test Result Distribution")

        # Prepare data for both charts
        distribution_df = (
            filtered_df["Result"]
            .value_counts()
            .reindex(["Pass", "Fail", "Skipped"])
            .fillna(0)
            .reset_index()
        )
        distribution_df.columns = ["Result", "Count"]

        color_map = {
            "Pass": "green",
            "Fail": "red",
            "Skipped": "gold"
        }

        # Chart Tabs
        tab1, tab2 = st.tabs(["🧁 Pie Chart", "📊 Bar Chart"])

        with tab1:
            st.markdown("### 🧁 Pie Chart: Test Result Distribution")
            fig_pie = px.pie(
                distribution_df,
                names="Result",
                values="Count",
                title="Pie View of Test Results",
                color="Result",
                color_discrete_map=color_map
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with tab2:
            st.markdown("### 📊 Bar Chart: Test Result Distribution")
            fig_bar = px.bar(
                distribution_df,
                x="Result",
                y="Count",
                title="Bar View of Test Results",
                color="Result",
                color_discrete_map=color_map,
                text="Count"
            )
            fig_bar.update_traces(textposition="outside")
            st.plotly_chart(fig_bar, use_container_width=True)

        # Table (interactive)
        st.subheader("📋 Detailed Test Results Table")

        gb = GridOptionsBuilder.from_dataframe(filtered_df)
        gb.configure_pagination()
        gb.configure_side_bar()
        gb.configure_default_column(editable=False, groupable=True)

        # Show tooltip on hover for "Error" column
        gb.configure_column("Error", header_name="Error Message", tooltipField="Error")

        gridOptions = gb.build()

        AgGrid(
            filtered_df,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            height=500,
            theme="balham",
            tooltip_show_delay=0
        )

        # Download
        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Filtered CSV", csv, "postman_filtered_report.csv", "text/csv")
    else:
        st.warning("No test results found in the uploaded JSON.")

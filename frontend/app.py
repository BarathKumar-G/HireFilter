import requests
import streamlit as st

st.set_page_config(
    page_title="HireFilter",
    page_icon="📄",
    layout="wide"
)

st.title("HireFilter")
st.subheader(
    "AI Resume Screening Agent"
)

job_description = st.text_area(
    "Job Description",
    height=250
)

resume = st.text_area(
    "Resume",
    height=250
)

if st.button("Screen Resume"):

    if not job_description.strip():
        st.error(
            "Please enter a Job Description"
        )

    elif not resume.strip():
        st.error(
            "Please enter a Resume"
        )

    else:

        payload = {
            "job_description":
                job_description,

            "resume":
                resume
        }

        response = requests.post(
            "http://127.0.0.1:8000/screen",
            json=payload
        )

        if response.status_code != 200:

            st.error(
                f"Backend Error: {response.text}"
            )

        else:

            result = response.json()

            st.metric(
                "Match Score",
                f"{result['score']}%"
            )

            st.subheader(
                "Matching Results"
            )

            st.json(
                result["matching"]
            )

            st.subheader(
                "Explanation"
            )

            st.write(
                result["explanation"]
            )
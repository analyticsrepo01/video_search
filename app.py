import streamlit as st
import io

def main():
    st.title("Insurance Claim App")

    tab1, tab2 = st.tabs(["Welcome", "Claim Submission"])

    with tab1:
        st.header("Welcome, Saurabh!")
        st.write("Insurance Policy Number: 900294532487")

    with tab2:
        st.header("Claim Submission")
        uploaded_file = st.file_uploader("Upload Insurance Claim Receipt (PDF)", type="pdf")

        if uploaded_file is not None:
            st.write("File Uploaded Successfully!")
            #st.write(f"Filename: {uploaded_file.name}") #this line was causing an error

            if st.button("Submit Claim"):
                # Read the PDF file
                pdf_bytes = uploaded_file.read()
                #st.write(f"File Bytes: {pdf_bytes}") #this line was causing an error

                # Simulate sending to Gemini and extracting data
                st.write("Sending PDF to Gemini for processing...")
                extracted_data = simulate_gemini_extraction(pdf_bytes)

                st.write("Extracted Data:")
                st.write(extracted_data)

def simulate_gemini_extraction(pdf_bytes):
    """
    This function simulates the Gemini extraction process.
    Replace this with actual Gemini API calls.
    """
    # For demonstration purposes, let's return some dummy data.
    return {
        "name": "Saurabh",
        "provider": "Example Insurance Co.",
        "claim_amount": 100.00,
        "claim_date": "2024-01-01"
    }


if __name__ == "__main__":
    main()

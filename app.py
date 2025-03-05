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
            #st.write(f"Filename: {uploaded_file.name}") # debugging
            #st.write(f"File size: {uploaded_file.size}") # debugging

            if st.button("Submit Claim"):
                # Here, you would send the PDF to Gemini for processing
                # and extract the key fields.  This is a placeholder.
                st.write("Sending PDF to Gemini for processing...")

                # Simulate Gemini response (replace with actual Gemini integration)
                # For demonstration, let's just display some dummy extracted data
                extracted_data = {
                    "name": "Saurabh Example",
                    "provider": "Example Insurance Co.",
                    "claim_amount": "$123.45",
                    "claim_date": "2024-01-01"
                }

                st.write("Extracted Data:")
                for key, value in extracted_data.items():
                    st.write(f"{key}: {value}")

                st.success("Claim submitted successfully!")

if __name__ == "__main__":
    main()

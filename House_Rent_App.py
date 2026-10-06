# HOUSE RENT PREDICTION APP (simple version)
# Steps: 1. Import libraries  2. Load model  3. Prediction function
#        4. Build the interface  5. Predict button

import pickle
import pandas as pd
import streamlit as st

# STEP 1 & 2: LOAD THE TRAINED MODEL
# model.sav is a full pipeline, so it accepts raw values like 'Lagos' or 'Flat'
load_model = pickle.load(open('model.sav', 'rb'))
FEATURE_COLUMNS = pickle.load(open('model_columns.sav', 'rb'))


# STEP 3: PREDICTION FUNCTION
def rent_prediction(input_data):
    input_df = pd.DataFrame([input_data], columns=FEATURE_COLUMNS)
    return load_model.predict(input_df)[0]


# STEP 4: STREAMLIT INTERFACE
def main():
    st.set_page_config(page_title="House Rent Predictor", page_icon="🏠", layout="wide")
    st.title("🏠 House Rent Predictor")
    st.write("Enter the property details to estimate the annual rent in Nigeria.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Location")
        state = st.selectbox("State", ["Lagos", "Abuja", "Rivers", "Oyo", "Kano",
                                       "Kaduna", "Enugu", "Ogun", "Delta", "Anambra"])
        area_type = st.selectbox("Area Type", ["Urban", "Suburban", "Rural"])
        distance = st.number_input("Distance to City Centre (km)", min_value=0.0, value=8.0, step=1.0)

    with col2:
        st.subheader("Property")
        property_type = st.selectbox("Property Type", ["Self-Contain", "Flat", "Terrace", "Bungalow", "Duplex"], index=1)
        bedrooms = st.number_input("Bedrooms", min_value=1, max_value=8, value=3, step=1)
        bathrooms = st.number_input("Bathrooms", min_value=1, max_value=6, value=2, step=1)
        toilets = st.number_input("Toilets", min_value=1, max_value=7, value=3, step=1)
        size_sqm = st.number_input("Size (sqm)", min_value=15.0, max_value=400.0, value=100.0, step=5.0)

    with col3:
        st.subheader("Condition")
        building_age = st.number_input("Building Age (Years)", min_value=0, max_value=60, value=5, step=1)
        furnishing = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Furnished"])
        parking = st.number_input("Parking Spaces", min_value=0, max_value=10, value=1, step=1)

    st.markdown("---")
    st.subheader("Facilities")
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        has_generator = st.selectbox("Generator", ["No", "Yes"])
    with col5:
        has_borehole = st.selectbox("Borehole", ["No", "Yes"])
    with col6:
        has_security = st.selectbox("Security", ["No", "Yes"])
    with col7:
        power_hours = st.number_input("Power Supply (Hours/Day)", min_value=0.0, max_value=24.0, value=10.0, step=1.0)

    # STEP 5: PREDICTION BUTTON
    st.markdown("---")
    if st.button("Predict Annual Rent", use_container_width=True):
        try:
            input_data = {
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "toilets": toilets,
                "size_sqm": size_sqm,
                "building_age_years": building_age,
                "parking_spaces": parking,
                "distance_to_city_centre_km": distance,
                "power_supply_hours": power_hours,
                "has_generator": 1 if has_generator == "Yes" else 0,
                "has_borehole": 1 if has_borehole == "Yes" else 0,
                "has_security": 1 if has_security == "Yes" else 0,
                "state": state,
                "area_type": area_type,
                "property_type": property_type,
                "furnishing": furnishing,
            }

            rent = rent_prediction(input_data)

            st.success("Prediction complete")
            st.metric("Estimated Annual Rent", f"₦{rent:,.0f}")
            st.metric("Estimated Monthly Equivalent", f"₦{rent / 12:,.0f}")

        except Exception as e:
            st.error(f"Prediction Error: {e}")


# STEP 6: RUN APP
if __name__ == "__main__":
    main()

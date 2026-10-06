HOUSE RENT PREDICTION CAPSTONE (Real Estate, Nigeria) - REGRESSION

Files
1. house_rent_dataset.csv     Raw, messy data (3,030 rows, 17 columns), target annual_rent (NGN)
2. House_Rent_Capstone.ipynb  Cleaning, EDA, model training, saving the model
3. house_rent_clean.csv       Output of the cleaning step (3,000 rows)
4. model.sav, model_columns.sav  Saved model pipeline and feature list
5. House_Rent_App.py          Simple Streamlit app
6. requirements.txt

How to run
1. Keep all files in the same folder.
2. Open the notebook and Run All (re-creates the clean CSV and model files).
3. In a terminal inside the folder:  streamlit run House_Rent_App.py

Note: model.sav was built with scikit-learn 1.8.0. If you get a version error,
re-run the notebook to regenerate model.sav.
The dataset is synthetic (generated for learning), not real listings.

def preprocessing(df):
    import joblib
    ## Load the trained Model for Prediction
    sc = joblib.load("Standard_Scaler.joblib")
    scaled_x = sc.transform(df)
    return  scaled_x

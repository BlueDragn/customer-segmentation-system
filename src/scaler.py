from sklearn.preprocessing import StandardScaler

def scale_feature(df):

    scaler =  StandardScaler()

    scaled_data = scaler.fit_transform(df)

    return scaled_data
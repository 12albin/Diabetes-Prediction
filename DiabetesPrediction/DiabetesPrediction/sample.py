# import joblib
# import os

# # Example absolute path
# file_path = 'C:/Users/Albin T S/Desktop/AIML project/diabetes_prediction/DiabetesPrediction/DiabetesPrediction/knn.pkl'

# try:
#     # Load the model
#     loaded_model = joblib.load(file_path)
#     print("Model loaded successfully!")
#     data=[[7,100,0,0,0,30,0.484,32]]
#     # Use the loaded model for predictions
#     # Replace 'data' with your actual input data
#     predictions = loaded_model.predict(data)
#     print("Predictions:", predictions)
    
# except FileNotFoundError:
#     print(f"File '{file_path}' not found. Please check the file path.")
# except Exception as e:
#     print("Error loading the model:", e)
import joblib
print("Loading model from:", "DiabetesPrediction/DiabetesPrediction/knn.pkl")
loaded_model = joblib.load("C:/Users/Albin T S/Desktop/AIML project/diabetes_prediction/DiabetesPrediction/DiabetesPrediction/knn.pkl")

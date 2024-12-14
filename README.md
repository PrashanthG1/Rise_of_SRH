# ML Project: Subject Marks Prediction

## Project Overview

This project is designed to predict a student's marks in a third subject based on their marks in two other subjects. It uses machine learning to build an accurate model and deploys it on Azure Cloud for easy access and real-time predictions. The application allows users to input their marks in two subjects, and the model estimates their performance in a third subject.

## Key Features

- **Machine Learning Model**: Predicts marks in a third subject based on the input marks of two subjects.
- **Azure Deployment**: The application is hosted on Azure Cloud for scalability and production use.
- **Real-Time Prediction**: Users can input marks through a simple interface and get an approximate prediction of their marks in another subject.

## Methodology

1. **Data Collection**: Historical student data with marks in multiple subjects was used for training the model.
2. **Model Selection**: A regression-based machine learning model (such as Linear Regression or Decision Trees) was chosen to predict marks.
3. **Training the Model**: The model was trained using the available dataset, ensuring good generalization for future predictions.
4. **Deployment on Azure**: The trained model was deployed as a web service on Azure, making it accessible through an API for real-time predictions.

## How to Use

1. **Enter Marks**: Input the marks of two subjects (e.g., Subject 1 and Subject 2).
2. **Get Prediction**: The model will output the predicted marks in a third subject based on the inputs.
3. **Azure Deployment**: Access the deployed service through the provided endpoint for production-level predictions.

## Technologies Used

- **Machine Learning**: Python (scikit-learn, pandas, etc.)
- **Azure**: Azure Machine Learning, Azure Web Services
- **Deployment**: Azure App Services or Azure Functions (for API deployment)

## Future Enhancements

- Add more subjects for prediction to make the model more comprehensive.
- Incorporate additional features such as student history or external factors influencing performance.

## License

This project is licensed under the MIT License.


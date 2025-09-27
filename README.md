# Student Performance Prediction System

A comprehensive machine learning project that predicts student math scores based on various demographic and academic factors. This end-to-end ML pipeline includes data ingestion, transformation, model training, and a web interface for real-time predictions.

## 🎯 Project Overview

This project analyzes student performance data to predict math scores using machine learning algorithms. The system considers multiple factors including gender, ethnicity, parental education level, lunch type, test preparation course completion, and reading/writing scores to make accurate predictions.

## 🚀 Features

- **End-to-End ML Pipeline**: Complete workflow from data ingestion to model deployment
- **Multiple Algorithm Support**: Implements and compares 7 different regression algorithms
- **Automated Model Selection**: Uses GridSearchCV to find the best performing model
- **Web Interface**: Flask-based web application for easy predictions
- **Robust Error Handling**: Custom exception handling and comprehensive logging
- **Modular Architecture**: Well-structured codebase with separate components

## 🏗️ Project Structure

```
├── app.py                          # Flask web application
├── requirements.txt                # Project dependencies
├── setup.py                       # Package setup configuration
├── artifacts/                     # Generated model files and data
│   ├── model.pkl                  # Trained model
│   ├── preprocessor.pkl           # Data preprocessing pipeline
│   ├── train.csv                  # Training dataset
│   ├── test.csv                   # Testing dataset
│   └── data.csv                   # Raw dataset
├── src/
│   ├── components/
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py  # Feature engineering and preprocessing
│   │   └── model_trainer.py       # Model training and evaluation
│   ├── pipeline/
│   │   └── predict_pipeline.py    # Prediction pipeline
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   └── utils.py                   # Utility functions
├── templates/                     # HTML templates
│   ├── index.html                 # Homepage
│   └── home.html                  # Prediction form
└── catboost_info/                 # CatBoost training logs
```

## 🛠️ Technologies Used

- **Python 3.x**
- **Machine Learning**: scikit-learn, CatBoost, XGBoost
- **Web Framework**: Flask
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Model Persistence**: dill
- **Development**: Jupyter notebooks

## 🤖 Machine Learning Models

The project evaluates multiple regression algorithms:

1. **Random Forest Regressor**
2. **Decision Tree Regressor**  
3. **Gradient Boosting Regressor**
4. **Linear Regression**
5. **XGBoost Regressor**
6. **CatBoost Regressor**
7. **AdaBoost Regressor**

The system automatically selects the best-performing model based on R² score using cross-validation and hyperparameter tuning.

## 📊 Dataset Features

The model uses the following input features:

- **Gender**: Student's gender (male/female)
- **Race/Ethnicity**: Student's ethnic background
- **Parental Level of Education**: Parents' highest education level
- **Lunch**: Type of lunch (standard/free or reduced)
- **Test Preparation Course**: Completion status of test prep course
- **Reading Score**: Student's reading test score
- **Writing Score**: Student's writing test score

**Target Variable**: Math Score

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
```bash
git clone <[repository-ur](https://github.com/Muhammad-Yousaf09/ML-Project-Student-performance-indication)l>
cd student-performance-prediction
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package**
```bash
pip install -e .
```

## 💻 Usage

### Training the Model

Run the complete ML pipeline:

```bash
python src/components/data_ingestion.py
```

This will:
- Load and split the dataset
- Apply data transformations
- Train multiple models with hyperparameter tuning
- Save the best model and preprocessor

### Web Application

1. **Start the Flask server**
```bash
python app.py
```

2. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Navigate to the prediction form
   - Enter student information
   - Get instant math score predictions

### Making Predictions Programmatically

```python
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create prediction pipeline
predict_pipeline = PredictPipeline()

# Prepare input data
data = CustomData(
    gender='male',
    race_ethnicity='group B',
    parental_level_of_education="bachelor's degree",
    lunch='standard',
    test_preparation_course='completed',
    reading_score=75,
    writing_score=80
)

# Convert to DataFrame
pred_df = data.get_data_as_data_frame()

# Make prediction
results = predict_pipeline.predict(pred_df)
print(f"Predicted Math Score: {results[0]}")
```

## 📈 Model Performance

The system automatically evaluates all models and selects the best performer. Key metrics include:

- **R² Score**: Measures the proportion of variance explained
- **Cross-Validation**: Ensures model generalization
- **Hyperparameter Tuning**: Optimizes model parameters using GridSearchCV

Based on the CatBoost training logs, the model achieves:
- Final RMSE: ~4.58
- Training completed in 100 iterations
- Consistent improvement throughout training

## 🔧 Configuration

### Hyperparameter Grids

The project includes comprehensive hyperparameter tuning for each algorithm:

- **Random Forest**: n_estimators optimization
- **Gradient Boosting**: learning_rate, subsample, n_estimators
- **XGBoost**: learning_rate, n_estimators
- **CatBoost**: depth, learning_rate, iterations
- **AdaBoost**: learning_rate, n_estimators

### Data Preprocessing

- **Numerical Features**: Median imputation + Standard scaling
- **Categorical Features**: Most frequent imputation + One-hot encoding + Scaling
- **Pipeline**: Automated preprocessing using scikit-learn pipelines

## 📝 Logging & Error Handling

- **Custom Exception Class**: Detailed error tracking with file and line information
- **Comprehensive Logging**: Timestamped logs for debugging and monitoring
- **Error Propagation**: Consistent error handling throughout the pipeline

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact

**Author**: Muhammad Yousaf  
**Email**: yousafzadran50@gmail.com

## 🔮 Future Enhancements

- [ ] Add more sophisticated feature engineering
- [ ] Implement deep learning models
- [ ] Create RESTful API endpoints
- [ ] Add model interpretability features (SHAP, LIME)
- [ ] Implement automated model retraining
- [ ] Add data validation and drift detection
- [ ] Create comprehensive test suite
- [ ] Deploy to cloud platforms (AWS, Azure, GCP)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Built with ❤️ for educational purposes and real-world ML applications*

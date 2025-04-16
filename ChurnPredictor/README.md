**About** <br>
ChurnPredictor predicts whether a given subscriber will churn based on historical parameters. It makes this prediction based on a number of parameters like gender, age, telecom plan, call-in-mins, past complaints, etc.
<br>
The project uses scikit-learn's XGBoost algo to make this prediction (churn or No-churn). XGBoost is most suited because it works best for supervised classification problems based on tabular data.

**Features**
This project -
1. Loads or generates synthetic churn data
2. Preprocesses the data for machine learning
3. Trains an XGBoost model
4. Evaluates the model with metrics like precision, recall, F1-score
5. Saves the trained model to disk (in pkl format)
6. calls visualization functions from evaluate.py

**Tech Stack**
1. Python libraries
    a. scikit learn
    b. matplotlib
    c. pandas
    d. faker

**Setup Instructions** <BR>
1. python -m venv churn-pred-env
2. source churn-pred-env/bin/activate
3. pip install -r requirements.txt

**Run Instructions** <BR>
1. python3.9 train_model.py

If you get an error regarding OpenMP, you may need to install libomp library on your system using - <br>
brew install libomp

Once the application is run, you should be able to see the following
- Confusion Matrix 
- Classification Report

It should save the model as 'churn_model.pkl' file. This is your model file


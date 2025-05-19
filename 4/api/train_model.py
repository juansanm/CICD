# Niveles/4/api/train_model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, 'app/model.pkl')

if __name__ == "__main__":
    train_and_save_model()

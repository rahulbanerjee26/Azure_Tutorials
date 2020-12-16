import joblib
from azureml.core.model import Model

def init():
    global model
    # Example when the model is a file
    model_path = Model.get_model_path("knn")
    print("Model Path is  ", model_path)
    model = joblib.load(model_path)


def run(data):
    try:
        print(data)
        result = model.predict(data['data'])
        # You can return any data type, as long as it is JSON serializable.
        return {'data' : result.tolist() , 'message' : "Successfully classified Iris"}
    except Exception as e:
        error = str(e)
        return {'data' : error , 'message' : 'Failed to classify iris'}
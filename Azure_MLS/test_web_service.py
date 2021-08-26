import requests
from deploy import deploy
import json
from sklearn.preprocessing import MinMaxScaler

pip_packages=['pandas==1.1.5', 'azureml-defaults','joblib==0.17.0'] 
conda_packages = ['scikit-learn==0.23.2']
to_deploy = False

if to_deploy:
    url = deploy(
            ws_name = 'myworkspace',
            model_name = 'knnClassifierModel',
            path_to_model = 'model/knn.pkl', 
            environment_name = 'env',
            register_environment = True,
            pip_packages = pip_packages,
            conda_packages = conda_packages,
            cpu_cores =1 , 
            memory_gb = 1, 
            path_to_entry_script = 'score.py',
            service_name = 'test_deploy_service'
    )
else:
    # replace with endpoint
    url = ''
scaler = MinMaxScaler()
data = {
    'data': scaler.fit_transform([[0.9,0.1,0.1,0.9]]).tolist()
}
headers = {'Content-Type':'application/json'}
r = requests.post(url, str.encode(json.dumps(data)), headers = headers)
print(r.status_code)
print(r.json())
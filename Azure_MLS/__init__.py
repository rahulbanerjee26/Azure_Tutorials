from deploy import create_workspace, deploy
from dotenv import load_dotenv
import os

load_dotenv()
subscription_id = os.environ.get('SUBSCRIPTION_ID')
create_workspace(subscription_id,'myworkspace',False,'myResourcegroup','eastus2')

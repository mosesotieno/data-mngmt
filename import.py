# ----- Modules required

import requests
from ssaw import Client, ExportApi, QuestionnairesApi, models
from time import sleep
import configparser
import os

# ---- Define functions

def check_net(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        print(f'Connection available on: {url}')
        return True
    except requests.ConnectionError:
        return False
    
# ---- Create configuration if not there or load 

config = configparser.ConfigParser()

if not os.path.exists('config.ini'):
  
   # Add sections and set values for Survey Solutions
    config['susol'] = {
        'url': None,
        'api_user': None,
        'api_password': None,
        'workspace': None,
        'quiz_id': None
          
    }
    
  # Add the email address and password
    config['email'] = {
        'email_address': None,
        'pass_word':None
    }
    
  # Add the email address and password
    config['mysql'] = {
        'host': None,
        'database': None,
        'user': None,
        'password': None
    }
  
else:
  # Read the config file
  config.read('config.ini')
  
  
# ---- Retrieve all the necessary information

url_ss = config['susol']['url']
apiuser = config['susol']['api_user']
passwd = config['susol']['api_password']
wkspace = config['susol']['workspace']
quizid = config['susol']['quiz_id']


#----- Check whether there is internet connectivity 

net_available = check_net()


if net_available:
  try:
    client = Client(url=url_ss,
    api_user = apiuser, 
    api_password=passwd,
    workspace=wkspace)
  except:
    client=None
else:
  client=None
  print("Internet not available")
  
  
# ---- Check whether you are able to communicate with the server

if client:
  try:
    for q in QuestionnairesApi(client).get_list(questionnaire_id=quizid):
      print("Success! You have connected successfully to the server!")
      print(q.title, q.version)
  except:
    print("Unable to connect to server")
else:
  print("Configurations need to be checked!")
  

# ---- Export Data and Download
if client:
  try:
    export_object = models.ExportJob(quizid,export_type='STATA')
  
    ExportApi(client).start(export_object, wait=True)
    
    ExportApi(client, workspace=wkspace).get(questionnaire_identity=quizid,
                          export_type='STATA',
                          show_progress=True,
                          generate=True,
                          export_path='./data/rawdata/')
  except:
    print("Unable to create export object")
else:
  print("You did not connect to server")
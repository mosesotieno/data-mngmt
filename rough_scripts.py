import requests
from ssaw import Client, ExportApi, QuestionnairesApi, models
from time import sleep
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

url_ss = config['susol']['url']
apiuser = config['susol']['api_user']
passwd = config['susol']['api_password']
wkspace = config['susol']['workspace']
quizid = config['susol']['quiz_id']

wkspace = 'cp1kenya'
quizid = '7b3081cb-4f65-4de1-a9aa-9b89bcc336fd'

client = Client(url=url_ss,
    api_user = apiuser, 
    api_password=passwd,
    workspace=wkspace)

for q in QuestionnairesApi(client).get_list():
    print(q)

p2_export_object = models.ExportJob(quizid,
                                                export_type='STATA')

ExportApi(client).start(p2_export_object, wait=True)

# ----- Download the P1P2 dataset

ExportApi(client, workspace="cp1kenya").get(questionnaire_identity=quizid,
                                        export_type='STATA',
                                        show_progress=True,
                                        generate=True,
                                        export_path='.')



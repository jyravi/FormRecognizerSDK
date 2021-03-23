import os
import json
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential

endpoint= " " ## paste your endpoint
key ="" ## paste your key
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))

my_json=[]
def callBack(response):
    if response.http_request.method=='GET':
        my_json.append(json.loads(response.http_response.text()))

invoicefile= ### write the filename
with open(invoicefile, "rb") as fd:
    invoice = fd.read()
    
poller = form_recognizer_client.begin_recognize_invoices(invoice, include_field_elements =True, raw_response_hook =callBack)
result = poller.result()

response== my_json[-1]

#OCR extrcations

textlines=[]
for readresults in response["analyzeResult"]["readResults"]:
    textlines.append(readresults['lines'])

#table extractions
tables=[]
for tableresults in response["analyzeResult"]["pageResults"]:
    tables.append(tableresults['tables'])

#invoice field extraction    
for invoice in result:
    for name, field in invoice.fields.items():
        print("{}: {} has confidence {}".format(name, field.value, field.confidence))

import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential

endpoint= " " ## paste your endpoint
key ="" ## paste your key
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))

invoicefile= ### write the filename
with open(invoicefile, "rb") as fd:
    invoice = fd.read()
    
poller = form_recognizer_client.begin_recognize_invoices(invoice, include_field_elements =True, raw_response_hook =callBack)
result = poller.result()

pageNum=result[0].page_range.last_page_number

readresults={}
pageresults={}

for i in range(pageNum):
    lines=result[0].pages[i].lines
    readresults[i]=[]
    readresults[i].append(lines)
    tables=result[0].pages[i].tables
    pageresults[i]=[]
    pageresults[i].append(tables)
    
for invoice in result:
    for name, field in invoice.fields.items():
        print("{}: {} has confidence {}".format(name, field.value, field.confidence))

    

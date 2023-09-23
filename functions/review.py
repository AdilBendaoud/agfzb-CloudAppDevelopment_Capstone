from ibmcloudant.cloudant_v1 import CloudantV1, Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(param_dict):
    authenticator = IAMAuthenticator(param_dict["apikey"])
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(param_dict["url"])
    
    method = param_dict['__ow_method']
    
    if method == 'get':
        if 'dealerId' not in param_dict:
            return {'statusCode': 400,'body': 'The "dealerId" parameter is missing in the request.'}

        dealerId = param_dict['dealerId']
        response = service.post_all_docs(db='reviews',include_docs=True).get_result()
    
        rows = response.get("rows", [])
        outputData = []
        for row in rows:
            doc = row.get("doc", {})
            if  doc.get("dealership") == int(dealerId):
                outputData.append(doc)
        
        if len(outputData) == 0 :
            return {'statusCode': 404,'body': 'dealerId does not exist'}
        return {"body": outputData}
    
    elif method == 'post':
        
        try:
            response = service.post_document(db='reviews', document=param_dict["review"]).get_result()
            return {
                'headers': {'Content-Type':'application/json'},
                'body': {'data':response}
            }
        except:
            return {
                'statusCode': 404,
                'message': 'Something went wrong'
            }

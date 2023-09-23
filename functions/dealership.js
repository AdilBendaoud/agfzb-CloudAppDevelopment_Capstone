const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
    const authenticator = new IamAuthenticator({apikey: params.apikey});
    const service = new CloudantV1({
        authenticator: authenticator
    });
    service.setServiceUrl(params.url);
    const state = params.state;
    
    try {
        let inputDocuments = await service.postAllDocs({
              db: 'dealerships',
              includeDocs: true
            })
        
        if (inputDocuments.result.rows.length === 0){
            return {statusCode:404, body: "The database is empty"}
        }
        
        const outputArray = await inputDocuments.result.rows.map((inputObj) => {
            const inputDoc = inputObj.doc;
            if (state === undefined){
                return {
                    "id": inputDoc.id,
                    "city": inputDoc.city,
                    "state": inputDoc.state,
                    "st": inputDoc.st,
                    "address": inputDoc.address,
                    "zip": inputDoc.zip,
                    "lat": inputDoc.lat,
                    "long": inputDoc.long
                };
            }else{
                if(inputDoc.state === state){
                    return {
                    "id": inputDoc.id,
                    "city": inputDoc.city,
                    "state": inputDoc.state,
                    "st": inputDoc.st,
                    "address": inputDoc.address,
                    "zip": inputDoc.zip,
                    "lat": inputDoc.lat,
                    "long": inputDoc.long
                    };
                }
            }
        })
        if(outputArray.length === 0){
            return {statusCode:404, body: "The state does not exist"};
        }
        return {statusCode:200, body: outputArray };
    } catch (error) {
        return { statusCode:500, body: "Something went wrong on the server" };
    }
}
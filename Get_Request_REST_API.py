import requests

def Get_Embeddings_Sentences_API(textoflink):
    listofsentences_embeddings = []
    try:
        session = requests.Session()
        session.headers.update(
            {'Authorization': 'Token ?'})
        resultAPi = session.post('http://127.0.0.1:9000/v1/beta/api/embeddings_sentences/',
                                 data={'text': textoflink})
        print(resultAPi.content)
        if resultAPi.status_code == 200:
                listofsentences_embeddings = resultAPi.json()
        else:
            listofsentences_embeddings = {'error':'Status code is: '+str(resultAPi.status_code)}
    except Exception as e:
        print(str(e))
        pass

    return listofsentences_embeddings


listres = Get_Embeddings_Sentences_API("amin is good boy.")
print(listres)
# if 'error' not in listres:
#     for key in listres['Embeddings']:
#         for i in key.items():
#             print("sentence :",i[0])
#             print("embbedding :", i[1])
# else:
#     print(listres)
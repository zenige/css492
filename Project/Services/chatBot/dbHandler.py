from Project import db

def getUserById(userID):
    doc_ref = db.collection(u'users').document(userID)
    doc = doc_ref.get()
    res = doc.to_dict()
    print('userInfo',res)
    return res
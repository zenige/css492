from Project.Services.chatBot import templateMessage,chatService
from datetime import datetime
from Project.Services.ImageClassifly import predict

import webbrowser
def stateHandler(**kwargs):
    # if kwargs['postback']['postback'] == 'a':
    #     # return webbrowser.open('https://liff.line.me/1655993001-QLqyKnVe')
    #     print("SSSS")
    print("kwargs",kwargs)

    #customer_define = customer_collection.find_one({'$and':[{"userID": kwargs['sender_id']},{"botID": ObjectId(kwargs['botID'])}]})
    res = {"message": "เกิดข้อผิดพลาดโปรดลองใหม่หรือทำกระบวนการที่ทำอยู่ให้เสร็จก่อนครับ"}
    if 'postback' in kwargs.keys():
        commands = kwargs['postback']['postback'].split("&")
        action = commands[0].split("=")
        state = commands[1].split("=")
        print(action)
        print(state)
        if(action[1] == 'start'):
            if(state[1] == 'start'):
                return {"message":"📷 ส่งรูปภาพหรือถ่ายภาพจากกล้องโทรศัพท์ของคุณมาให้ผมนำไปวินิจฉัยได้เลยครับ \n\n✨ (กรุณาส่งรูปภาพครั้งละ 1 รูปต่อการวินิจฉัย 1 ครั้งเท่านั้น) ✨   \n\nเมื่อส่งรูปภาพแล้ว กรุณารอระบบประมวลผลสักครู่นะครับ 😄"}
        elif(action[1] == 'seeMore'):
            if(state[1] == 'seeMore'):
                return templateMessage.seeMoreMessage()
            if(state[1] == 'eczema'):
                return templateMessage.seeMoreEczema()
            elif(state[1] == 'atopic'):
                return templateMessage.seeMoreAtopic()
            elif(state[1] == 'ringworm'):
                return templateMessage.seeMoreRingworm()
        elif(action[1] == 'moreDetail'):
            return templateMessage.moreDetailTreatment(state[1])
        elif(action[1] == 'moreDetailTreat'):
            substate = commands[2].split("=")
            print(substate)
            if substate[1] =='reason':
                return templateMessage.moreDetailTreatReason(state[1])
            elif substate[1] == 'treatSelf':
                return templateMessage.moreDetailTreatSelf(state[1])
            elif substate[1] == 'med':
                return templateMessage.moreDetailMed(state[1])
            elif substate[1] == 'prod':
                return templateMessage.moreDetailProd(state[1])
            elif substate[1] =='symptom':
                return templateMessage.moreDetailSymptom(state[1])
        elif(action[1] == 'medDetail'):
            return chatService.medHandler(state[1])
        # elif(action[1] == 'startDoc'):
        #     return 
            


    if 'image' in kwargs.keys():
        now = datetime.now()
        message_content = kwargs['line_bot_api'].get_message_content(kwargs['image']['imageId'])
        print(message_content)
        with open("./static/img/"+kwargs['sender_id']+'&&'+str(now)+".jpg", 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        res = predict.predictImage("./static/img/"+kwargs['sender_id']+'&&'+str(now)+".jpg",kwargs['sender_id'])
       
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res


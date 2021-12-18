from Project.Services.chatBot import templateMessage,dbHandler,treatment
from pythainlp.tokenize import word_tokenize
from Project.Services.ImageClassifly import predict
from Project.Services.liff import liffHandler
def basicEventHandler(**kwargs):

    # doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    # event_collection = mongo.db.events
    # if kwargs['subState'] == 'done' or kwargs['subState'] == 'none':
    #     return False, {'message': "Done"},"done"
    msg = kwargs['message']['message']
    msg = word_tokenize(msg)
    print(kwargs)
    for x in ['ครับ', 'ค่ะ', 'ค่า', 'คะ', 'คับ', 'คร้าบ', 'ฮ่ะ', 'อ่ะ', 'อ่า', 'ป้ะ', 'ป่ะ', 'บ่', 'แมะ', 'มะ', 'ก๊า', 'ไหม', 'มั้ย', 'หน่อย']:
        try:
            msg.remove(x)
            break
        except :
            continue
    msg = ''.join(msg)
    if msg == 'สวัดดี' or msg == 'ช่วยเหลือ' or msg == 'สวัสดี' :   #command for first time
        print("in sawad")
        firstMessage,secondMessage = templateMessage.welcomMessage(kwargs['userName'])
        print("befre return")
        return {'group': [{'message':secondMessage},{'flex':firstMessage,"alt":"skin detail"}]}
    elif msg == 'เริ่มการวินิฉัย':
        return {"message":"📷 ส่งรูปภาพหรือถ่ายภาพจากกล้องโทรศัพท์ของคุณมาให้ผมนำไปวินิจฉัยได้เลยครับ \n\n✨ (กรุณาส่งรูปภาพครั้งละ 1 รูปต่อการวินิจฉัย 1 ครั้งเท่านั้น) ✨   \n\nเมื่อส่งรูปภาพแล้ว กรุณารอระบบประมวลผลสักครู่นะครับ 😄"}
    elif msg == 'test':
        content =  {
            "type": "bubble",
            "hero": {
              "type": "image",
              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
              "size": "full",
              "aspectRatio": "20:13",
              "aspectMode": "cover",
              "action": {
                "type": "uri",
                "uri": "http://linecorp.com/"
              }
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Brown Cafe",
                  "weight": "bold",
                  "size": "xl"
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "margin": "md",
                  "contents": [
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                      "type": "text",
                      "text": "4.0",
                      "size": "sm",
                      "color": "#999999",
                      "margin": "md",
                      "flex": 0
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "lg",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Place",
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1
                        },
                        {
                          "type": "text",
                          "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                          "wrap": True,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Time",
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1
                        },
                        {
                          "type": "text",
                          "text": "10:00 - 23:00",
                          "wrap": True,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            "footer": {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "uri",
                    "label": "CALL",
                    "uri": "https://linecorp.com"
                  }
                },
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "uri",
                    "label": "WEBSITE",
                    "uri": "https://linecorp.com"
                  }
                }
              ],
              "flex": 0
            }
          }
        return {'flex':content,'alt':"sss"}
    elif msg == '1':
        a = [1,2,3]
        return {"group":[{"message":"TEST"},{"img":"https://i.ibb.co/1JJFqQW/Prednisolone-0-5-Clinipred-cream.jpg"}]}
    elif msg =='ใช่':
        userInfo = dbHandler.getUserById(kwargs['sender_id'])
        print(userInfo)
        if userInfo['mainState'] == "eczema":
            return liffHandler.treatMentEczema(userInfo['subState'])
        # elif userInfo['mainState'] =="atopic":
        #     return
        # elif userInfo['mainState'] =="ringworm":
        #     return 
    
    elif msg =='การทำแบบประเมินเสร็จสิ้น':
        userInfo = dbHandler.getUserById(kwargs['sender_id'])
        if userInfo['mainState'] == 'eczema':
            res = treatment.treatmentEczemaHandler(userInfo['subStateTH'],userInfo['subState'],userInfo['score'])
        elif userInfo['mainState'] == 'atopic':
            res = treatment.treatmentAtopicHandler(userInfo['subStateTH'],userInfo['subState'],userInfo['score'])
        elif userInfo['mainState'] == 'ringworm':
            res = treatment.treatmentRingwormHandler(userInfo['subStateTH'],userInfo['subState'],userInfo['score'])
        return res
      




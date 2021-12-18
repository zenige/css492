import json

from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)


def welcomMessage(userName):
    firstMessage = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://cdn.discordapp.com/attachments/791178261371289631/917601652649889812/Healthcare_Chatbot_-_LINE_Chatbot_Logo.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "uri": "http://linecorp.com/"
            },
            "margin": "sm",
            "position": "relative",
            "align": "start"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "ผมสามารถวินิจฉัยโรคผิวหนังของคุณได้ว่าคุณป่วยเป็นโรคอะไร เพียงคุณส่งรูปมาให้ผม เริ่มวินิจฉัยกันเลยไหมครับ? กรุณาเลือกเมนูด้านล่าง",
                    "size": "md",
                    "style": "normal",
                    "decoration": "none",
                    "position": "relative",
                    "wrap": True
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
                        "type": "postback",
                        "label": "เริ่มการวินิฉัย",
                        "display_text":"เริ่มการวินิฉัย",
                        "data": "action=start&state=start"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "ดูเพิ่มเติม",
                        "display_text":"ดูเพิ่มเติม",
                        "data": "action=seeMore&state=seeMore"

                    }
                }
            ],
            "flex": 0
        }
    }
    secondMessage = "สวัสดีครับ "+userName+"! ผมชื่อน้องสุขภาพดี ผมเป็นระบบแชทบอทช่วยวินิจฉัยและจำแนกโรคทางผิวหนังทั่วไปครับ"
    return firstMessage, secondMessage


def seeMoreMessage():

    content = columns = [
        CarouselColumn(
            thumbnail_image_url='https://i.ibb.co/94zF8gW/Eczema.jpg',
            title='1.) Eczema (โรคผื่นแพ้อักเสบ)',
            text='กดเพื่อดูข้อมูลเพิ่มเติม',
            actions=[
                PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='ดูรายละเอียดเพิ่มเติม',
                    data='action=seeMore&state=eczema'
                )
            ]
        ),
        CarouselColumn(
            thumbnail_image_url='https://i.ibb.co/cJykNJV/Atopic-Dermatitis.jpg',
            title='2.) Atopic Dermatitis (โรคผื่นภูมิแพ้ผิวหนัง)',
            text='กดเพื่อดูข้อมูลเพิ่มเติม',
            actions=[
                PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='ดูรายละเอียดเพิ่มเติม',
                    data='action=seeMore&state=atopic'
                )
            ]
        ),
        CarouselColumn(
            thumbnail_image_url='https://i.ibb.co/hsngTWk/Tinea-Ringworm-Candidiasis-and-other-Fungal-Infections.jpg',
            title='3.) Tinea Ringworm (โรคกลากเกลื้อน)',
            text='กดเพื่อดูข้อมูลเพิ่มเติม',
            actions=[
                PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='ดูรายละเอียดเพิ่มเติม',
                    data='action=seeMore&state=ringworm'
                )
            ]
        )

    ]
    return {'group': [{'message': "การวินิจฉัยนั้น ระบบจะให้คุณส่งรูปภาพหรือถ่ายภาพจากโทรศัพท์ของคุณมายังแชทบอท จากนั้นระบบจะใช้เวลาประมวลผลจากรูปภาพของคุณสักครู่ เมื่อประมวลผลเสร็จสิ้น ระบบจะส่งผลการวินิจฉัยมาให้คุณ พร้อมทั้งคำแนะนำต่าง ๆ ในการรักษา"}, {'message': "โดยระบบจะวินิจฉัยว่าคุณมีความน่าจะเป็นที่จะอยู่ในกลุ่มเสี่ยงของโรคใดจากทั้งหมด 3 โรค ได้แก่"}, {'carousel': content, "alt": "skin detail"}]}


def seeMoreEczema():
    return {"message": "โรคผื่นแพ้อักเสบ (Eczema) คือภาวะการอักเสบของผิวหนังที่เกิดขึ้น เป็นได้จากหลายสาเหตุ มักมาด้วยอาการผื่นคัน บวม หรือแดงตามผิวหนัง แต่ในบางรายอาจเกิดเป็นแผลพุพอง มีน้ำหนอง หรือตกสะเก็ดร่วมด้วย โดยภาวะผิวหนังอักเสบที่พบบ่อย ได้แก่ โรคผื่นภูมิแพ้ผิวหนัง โรคเซบเดิร์ม และโรคผื่นแพ้สัมผัส อย่างไรก็ตามภาวะนี้จะไม่ติดต่อสู่ผู้อื่น แต่อาจทำให้รู้สึกคันหรือระคายเคือง และเสียความมั่นใจเพราะลักษณะผิวหนังที่ผิดปกติได้\n\nอ่านเพิ่มเติมที่: https://www.lcclinics.com/ผิวหนังอักเสบ-eczema-คืออะไร/"}

def seeMoreAtopic():
    return {"message": "โรคผื่นภูมิแพ้ผิวหนัง (Atopic Dermatits)  เป็นโรคผิวหนังอักเสบที่เป็นๆ หายๆ พบบ่อยในเด็ก ผู้ที่ป่วยเป็นโรคนี้จะมีแนวโน้มทางพันธุกรรมอยู่เป็นพื้นฐาน กล่าวคือ ผู้ป่วยมักมีประวัติเยื่อบุตาอักเสบ แพ้อากาศ ไอ  จามบ่อย ๆ หรือหอบหืด โดยเฉพาะเวลาที่อากาศรอบตัวเปลี่ยนแปลง เช่น ตอนเช้ามืดคนในครอบครัวผู้ป่วยมักมีประวัติโรคภูมิแพ้ของเยื่อบุต่าง ๆ เช่น เยื่อบุตาอักเสบภูมิแพ้ แพ้อากาศ ไอจามบ่อย ๆ หอบหืด หรือผิวหนังอักเสบภูมิแพ้\n\nอ่านเพิ่มเติมที่: https://www.si.mahidol.ac.th/siriraj_online/thai_version/Health_detail.asp?id=22"}

def seeMoreRingworm():
    return {"message":"โรคกลากเกลื้อนและการติดเชื้อราอื่น ๆ (Tinea Ringworm Candidiasis and other Fungal Infections)  เป็น โรคติดเชื้อราสามารถเป็นโรคติดต่อได้ มันสามารถแพร่กระจายจากคนสู่คน ในบางรายอาจพบว่าสาเหตุของการติดเชื้ออาจมาจากการติดเชื้อจากสัตว์หรือพื้นผิวหรือดินที่มีการปนเปื้อน\n\nอ่านเพิ่มเติม https://www.ptat.org/uploads/pdf/journalPdf_36-2-2013-e4.pdf\n"}

def listPredictImg(disease,userId):
    content = columns = []
    for idx, i in enumerate(disease):
        print(idx)
        url = ''
        if i['label'] == 'Tinea_Ringworm':
            url = 'https://liff.line.me/1656721605-52PWxpmj'
            content.append(CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/hsngTWk/Tinea-Ringworm-Candidiasis-and-other-Fungal-Infections.jpg',
                title=str((idx+1))+'.) '+str(i['label']),
                text='มีความน่าจะเป็น = '+str(i['predict']),
                actions=[
                     PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='ดูรายละเอียดเพิ่มเติม',
                    data='action=seeMore&state=ringworm'
                    )
                ]
            ))
        elif i['label'] == 'Eczema':
            
            content.append(CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/94zF8gW/Eczema.jpg',
                title=str((idx+1))+'.) '+str(i['label']),
                text='มีความน่าจะเป็น = '+str(i['predict']),
                actions=[
                     PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='ดูรายละเอียดเพิ่มเติม',
                    data='action=seeMore&state=eczema'
                    )
                ]
            ))
        elif i['label'] == 'Atopic_Dermatitis':
            url = 'https://liff.line.me/1656721598-rbNWDBag'
            content.append(CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/cJykNJV/Atopic-Dermatitis.jpg',
                title=str((idx+1))+'.) '+str(i['label']),
                text='มีความน่าจะเป็น = '+str(i['predict']),
                  actions=[
                     PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='ดูรายละเอียดเพิ่มเติม',
                    data='action=seeMore&state=atopic'
                    )
                ]
            ))
        nameTH = ''
        if(str(disease[0]['label'])) == 'Tinea_Ringworm':
            print("11111")
            nameTH = 'โรคกลากเกลื้อน'
            url='https://liff.line.me/1656721605-52PWxpmj'
        elif(str(disease[0]['label'])) == 'Eczema':
            print("22222")
            nameTH = 'โรคผื่นแพ้อักเสบ'
            url = 'https://liff.line.me/1655993001-QLqyKnVe'
        elif(str(disease[0]['label'])) == 'Atopic_Dermatitis':
            print("33333")
            nameTH = 'โรคผื่นภูมิแพ้ผิวหนัง'
            url='https://liff.line.me/1656721598-rbNWDBag'
        flexContent = {
            "type": "bubble",
            "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "คุณต้องการทำแบบประเมินเพื่อประเมินระดับความรุนแรงของ"+str(nameTH)+" ("+str(disease[0]['label'])+") หรือไม่?",
                            "weight": "regular",
                            "decoration": "none",
                            "position": "relative",
                            "align": "start",
                            "gravity": "top",
                            "wrap": True
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
                                "label": "ใช่ ทำเลย",
                                "display_text":'ทำแบบประเมินเพิ่มเติม',
                                "uri": url+"?userId="+userId
                            }
                        },
                    {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "postback",
                                "label": "ไม่ละ ขอบคุณ",
                                "display_text":'ไม่ทำแบบประเมินเพิ่มเติม',
                                "data": "action=moreDetail&state="+str(disease[0]['label'])
                            }
                        }
                ],
                "flex": 0
            }
        }
    return {"group": [{'carousel': content, "alt": "skin detail"}, {'message': 'คุณมีความน่าจะเป็นที่จะเป็นโรค'+str(disease[0]['label']) + 'มากที่สุดถึง' + str(disease[0]['predict']) + '% '}, {'flex': flexContent, 'alt': 'ต้องการทำแบบทดสอบเพิ่มเติมไหม'}]}
    #     content['colums']


def moreDetailTreatment(i):
    print("moredetail",i)
    content = ""
    if i == 'Eczema':
        content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/94zF8gW/Eczema.jpg',
                title='1.) สาเหตุที่ทำให้เกิดโรคผืนแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม สาเหตุที่ทำให้เกิดโรคผืนแพ้อักเสบ',
                        data='action=moreDetailTreat&state=eczema&subState=reason'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/FwCBX3d/image.png',
                title='2.) การดูแลตัวเองสำหรับโรคผื่นแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม การดูแลตัวเองสำหรับโรคผื่นแพ้อักเสบ',
                        data='action=moreDetailTreat&state=eczema&subState=treatSelf'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/892W6mJ/image.jpg',
                title='3.) การใช้ยารักษาโรคผืนแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม การใช้ยารักษา',
                        data='action=moreDetailTreat&state=eczema&subState=med'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/QdtdwjN/image.jpg',
                title='4.) ผลิตภัณที่แนะนำทั่วไปสำหรับโรคผื่นแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม ผลิตภัณที่แนะนำทั่วไปสำหรับโรคผื่นแพ้อักเสบ',
                        data='action=moreDetailTreat&state=eczema&subState=prod'
                    )
                ]
            )

        ]
    elif i == 'Atopic_Dermatitis':
         content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/cJykNJV/Atopic-Dermatitis.jpg',
                title='1.) อาการและลักษณะของผื่นแพ้',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม อาการและลักษณะของผื่นแพ้',
                        data='action=moreDetailTreat&state=atopic&subState=symptom'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/FwCBX3d/image.png',
                title='2.) อะไรบ้างที่ทำให้ผื่นนี้กำเริบมากขึ้น?',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม อะไรบ้างที่ทำให้ผื่นนี้กำเริบมากขึ้น',
                        data='action=moreDetailTreat&state=atopic&subState=reason'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/892W6mJ/image.jpg',
                title='3.) วิธีการดูแลและรักษา',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม วิธีการดูแลและรักษา',
                        data='action=moreDetailTreat&state=atopic&subState=treatSelf'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/QdtdwjN/image.jpg',
                title='4.) ผลิตภัณที่แนะนำทั่วไปสำหรับโรคผื่นภูมิแพ้ผิวหนัง',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม ผลิตภัณที่แนะนำทั่วไปสำหรับโรคผื่นภูมิแพ้ผิวหนัง',
                        data='action=moreDetailTreat&state=atopic&subState=prod'
                    )
                ]
            )

        ]
    elif i == 'Tinea_Ringworm':
            content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/hsngTWk/Tinea-Ringworm-Candidiasis-and-other-Fungal-Infections.jpg',
                title='1.) สาเหตุที่ทำให้เกิดโรคกลากเกลื้อน',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม สาเหตุที่ทำให้เกิดโรคกลากเกลื้อน',
                        data='action=moreDetailTreat&state=ringworm&subState=reason'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/FwCBX3d/image.png',
                title='2.) การดูแลตัวเองสำหรับโรคกลากเกลื้อน?',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม การดูแลตัวเองสำหรับโรคกลากเกลื้อน',
                        data='action=moreDetailTreat&state=ringworm&subState=treatSelf'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/892W6mJ/image.jpg',
                title='3.) การใช้ยารักษาโรคกลากเกลื้อน',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม การใช้ยารักษาโรคกลากเกลื้อน',
                        data='action=moreDetailTreat&state=ringworm&subState=med'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/QdtdwjN/image.jpg',
                title='4.) ผลิตภัณที่แนะนำทั่วไปสำหรับโรคกลากเกลื้อน',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม ผลิตภัณที่แนะนำทั่วไปสำหรับโรคกลากเกลื้อน',
                        data='action=moreDetailTreat&state=ringworm&subState=prod'
                    )
                ]
            )

        ]
    return {'carousel': content, 'alt': "ดูรายละเอียดการรักษา"}


def moreDetailTreatReason(i):
    if i == 'eczema':
        content = "สาเหตุที่ทำให้เกิดโรคผื่นแพ้อักเสบนั้น แบ่งออกเป็น 2 สาเหตุหลัก ๆ ดังนี้ \n\n1. สาเหตุภายนอกร่างกาย เช่น การสัมผัสสารระคายเคือง หรือ การแพ้สารต่างๆ โรคภูมิแพ้ หรือ อื่นๆ เช่น แมลงกัดแล้วแพ้ \n\n2. สาเหตุภายในร่างกาย มีได้หลายชนิด และมีลักษณะจำเพาะที่แตกต่างกันไป ซึ่งเกิดจากโรคต่าง ๆ ดังนี้ Atopic dermatitis ,Seborrheic dermatitis ,Nummular eczema , Dyshidrosis ,Stasis dermatitis ,Lichen simplexchronicus\n\nอ่านเพิ่มเติมที่: https://www.clinicneo.com/eczema/"
    elif i == 'atopic':
        content = "           1. สภาวะแวดล้อม เช่น สภาวะที่มีละอองเกสร ขนสัตว์ ไรฝุ่น สิ่งเหล่านี้ทำให้ผื่นมีอาการคันมากขึ้น\n           2. เชื้อโรค เช่น แบคทีเรีย เชื้อรา อาจแทรกซ้อนทำให้เกิดการติดเชื้อบนผิวหนังของผู้ป่วย ผิวหนังที่อักเสบอยู่เดิมจะกำเริบมากขึ้น\n           3. ฤดูกาล ผื่นผิวหนังอักเสบมักมีอาการมากขึ้น ในช่วงฤดูหนาว เพราะความชื้นในอากาศต่ำ อากาศแห้ง เย็น ทำให้ผิวหนังผู้ป่วยคันและเป็นผื่น \n           4. เสื้อผ้า เครื่องนุ่มห่ม  และเครื่องประดับที่มีขน โดยเฉพาะอย่างยิ่งเสื้อผ้าที่ทำจากขนสัตว์ จะทำให้เกิดการคันเพิ่มเติม\n           5. สบู่ ครีม โลชั่น และผงซักฟอกที่ใช้เป็นประจำ สารเคมีเหล่านี้มีฤทธิ์ละลายไขมัน หรือ/และอาจมีส่วนประกอบที่ก่ออาการระคายเคืองแก่ผิวหนังทำให้เกิดอาการคันและเป็นผื่นผิวหนังอักเสบได้ง่าย\n           6. อาหาร ในผู้ป่วยกลุ่มนี้ประมาณ 10% พบว่าอาหารบางชนิดเป็นตัวกระตุ้นให้ผื่นแย่ลง มักพบในผู้ป่วยเด็ก เช่น นม ไข่ ถั่วเหลือง เนื้อสัตว์บางประเภท\n           7. จิตใจที่วิตกกังวลความเครียดก็สามารถทำให้โรคกำเริบได้\n\nอ่านเพิ่มเติมที่: https://www.si.mahidol.ac.th/siriraj_online/thai_version/Health_detail.asp?id=22"
    elif i == 'ringworm':
        content = "สาเหตุที่ทำให้เกิดโรคผื่นแพ้อักเสบนั้น แบ่งออกเป็น 2 สาเหตุหลัก ๆ ดังนี้ \n\n1. สาเหตุของโรคเกลื้อนเกิดขึ้นเมื่อเชื้อยีสต์ Malassezia เติบโตอย่างรวดเร็วบนผิวหนัง แพทย์ยังไม่แน่ใจในสาเหตุ  แต่ปัจจัยบางอย่างอาจส่งเสริมการเจริญเติบโตของยีสต์บนผิวหนัง ได้แก่\n\n- สภาพอากาศที่มีความร้อนชื้น\n- เหงื่อออกมากเกินไป\n- ผิวมัน\n- ระบบภูมิคุ้มกันอ่อนแอ\n- เกิดการเปลี่ยนแปลงของฮอร์โมน\n\n2. สาเหตุของโรคกลากเกิดจากเชื้อราที่ผิวหนังในกลุ่มเดอมาโทไฟท์ (Dermatophytes) เชื้อราเหล่านี้จะอาศัยอยู่บนชั้นเนื้อเยื่อโปรตีนเคราตินบนผิวหนังที่ตายแล้วเท่านั้น แต่มักจะไม่เข้าสู่ร่างกายหรือเยื่อบุผิวอย่างปากหรือจมูก\n\nเชื้อราเป็นสปอร์เล็ก ๆ ที่มีความคงทนและสามารถอยู่รอดบนผิวหนังของมนุษย์ ในพื้นดิน หรือตามสิ่งของต่าง ๆ ได้เป็นเวลาหลายเดือน และยังเจริญเติบโตได้ดีในสภาพอากาศร้อนชื้นอย่างเช่นในประเทศไทย จึงเกิดการแพร่กระจายได้ง่าย โดยสามารถติดจากคนและสัตว์ด้วยการสัมผัส การจับสิ่งของที่มักมีเชื้อรานี้เกาะอยู่ เช่น เสื้อผ้า ผ้าเช็ดตัว หวี และแปรงสีฟัน หรือติดจากดินในกรณีที่ต้องทำงานหรือยืนเท้าเปล่าบนพื้นดินที่มีเชื้อรา\n\nอ่านเพิ่มเติมที่: http://www.ptat.org/uploads/pdf/journalPdf_36-2-2013-e4.pdf"
    return {"message": content}


def moreDetailTreatSelf(i):
    if i == 'eczema':
        content = "การดูแลตัวเองสำหรับโรคผื่นแพ้อักเสบ\n\nการดูแลตัวเองของโรคในกลุ่มนี้จะมุ่งเน้นไปที่การป้องกันและบรรเทาอาการคันให้ลดน้อยลง เนื่องจากภาวะผื่นแพ้อักเสบนั้นจะส่งผลให้ผิวแห้งและคัน โดยการดูแลตัวเองนั้นจะเป็นในลักษณะดังต่อไปนี้\n\n- หลีกเลี่ยงการถูหรือเกาบริเวณผื่นและผิวหนังที่มีอาการคัน\n- สวมใส่เสื้อผ้าที่ทำจากผ้าฝ้าย\n- เลือกใช้ผลิตภัณฑ์ซักผ้าที่อ่อนโยน\n- เพิ่มความชุ่มชื้นให้กับผิวเป็นประจำด้วยมอยซ์เจอร์ไรเซอร์\n- หลีกเลี่ยงสารก่อภูมิแพ้\n- ลดความเครียด\n\nอ่านเพิ่มเติมที่: https://www.clinicneo.com/eczema/"
    elif i == 'atopic':
        content = "     1. หลีกเลี่ยงสิ่งต่าง ๆ ที่ทำให้โรคกำเริบมากขึ้น เช่นไม่อยู่ในห้องปรับอากาศที่เย็นจัด ไม่อาบน้ำที่มีอุณหภูมิเย็นหรือร้อนจัด และควรหลีกเลี่ยงภาวะที่ทำให้เหงื่อออกมาก\n     2. ควรรับประทานยาต้านฮิสตามีน ลดอาการคัน เมื่อมีอาการคันอาจรับประทานยาต้านฮิสตามีน วันละ 2-3 ครั้งติดต่อ เว้น 5-7 วัน เพื่อลดอาการคัน เพราะอาการคันทำให้ผู้ป่วยต้องแกะเกาผิวหนัง ผื่นผิวหนังที่อักเสบจะกำเริบขึ้นได้ ยากลุ่มนี้ได้แก่คลอเฟนนิลามีน สามารถซื้อได้ตามร้านขายยาทั่วไป ข้อที่ควรระวังคือ ยานี้มีผลข้างเคียงคือ อาการง่วงนอน\n     3. ยาทากลุ่มสเตรียรอยด์ มีฤทธิ์ลดการอักเสบของผื่นผิวหนัง ควรใช้ภายใต้การดูแลของแพทย์ เพราะโรคกลุ่มนี้ต้องใช้ยานาน อาจมีอาการข้างเคียงเกิดขึ้นได้ ถ้าใช้ยาไม่ถูกต้อง\n     4. กรณีที่มีตุ่มหนองเกิดแทรกซ้อนบนตุ่มหรือผื่นแดง แสดงว่ามีการติดเชื้อแบคทีเรียแทรกซ้อน ควรปรึกษาแพทย์เพราะผู้ป่วยจำเป็นต้องได้รับยาปฏิชีวนะ เพื่อฆ่าเชื้อแบคทีเรีย\n\nอ่านเพิ่มเติมที่: https://www.si.mahidol.ac.th/siriraj_online/thai_version/Health_detail.asp?id=22"
    elif i == 'ringworm':
        content = "การดูแลตัวเองสำหรับโรคกลากเกลื่อน\n\nรักษาผิวหนังให้สะอาดและแห้ง โดยเฉพาะตามข้อพับต่างๆ ล้างมื้อบ่อยๆโดยเฉพาะหลังจากสัมผัสสัตว์หรือคนอื่นๆ หลีกเลี่ยงการใช้ผ้าขนหนูหรือผลิตภัณฑ์ดูแลส่วนตัวร่วมกับผู้อื่นๆ สวมรองเท้าในห้องล็อกเกอร์ ห้องอาบน้ำสาธารณะและสระว่ายน้ำ เช็ดอุปกรณ์ในยิมทั้งก่อนและหลังการใช้งาน\n\n- ในผู้ที่เคยเป็นโรคเกลื้อนแล้ว เมื่อกลับเป็นซ้ำอีก มักจะรู้ตัวเองได้อย่างรวดเร็ว แนะนำให้รีบปรึกษาแพทย์และทำการรักษาโดยเร็ว เพื่อไม่ให้โรคเป็นมากขึ้น\n- ในกรณีผู้ที่เป็นซ้ำบ่อยๆ อาจจำเป็นต้องใช้ยาสำหรับป้องกันสม่ำเสมอ ควรปรึกษาแพทย์ก่อนเสมอ\n- ในกรณีที่เป็นโรคเกลื้อนในเด็กเล็ก ผู้ปกครองไม่ควรรักษาเอง เพราะการเลือกชนิดยา และปริมาณยาจะแตกต่างกับในผู้ใหญ่ และในเด็กเล็กมักมีผลข้างเคียงจากยาสูงกว่าในผู้ใหญ่เมื่อใช้ขนาดยาไม่ถูกต้อง แนะนำให้ปรึกษาแพทย์ก่อนเสมอ\n- ควรรักษาความสะอาดของร่างกายไม่ให้เหงื่อไคลหมักหมม โดยเฉพาะในช่วงฤดูร้อนที่มีเหงื่อออกมาก ถ้าเหงื่อออกมาก แนะนำให้อาบน้ำบ่อยได้ และเช็ดตัวให้แห้งเสมอ\n- เลือกสวมเสื้อผ้าที่ระบายความร้อนและความชื้น เช่น เสื้อผ้าที่ทำจากผ้าฝ้าย\n- เลี่ยงการใช้ผลิตภัณฑ์ทาผิวที่เป็นน้ำมันหรือมีส่วนผสมของน้ำมัน\n\nอ่านเพิ่มเติม https://ihealzy.com/ringworm-0087/\n"
    return {"message": content}


def moreDetailMed(i):
    if i == 'eczema':
        content = "การใช้ยารักษาโรคผื่นแพ้อักเสบ\n\nกลุ่มยาทาหรือครีมทารักษาโรคผื่นแพ้อักเสบ\n- ยาทากลุ่มคอร์ติโคสเตียรอยด์ (Corticosteroids)\n- ยาทาชนิดกดภูมิคุ้มกันของร่างกาย (Calcineurin Inhibitor)\n- ครีมทามอยซ์เจอร์ไรเซอร์ชนิดเข้มข้น\n- กลุ่มน้ำมันทาผิว\n\nกลุ่มยารับประทานรักษาโรคผื่นแพ้อักเสบ\n- ยาแก้แพ้\n- ยารับประทานกลุ่มคอร์ติโคสเตียรอยด์ (Corticosteroids)\n- ยาฆ่าเชื้อ\n\nอ่านเพิ่มเติมที่: https://www.clinicneo.com/eczema/"
    elif i == 'ringworm':
        content ="ประเภทยารักษาโรคกลากเกลื้อน\n\nการรักษาโรคเกลื้อนมีด้วยกันหลายวิธี มีทั้งยากิน ยาทา และยาฟอกที่ผิวหนัง โดยยาที่ใช้ในปัจจุบันมีด้วยกัน ดังนี้\n1.กลุ่มยากินรักษาโรคเกลื้อน  ยากินรักษาโรคเกลื้อน จะใช้เป็นยากินกลุ่มยาต้านเชื้อราหรือยารักษาเชื้อราที่ผิวหนัง เหมาะสำหรับคนไข้ที่มีการติดเชื้อราเกลื้อนที่ผิวหนังเป็นบริเวณกว้าง หรือใช้ในคนไข้ที่ใช้ยาทาและยาฟอกแล้วยังไม่ได้ผล โดยปกติต้องทานติดต่อกันอย่างน้อย 2 สัปดาห์ขึ้นไป\n2.กลุ่มยาทารักษาโรคเกลื้อน  ยาทารักษาโรคเกลื้อน จะใช้เป็นยาทารักษาเชื้อรา เหมาะสำหรับคนไข้ที่มีการติดเชื้อราที่ผิวหนังไม่มาก ผื่นที่ผิวหนังไม่เยอะ\n3.กลุ่มยาฟอกหรือแชมพูรักษาโรคเกลื้อน  ยาฟอกรักษาโรคเกลื้อน จะใช้เป็นยากลุ่มแชมพูหรือสบู่ที่มีส่วนผสมของยารักษาเชื้อรา ใช้ฟอกผิวหนังที่เป็นผื่นตอนอาบน้ำ เหมาะสำหรับคนไข้ที่มีผื่นเป็นบริเวณกว้าง\n \nอ่านเพิ่มเติม https://www.lcclinics.com/โรคเกลื้อน-pityriasis-versicolor-คืออะไร/\n"
    return {"message": content}

def moreDetailSymptom(i):
    if i == 'atopic':
        content = "ผื่นผิวหนังอักเสบในโรคนี้อาการคันมาก ลักษณะเป็นผื่นแดงหรือมีตุ่มแดงนูน ตุ่มน้ำใส ซึ่งเมื่อแตกออกเป็นน้ำเหลืองไหลเยิ้มแล้วกลายเป็นสะเก็ดแข็ง ถ้าผื่นนี้เป็นมานานเข้าสู่ระยะเรื้อรัง จะพบเป็นแผ่นหนาแข็ง มีขุย ตำแหน่งที่พบผื่นแตกต่างกันได้ตามวัยของผู้ป่วยในเด็กเล็ก ช่วงขวบปีแรก ผื่นผิวหนังอักเสบจะพบมากบริเวณใบหน้า ศีรษะ เด็กมักจะเอาแก้มหรือศีรษะถูกไถกับหมอน ผ้า ที่นอน เพราะผื่นคันมากในเด็กวัยเรียน และผู้ใหญ่ ผื่นผิวหนังอักเสบพบมากในบริเวณข้อพับแขน ข้อพับขา คอ ใบหน้า และผิวหนังตำแหน่งที่มีการเสียดสีแต่ในรายที่เป็นมากๆ ผื่นเกิดทั่วร่างกายได้\n\nอ่านเพิ่มเติมที่: https://www.si.mahidol.ac.th/siriraj_online/thai_version/Health_detail.asp?id=22"
    return {"message": content}
def moreDetailProd(i):
    if i == 'eczema':
        content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/SVDF0vn/1.png',
                title='Betamethasone Dipropionate 0.05%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Betamethasone ',
                         data='action=medDetail&state=betamethasone'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/wNQTgbg/2.jpg',
                title='Clobetasol Propionate 0.05%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Clobetasol',
                         data='action=medDetail&state=clobetasol'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/SxNvS2X/3.jpg',
                title='Topicorte Desoximetasone 0.25%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Topicorte',
                         data='action=medDetail&state=topicorte'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/BjDLqfX/4.jpg',
                title='Hydrocortisone Cream 1%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Hydrocortisone',
                         data='action=medDetail&state=hydrocortisone'
                     )
                ]
            )

        ]
    elif i == 'atopic':
         content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/1JJFqQW/Prednisolone-0-5-Clinipred-cream.jpg',
                title='Prednisolone 0.5% (Clinipred® cream)',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Prednisolone ',
                         data='action=medDetail&state=prednisolone'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/Cb8zNkb/Betamethasone-valerate-0-1-ointment-Betnovate-Valisone-ointment.jpg',
                title='Betamethasone valerate 0.1%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Betamethasone',
                         data='action=medDetail&state=betamethasone'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/kHj6q8T/TA-cream-0-02.png',
                title='Triamcinolone acetonide 0.02%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม triamcinolone',
                         data='action=medDetail&state=triamcinolone'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/qJSSHNP/4.jpg',
                title='Hydrocortisone Cream 1%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Hydrocortisone',
                         data='action=medDetail&state=hydrocortisone'
                     )
                ]
            )

        ]
    elif i == 'ringworm':
         content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/R7dpZzN/Clotrimazole.png',
                title='Clotrimazole',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Clotrimazole ',
                         data='action=medDetail&state=clotrimazole'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/BqWXVMC/Ketoconazole.png',
                title='Ketoconazole',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Ketoconazole',
                         data='action=medDetail&state=ketoconazole'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/SNqqC6L/Tonaf-Cream.jpg',
                title='Tonaf Cream',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Tonaf Cream',
                         data='action=medDetail&state=tonaf'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/7GzWqvM/Miconazole.jpg',
                title='Miconazole',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Miconazole',
                         data='action=medDetail&state=miconazole'
                     )
                ]
            )

        ]


    return {"carousel": content, 'alt': "ข้อมูลยาต่างๆ"}


from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)

def treatMentEczema(subState):
    res = {}
    print(subState)
    if subState == 'Clear':
        res = {"group":[{"text":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class VII: Least Potent \n\nเช่น Hydrocortisone acetate 1%, 2.5% cream (Hytisone® cream) หรือ Prednisolone 0.5% (Clinipred® cream) เป็นต้น\n\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"}]}
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6v7lBLWbECKWyBe6HHrB3gCfweE9sI10tqg&usqp=CAU',
                    title='Hydrocortisone 1% ',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=hydrocortisone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                    title='Prednisolone 0.5% (Clinipred® cream)',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=prednisolone'
                        )
                    ]
                )
            ]
        res['group'].append({'carousel':content,'alt':"ดูข้อมูลยา"})
    return res

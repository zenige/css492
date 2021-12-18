from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)

def treatmentEczemaHandler(subStateTH,subState,score):
    res = {"group":[{"message":"คุณมีระดับความรุนแรงของโรคผื่นแพ้อักเสบ (Eczema) อยู่ที่ "+str(score) +" คะแนน ซึ่งถือว่าอยู่ในระดับที่ "+subStateTH +"("+subState+") ตามเกณฑ์ของ Eczema Area and Severity Index (EASI) 😄"}]}
    content = ""
    if subState == 'Clear':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class VII: Least Potent \n\nเช่น Hydrocortisone acetate 1%, 2.5% cream (Hytisone® cream) หรือ Prednisolone 0.5% (Clinipred® cream) เป็นต้น\n\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/BjDLqfX/4.jpg',
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
                    thumbnail_image_url='https://i.ibb.co/1JJFqQW/Prednisolone-0-5-Clinipred-cream.jpg',
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
    elif subState == 'Almost_Clear':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class VI: Mild \n\nเช่น Betamethasone valerate 0.05% cream and ointment หรือ Fluocinonide acetonide 0.01% cream and solution (Synalar) เป็นต้น\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/SVDF0vn/1.png',
                    title='Betamethasone Dispropionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/HChSgWN/Fluocinonide-acetonide-0-01-cream-and-solution-Synalar.jpg',
                    title='Fluocinonide acetonide 0.01%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=fluocinonide'
                        )
                    ]
                )
            ]
    elif subState == 'Mild':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class V: Lower mid-strength \n\nเช่น Betamethasone dipropionate 0.05% lotion (Diprosone lotion), Prednicarbate 0.1% cream (Dermatop®) หรือ Triamcinolone acetonide 0.1% cream (T.A.® cream) เป็นต้น\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/f4gWxmZ/Betamethasone-dipropionate-0-05-lotion.jpg',
                    title='Betamethasone Dispropionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/VWPHv56/Prednicarbate-0-1-cream.jpg',
                    title='Prednicarbate 0.1% cream',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=prednicarbate'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/fpr3S8C/Triamcinolone-acetonide-0-1-cream-T-A-cream-jpg.jpg',
                    title='Triamcinolone acetonide 0.1%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=fluocinonide'
                        )
                    ]
                )
                
            ]
    elif subState =='Moderate':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class IV: Mid-strength\n\nเช่น Betamethasone valerate 0.1% cream (Betnovate® cream), Fluocinolone acetonide 0.025% cream (Synalar® cream), Mometasone furoate 0.1% cream (Elomet® cream) เป็นต้น\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/gFHys9B/Betamethasone-valerate-0-1-cream-Betnovate-cream.jpg',
                    title='Betamethasone valerate 0.1%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/MpN4j4h/Fluocinolone-acetonide-0-025-cream-Synalar-cream.jpg',
                    title='Fluocinolone acetonide 0.025%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=fluocinolone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/VQzDqTg/Triamcinolone-acetonide-0-1-cream-T-A-cream.jpg',
                    title='Mometasone furoate 0.1%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=mometasone'
                        )
                    ]
                )
                
            ]
    elif subState == 'Severe':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class III: Upper mid strength \n\nเช่น Betamethasone valerate 0.1% ointment (Betnovate/Valisone® ointment), Fluticasone propionate 0.005% ointment (Cutivate® ointment), Triamcinolone acetonide 0.5% cream and ointment (Aristocort®) เป็นต้น\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/Cb8zNkb/Betamethasone-valerate-0-1-ointment-Betnovate-Valisone-ointment.jpg',
                    title='Betamethasone valerate 0.1%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/rbmCvQ9/Fluticasone-propionate-0-005-ointment-Cutivate-ointment.jpg',
                    title='Fluticasone propionate 0.005%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=fluticasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/7WkbC42/Triamcinolone-acetonide-0-5-cream-and-ointment-Aristocort.jpg',
                    title='Triamcinolone acetonide 0.5%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=triamcinolone'
                        )
                    ]
                )
                
            ]
    elif subState == 'Very_Severe':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class II: Potent หรือ Class I: Superpotent \n\nเช่น Betamethasone dipropionate 0.05% cream/gel (Diprolene® cream, gel, and Diprosone® cream), Desoximetasone 0.25% cream (Topicort®) หรือ  Clobetasol propionate 0.05% cream (Dermovate cream®) เป็นต้น\n\nอ้างอิงข้อมูลจาก: การบริบาลทางเภสัชกรรมในโรคผิวหนังอักเสบ โดย นทพร ชัยพิชิต ปรด. (เภสัชกรรมเเละระบบสุขภาพ) สาขาบริบาลเภสัชกรรม คณะเภสัชศาสตร์ มหาวิทยาลัยพะเยา"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/SVDF0vn/1.png',
                    title='Betamethasone dipropionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/JszrPHK/Clobetasol-propionate-0-05-cream-Dermovate-cream.jpg',
                    title='Clobetasol propionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=clobetasol'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/SxNvS2X/3.jpg',
                    title='Desoximetasone 0.25%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=topicorte'
                        )
                    ]
                )
                
            ]
    res['group'].append({'carousel':content,'alt':"ดูข้อมูลยา"})
    return res



def treatmentAtopicHandler(subStateTH,subState,score):
    res = {"group":[{"message":"คุณมีระดับความรุนแรงของโรคผื่นภูมิแพ้ผิวหนัง (Atopic Dermatitis) อยู่ที่ "+str(score) +" คะแนน ซึ่งถือว่าอยู่ในระดับที่ "+subStateTH +"("+subState+") ตามเกณฑ์ของ The Scoring of Atopic Dermatitis (SCORAD)😄"}]}
    content = ""
    if subState == 'Mild':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Potency: Mild\n\nเช่น Hydrocortisone 1-2%(Hytisone® cream) หรือ Prednisolone 0.5% (Clinipred® cream) เป็นต้น\n\nอ้างอิงข้อมูลจาก: ตารางแสดงการจําแนกยาทาคอร์ติโคสเตอรอยด์ตามความแรงโดยวิธี vasoconstriction assay จาก แนวทางการดูแลรักษาโรคผื่นภูมิแพ้ผิวหนัง (Atopic Dermatitis) โดยคณะทำงานเพื่อการรักษาและป้องกันโรคผื่นภูมิแพ้ผิวหนังแห่งประเทศไทย"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/dtqSqRt/Hydrocortisone-1-2-Hytisone-cream.jpg',
                    title='Hydrocortisone 1-2%',
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
                    thumbnail_image_url='https://i.ibb.co/1JJFqQW/Prednisolone-0-5-Clinipred-cream.jpg',
                    title='Prednisolone 0.5% ',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=prednisolone'
                        )
                    ]
                ),
              
            ]
    elif subState == 'Moderate':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Potency: Moderate\n\nเช่น  Betamethasone dipropionate 0.05% (Visderm® cream, lotion), Triamcinolone acetonide 0.1% (TA® cream), Betamethasone valerate 0.1% (Betnovate® cream)  หรือ Fluocinolone acetonide 0.025 (Synalar® cream)  เป็นต้น\n\nอ้างอิงข้อมูลจาก: ตารางแสดงการจําแนกยาทาคอร์ติโคสเตอรอยด์ตามความแรงโดยวิธี vasoconstriction assay จาก แนวทางการดูแลรักษาโรคผื่นภูมิแพ้ผิวหนัง (Atopic Dermatitis) โดยคณะทำงานเพื่อการรักษาและป้องกันโรคผื่นภูมิแพ้ผิวหนังแห่งประเทศไทย"})
        content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/SVDF0vn/1.png',
                    title='Betamethasone dipropionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/VQzDqTg/Triamcinolone-acetonide-0-1-cream-T-A-cream.jpg',
                    title='Triamcinolone acetonide 0.1%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=triamcinolone'
                        )
                    ]
                ), 
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/gFHys9B/Betamethasone-valerate-0-1-cream-Betnovate-cream.jpg',
                    title='Betamethasone valerate 0.1%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/MpN4j4h/Fluocinolone-acetonide-0-025-cream-Synalar-cream.jpg',
                    title='Fluocinolone acetonide 0.025',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=fluocinolone'
                        )
                    ]
                ),
              
            ]
    elif subState == 'Severe':
            res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Potency: Potent หรือ Super potent\n\nเช่น Betamethasone dipropionate 0.05% (Diprosone ointment), Desoximetasone 0.25% (Topicorte) หรือ Clobetasol propionate 0.05% (Dermovate) เป็นต้น\n\nอ้างอิงข้อมูลจาก: ตารางแสดงการจําแนกยาทาคอร์ติโคสเตอรอยด์ตามความแรงโดยวิธี vasoconstriction assay จาก แนวทางการดูแลรักษาโรคผื่นภูมิแพ้ผิวหนัง (Atopic Dermatitis) โดยคณะทำงานเพื่อการรักษาและป้องกันโรคผื่นภูมิแพ้ผิวหนังแห่งประเทศไทย"})
            content = columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/SVDF0vn/1.png',
                    title='Betamethasone dipropionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=betamethasone'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/VQzDqTg/Triamcinolone-acetonide-0-1-cream-T-A-cream.jpg',
                    title='Desoximetasone 0.25% ',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                             data='action=medDetail&state=topicorte'
                        )
                    ]
                ), 
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/gFHys9B/Betamethasone-valerate-0-1-cream-Betnovate-cream.jpg',
                    title='Clobetasol propionate 0.05%',
                    text='กดเพื่อดูข้อมูลเพิ่มเติม',
                    actions=[
                        PostbackAction(
                            label='ดูรายละเอียดเพิ่มเติม',
                            display_text='ดูเพิ่มเติม การใช้ยารักษา',
                            data='action=medDetail&state=clobetasol'
                        )
                    ]
                )
            
              
            ]
    res['group'].append({'carousel':content,'alt':"ดูข้อมูลยา"})
    return res


def treatmentRingwormHandler(subStateTH,subState,score):
    res = {"group":[{"message":"คุณมีระดับความรุนแรงของโรคกลากเกลื้อน (Tinea Ringworm)  อยู่ที่ "+str(score) +" คะแนน ซึ่งถือว่าอยู่ในระดับที่ "+subStateTH +"("+subState+") "}]}
    content = ""
    if subState == 'Mild':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\n1.กลุ่มยาทารักษาโรคเกลื้อน  ยาทารักษาโรคเกลื้อน จะใช้เป็นยาทารักษาเชื้อรา เหมาะสำหรับคนไข้ที่มีการติดเชื้อราที่ผิวหนังไม่มาก ผื่นที่ผิวหนังไม่เยอะ\n2.กลุ่มยาฟอกหรือแชมพูรักษาโรคเกลื้อน  ยาฟอกรักษาโรคเกลื้อน จะใช้เป็นยากลุ่มแชมพูหรือสบู่ที่มีส่วนผสมของยารักษาเชื้อรา ใช้ฟอกผิวหนังที่เป็นผื่นตอนอาบน้ำ เหมาะสำหรับคนไข้ที่มีผื่นเป็นบริเวณกว้าง\n\nอ่านเพิ่มเติม https://www.lcclinics.com/โรคเกลื้อน-pityriasis-versicolor-คืออะไร/"})
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
    elif subState == 'Severe':
        res['group'].append({"message":"แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\n1.กลุ่มยากินรักษาโรคเกลื้อน  ยากินรักษาโรคเกลื้อน จะใช้เป็นยากินกลุ่มยาต้านเชื้อราหรือยารักษาเชื้อราที่ผิวหนัง เหมาะสำหรับคนไข้ที่มีการติดเชื้อราเกลื้อนที่ผิวหนังเป็นบริเวณกว้าง หรือใช้ในคนไข้ที่ใช้ยาทาและยาฟอกแล้วยังไม่ได้ผล โดยปกติต้องทานติดต่อกันอย่างน้อย 2 สัปดาห์ขึ้นไป\n\nอ่านเพิ่มเติม https://www.lcclinics.com/โรคเกลื้อน-pityriasis-versicolor-คืออะไร/"})
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
    res['group'].append({'carousel':content,'alt':"ดูข้อมูลยา"})
    return res
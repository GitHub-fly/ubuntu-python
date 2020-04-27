"""
二维码
pip3 install qrcode
pip3 install myqr
"""
import qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=8, border=4)
qr.add_data('Hello World ')
img = qr.make_image()
# img.save('./resources/img/code.png')
text = """
因为一场疫情，
夺走了许多生命；
因为一场疫情，
改变了许多人的生活轨迹；
也正因为这一场疫情，
各地出现了90后舍小家顾大家的潇洒身影。


当然，
我们也因为这场疫情，
在“云”上相遇、相知，
跌跌撞撞走过了将近一个学期。


也有人，
因为这场疫情，
离去或者分隔，
请相信，
疫情一定会过去，
人一定会回来，
祖国一定会保护好大家！

"""
qr.add_data(text)
# qr.add_data('https://www.baidu.com')
img1 = qr.make_image(fill_color='rgb(255, 255, 255)',
                     back_color='rgb(88, 88, 88)')
img1.save('./resources/img/code1.png')

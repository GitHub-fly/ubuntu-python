import random


"""
生成指定长度的验证码
:param code_len: 验证码的长度（默认4个字符）
:return 有大小写英文字母和数字构成的随机验证码
"""


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


"""
判断传入的文件名是否为图片类型的文件，
并返回所有图片类型的文件
"""
def is_img(file_list):
    # 所有图片类型的列表
    img_type = ['png', 'jpg', 'gif', 'png', 'ico', 'bmp', 'webp']
    # 返回值（列表）
    file = []
    for item in file_list:
        # 此处是截取所有文件的后缀名
        # rindex(str) 方法会返回最后一次出现 str 的是索引
        # lower() 方法是将此字符串全部转为小写
        # str in str_list 的写法表示，子字符串 str 是否为列表 str_list 中的子元素（简而言之：是否包含）
        if item[(item.rindex('.') + 1):].lower() in img_type:
            file.append(item)
    return file


if __name__ == '__main__':
    # print(generate_code(6))
    file_list = ['1.png', '2.docx', '3.zip', '4.excel', '5.jpg']
    print(is_img(file_list))

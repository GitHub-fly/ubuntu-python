"""
excel格式化写操作
"""
from datetime import datetime
import xlsxwriter


def set_format():
    workbook = xlsxwriter.Workbook('./resources/excel/excel_demo2.xlsx')
    worksheet = workbook.add_worksheet()

    # 基础样式
    fmt = workbook.add_format(
        {'font_name': u'微软雅黑', 'font_size': 10}
    )
    # 背景格式：定义字体、对齐方式、背景前景色等
    bg_format = workbook.add_format(
        {'bold': True, 'font_name': u'微软雅黑', 'bg_color': '#217346',
         'align': 'center', 'valign': 'vcenter',
         'font_color': '#282c34', 'font_size': 11, 'border': 1}
    )
    # 金额格式
    money_format = workbook.add_format({'num_format': '$#, ##0'})
    # 日期格式
    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
    # 设置行高，从第 0 行开始，行高为 20，格式为 fmt
    worksheet.set_row(0, 20, fmt)
    # 设置列宽，从 A 列到 C 列，列宽为 20，格式为 fmt
    worksheet.set_column("A:C", 20, fmt)
    # 用指定北京格式写入表头
    worksheet.write('A1', 'Item', bg_format)
    worksheet.write('B1', 'Date', bg_format)
    worksheet.write('C1', 'Cost', bg_format)

    expenses = (
        ['Rent', '2020-01-13', 1000],
        ['Gas', '2020-01-14', 100],
        ['Food', '2020-01-15', 300],
        ['Gym', '2020-01-16', 50]
    )

    row = 1
    col = 0
    # 遍历数据，用不同格式写入
    for item, date_str, cost in (expenses):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        worksheet.write_string(row, col, item)
        worksheet.write_datetime(row, col + 1, date, date_format)
        worksheet.write_number(row, col + 2, cost, money_format)
        row += 1

    worksheet.write(row, 1, 'Total')
    worksheet.write(row, 2, '=SUM(C2:C5)', money_format)
    workbook.close()


def practice():
    # 1. 创建一个 excel 文件并作为当前工作簿
    workbook = xlsxwriter.Workbook('./resources/excel/excel_demo1.xls')
    # 2. 添加一个工作表，默认名称是 Sheet1，Sheet2等，可以指定名称
    # 默认名称：Sheet1
    worksheet1 = workbook.add_worksheet()
    # 指定名称：Data
    worksheet2 = workbook.add_worksheet('Data')
    # 3. 写数据
    # 向 worksheet1 指定单元格写入内容
    worksheet1.write('A1', 'Hello World')
    # 向 worksheet2 写入一组数据并用公式求和
    expenses = (
        ['Rent', 1000],
        ['Gas', 100],
        ['Food', 300],
        ['Gym', 50],
    )
    # 行和列的索引初值均为 0
    row = 0
    col = 0
    # 遍历数据并逐行写入
    for item, cost in (expenses):
        worksheet2.write(row, col, item)
        worksheet2.write(row, col + 1, cost)
        row += 1
    # 写一个公式，计算出综合
    worksheet2. write(row, 0, 'Total')
    worksheet2.write(row, 1, '=SUM(B1:B4)')

    workbook.close()


if __name__ == "__main__":
    set_format()
    # practice()

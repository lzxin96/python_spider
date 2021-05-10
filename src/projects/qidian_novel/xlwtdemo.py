import xlwt

# 1.创建Workbook对象，并指定编码为utf-8
book = xlwt.Workbook(encoding='utf-8')
# 2.添加第一个Sheet，名称为Sheet1
sheet1 = book.add_sheet('Sheet1')
sheet2 = book.add_sheet('Sheet2')
# 3.向第1个Sheet的Cell（1,1）位置添加文本
sheet1.write(1,1,'世界，你好')
# 3.向第1个Sheet的Cell（2,2）位置添加文本
sheet1.write(2,2,'用Python操作Excel')
# 3.向第2个Sheet的Cell（2,2）位置添加文本
sheet2.write(2,2,'Hello word')
# 4.保存文件
book.save('demo.xls')
# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: Projec1AutoAddTag
# FN: simple_markup
# Author: xiaxu
# DATA: 2022/1/24
# Description:简单的标记
# ---------------------------------------------------
import sys,re
import util


print('<html><head><title>world wide spam.</title><body>')

title = True  #处理标题文档，默认第一行为标题
with open('test.txt','rt',encoding='utf8')as fp:
    file = fp.readlines()
for block in util.blocks(file):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)  #将*。**内容替换为斜体，返回一个第一个参数替换为第二个参数的内容，
    # 第二个参数可以接收一个函数
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        #这个是正文
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')


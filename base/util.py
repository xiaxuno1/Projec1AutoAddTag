# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: Projec1AutoAddTag
# FN: util
# Author: xiaxu
# DATA: 2022/1/24
# Description:一个文本生成器
# ---------------------------------------------------
def lines(file):
#在文件的末尾增加一个空行，确保下面可以找到每个文本块
    for line in file:
        yield line
        yield "\n"

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield  ''.join(block).strip()
            block = []


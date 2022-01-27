# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: Projec1AutoAddTag
# FN: parsers
# Author: xiaxu
# DATA: 2022/1/26
# Description:
# ---------------------------------------------------
import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
    """
    A Parser reads a text file, applying rules and controlling a handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
            #对匹配对象调用这个函数，实现了对不同标签的匹配
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')  #开头
        for block in blocks(file):  #遍历每个文本块
            for filter in self.filters: #调用过滤
                block = filter(block, self.handler)
                for rule in self.rules: #调用规则
                    if rule.condition(block): #规则适用
                        last = rule.action(block,
                               self.handler)
                        if last: break
        self.handler.end('document') #结束

class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its constructor.解析器
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

with open('../res/test.txt','rt',encoding='utf8')as fp:
    file = fp.readlines()

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(file)
# --------------------------------------------------
# !/usr/bin/python
# -*- coding: utf-8 -*-
# PN: Projec1AutoAddTag
# FN: handler
# Author: xiaxu
# DATA: 2022/1/26
# Description:这是一个处理程序，用来处理文本；生成不同的标记；具体添加标记在这里执行，怎么添加有函数定义
# ---------------------------------------------------
class Handler:
    """
    这个是所有处理函数的超类；提供了通用的一些方法，如start，end,sub
    An object that handles method calls from the Parser.

    The Parser will call the start() and end() methods at the
    beginning of each block, with the proper block name as a
    parameter. The sub() method will be used in regular expression
    substitution. When called with a name such as 'emphasis', it will
    return a proper substitution function.
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)  #返回对象的属性相当于self.prefix_name;没有时返回none；
        # 根据前缀和名称查找对应的方法；如果是可调用的，就调用对应的方法
        if callable(method): return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    #这是一个闭包函数，返回值为一个函数；这个函数作为替换函数传递给re.sub,
    def sub(self, name):  #这里这样使用，是因为re.sub()返回可通过第二个参数接收一个函数（替换函数），
        # 将对匹配的对象调用这个函数，并将返回值插入文本中；之所以使用闭包函数，猜测是为了保存参数name的值（闭包函数的最大功能）
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            #編組0表示整個模式；模式匹配返回matchobject對象,这种对象包含与模式匹配的信息；
            #还包含与哪部分匹配的信息‘there(was a (wee)(cooper) who (lived in fyfe))’
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    A specific handler used for rendering HTML.

    The methods in HTMLRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in HTML documents.
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1)) #编组1包含匹配的结果，即待替换的内容
    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))
    def feed(self, data):
        print(data)
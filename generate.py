#!/bin/python3

import shortcodes # parse shortcodes
import sys # Parsing arguments of the script
import os # create path

@shortcodes.register("corollary", "/corollary")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{corollary}\label{%s} %s \End{corollary}' % (kwargs["label"], content)
    else:
        return '\\Begin{corollary} %s \End{corollary}' % (content)

@shortcodes.register("definition", "/definition")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{definition}\label{%s} %s \End{definition}' % (kwargs["label"], content)
    else:
        return '\\Begin{definition} %s \End{definition}' % (content)

@shortcodes.register("example", "/example")
def handler(context, content, pargs, kwargs):
    if "name" in kwargs:
        if "label" in kwargs:
            return '\\Begin{example}\\textrm{\\normalfont (%s)}\label{%s} %s \End{example}' % (kwargs["name"], kwargs["label"], content)
        else:
            return '\\Begin{example}\\textrm{\\normalfont (%s)} %s \End{example}' % (kwargs["name"], content)
    elif "label" in kwargs:
        return '\\Begin{example}\label{%s} %s \End{example}' % (kwargs["label"], content)
    else:
        return '\\Begin{example} %s \End{example}' % (content)

@shortcodes.register("exercise", "/exercise")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{exercise}\label{%s} %s \End{exercise}' % (kwargs["label"], content)
    else:
        return '\\Begin{exercise} %s \End{exercise}' % (content)

@shortcodes.register("lemma", "/lemma")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{lemma}\label{%s} %s \End{lemma}' % (kwargs["label"], content)
    else:
        return '\\Begin{lemma} %s \End{lemma}' % (content)

@shortcodes.register("proof", "/proof")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{proof}\label{%s} %s \End{proof}' % (kwargs["label"], content)
    else:
        return '\\Begin{proof} %s \End{proof}' % (content)

@shortcodes.register("proposition", "/proposition")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{proposition}\label{%s} %s \End{proposition}' % (kwargs["label"], content)
    else:
        return '\\Begin{proposition} %s \End{proposition}' % (content)

@shortcodes.register("remark", "/remark")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{remark}\label{%s} %s \End{remark}' % (kwargs["label"], content)
    else:
        return '\\Begin{remark} %s \End{remark}' % (content)

@shortcodes.register("theorem", "/theorem")
def handler(context, content, pargs, kwargs):
    if "name" in kwargs:
        if "label" in kwargs:
            return '\\Begin{theorem}\\textrm{\\normalfont (%s)}\label{%s} %s \End{theorem}' % (kwargs["name"], kwargs["label"], content)
        else:
            return '\\Begin{theorem}\\textrm{\\normalfont (%s)} %s \End{theorem}' % (kwargs["name"], content)
    elif "label" in kwargs:
        return '\\Begin{theorem}\label{%s} %s \End{theorem}' % (kwargs["label"], content)
    else:
        return '\\Begin{theorem} %s \End{theorem}' % (content)

@shortcodes.register("watch", "/watch")
def handler(context, content, pargs, kwargs):
    if "label" in kwargs:
        return '\\Begin{watch}\label{%s} %s \End{watch}' % (kwargs["label"], content)
    else:
        return '\\Begin{watch} %s \End{watch}' % (content)

parser = shortcodes.Parser(start="{{%", end="%}}")

archivo = sys.argv[1]

ruta = '../content/'

with open(str(ruta)+str(archivo)+'.md', 'r') as myfile:
    data=parser.parse(myfile.read())
    os.makedirs(os.path.dirname('outputs/'+str(archivo)+'.md'), exist_ok=True)
    text_file = open('outputs/'+str(archivo)+'.md', "w")
    text_file.write(data)
    text_file.close()

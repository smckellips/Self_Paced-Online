#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = "    "
    indent_lvl = 0

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content == None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        open_tag = [self.indent*self.indent_lvl+'<{}'.format(self.tag)]
        for k, v in self.attributes.items():
            open_tag.append(' {}="{}"'.format(k, v))
        open_tag.append('>\n')
        out_file.write("".join(open_tag))
        self.indent_lvl = self.indent_lvl+1
        for line in self.contents:
            if isinstance(line, str):
                out_file.write(self.indent*self.indent_lvl+line)
                out_file.write('\n')
            else:
                line.indent_lvl = self.indent_lvl
                line.render(out_file)
        self.indent_lvl = self.indent_lvl-1
        out_file.write(self.indent*self.indent_lvl+'</{}>\n'.format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file)


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(self.indent*self.indent_lvl+'<{}>'.format(self.tag))
        out_file.write(self.contents[0])
        out_file.write('</{}>\n'.format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, content):
        raise TypeError("Cannot add content for SelfClosingTag type")

    def render(self, out_file):
        open_tag = [self.indent*self.indent_lvl+'<{}'.format(self.tag)]
        for k, v in self.attributes.items():
            open_tag.append(' {}="{}"'.format(k, v))
        open_tag.append(' />\n')
        out_file.write("".join(open_tag))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content=None):
        self.link = link
        self.content = content

    def render(self, out_file):
        open_tag = [self.indent*self.indent_lvl+'<{} href='.format(self.tag)]
        open_tag.append('"{}"'.format(self.link))
        open_tag.append('>{}</{}>\n'.format(self.content, self.tag))
        out_file.write("".join(open_tag))


class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):

    def __init__(self, lvl, content=None):
        self.tag = "h{}".format(lvl)
        self.contents = [content]

class Meta(SelfClosingTag):
    tag = "meta"


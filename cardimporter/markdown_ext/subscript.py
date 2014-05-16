"""Subscript extension for Markdown.

To subscript something, place a tilde symbol, '~', before and after the
text that you would like in subscript:  C~6~H~12~O~6~
The numbers in this example will be subscripted.  See below for more:

Examples:

>>> import markdown
>>> md = markdown.Markdown(extensions=['subscript'])
>>> md.convert('This is sugar: C~6~H~12~O~6~')
u'<p>This is sugar: C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></p>'

Paragraph breaks will nullify subscripts across paragraphs. Line breaks
within paragraphs will not.

Adapted from https://github.com/sgraber/markdown.subscript/blob/master/subscript.py
"""

from markdown.inlinepatterns import SimpleTagPattern
from markdown import Extension

# Global Vars
SUBSCRIPT_RE = r'(\~)(.*?)(\~)'

class SubscriptExtension(Extension):
    """ Subscript Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        # Create subscript pattern
        sub_tag = SimpleTagPattern(SUBSCRIPT_RE,"sub")
        md.ESCAPED_CHARS.append('~')
        md.inlinePatterns.add('subscript', sub_tag, "<not_strong")

def makeExtension(configs=None) :
    return SubscriptExtension(configs=configs)
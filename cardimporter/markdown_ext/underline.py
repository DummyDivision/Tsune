"""Underline extension for Markdown.
This overrides the _ <em> conversion.

Example:
text_underline_text => text<span style="text-decoration: underline">underline</span>text

"""

from markdown.inlinepatterns import SimpleTagPattern
from markdown import Extension

# Global Vars
UNDERLINE_RE = r'(_)(.*?)(_)'

class UnderlineExtension(Extension):
    """ Underline Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        # Create underline pattern
        u_tag = SimpleTagPattern(UNDERLINE_RE,"u")
        md.inlinePatterns.add('underline', u_tag, "<not_strong")
        # Delete old _text_ pattern
        del md.inlinePatterns["emphasis2"]

def makeExtension(configs=None) :
    return UnderlineExtension(configs=configs)
import re
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from HTMLParser import HTMLParser

italicstyle = re.compile(r"font-style: italic")
boldstyle = re.compile(r"font-weight: bold")
understyle = re.compile(r"text-decoration: underline")
escapeSyntax = re.compile(r"(\*\*|_|\^|~|\*)")
newLineSyntax = re.compile(r"[<]br /[>]")
mathSyntax = re.compile(r"\[(\$\$?)\](.*?)\[[/]\$\$?\]")
gapSyntax = re.compile(r"\{\{c\d::(.*?)\}\}")
htmlSyntax = re.compile(r"[<]/?[^>]+?>")
mathMarke = [(r'[$$]',r'[/$$]'),(r'[$]',r'[/$]')]

ankiTagToMarkDown = { "b":r"**", "i":r"*", "u":r"_","sup":r"^", "sub":"~"}
htmlParser = HTMLParser()

def _preproccAnki(anki):
    """Escapes all markdown tags in all content (e.g. ^^ emoticon) except inside math delimiters"""
    anki = mathSyntax.sub(r"\g<1>\g<2>\g<1>", anki)
    anki_split = re.split(r"(\$\$?)",anki)
    if len(anki_split) > 1:
        anki_split = _preproccSplits(anki_split)
        anki = "".join(anki_split)
    else:
        anki = _escapeMarkdownChars(anki)
    anki = _replaceBrWithNl(anki)
    return anki

def _preproccSplits(anki_splits):
    for i in range(0,len(anki_splits),4):
        anki_splits[i] = _escapeMarkdownChars(anki_splits[i])
    return anki_splits

def _escapeMarkdownChars(text):
    return escapeSyntax.sub(r"\\\g<1>",text)

def ankiToMarkDown(anki):
    """Takes anki formatted html string and returns tsune markdown dialect"""


    anki = _preproccAnki(anki)
    anki_soup = BeautifulSoup(anki)

    [_handleGenericWrapTag(b,ankiTagToMarkDown['b']) for b in anki_soup.find_all("b")]
    [_handleGenericWrapTag(b,ankiTagToMarkDown['i']) for b in anki_soup.find_all("i")]
    [_handleGenericWrapTag(b,ankiTagToMarkDown['u']) for b in anki_soup.find_all("u")]
    [_handleGenericWrapTag(b,ankiTagToMarkDown['sup']) for b in anki_soup.find_all("sup")]
    [_handleGenericWrapTag(b,ankiTagToMarkDown['sub']) for b in anki_soup.find_all("sub")]
    # [_handleGenericInsertBeforeTag(b,ankiTagToMarkDown['div']) for b in anki_soup.find_all("div")]
    anki_soup = _scanAllOtherTagsForStyles(anki_soup)
    anki_conv = htmlParser.unescape(htmlSyntax.sub("",unicode(anki_soup)))
    return anki_conv

def ankiTupeToTsuneDict(ankiTupel):
    if gapSyntax.search(ankiTupel[0]):
        ankiTupel = _handleCloze(ankiTupel[0])
    return {"front":ankiToMarkDown(ankiTupel[0]),"back":ankiToMarkDown(ankiTupel[1])}

def _handleCloze(clozeString):
    clozeString.encode("utf-8")
    front = gapSyntax.sub("<b>[...]</b>",clozeString)
    back = gapSyntax.sub("\g<1>",clozeString)
    return [front, back]

def _scanAllOtherTagsForStyles(soup):
    # TODO ...sigh
    return soup

def _replaceBrWithNl(anki):
    anki = newLineSyntax.sub("\n",anki)
    return anki

def _handleGenericInsertBeforeTag(tag,insert):
    if tag is None or tag.string is None or tag.string.strip() == "":
        return
    _markdownWrapIfStyleMatches(tag)
    tag.insert_before(insert)
    tag.replaceWithChildren()

def _markdownWrapIfStyleMatches(tag):
    if 'style' in tag.attrs:
        _ifRegExInStyle(tag,italicstyle,ankiTagToMarkDown['i'])
        _ifRegExInStyle(tag,boldstyle,ankiTagToMarkDown['b'])
        _ifRegExInStyle(tag,understyle,ankiTagToMarkDown['u'])

def _handleGenericWrapTag(tag,wrap):
    if tag is None or tag.string is None or tag.string.strip() == "":
        return
    _markdownWrapIfStyleMatches(tag)
    _wrapTagWith(tag,wrap)
    tag.replaceWithChildren()

def _ifRegExInStyle(tag,regex,wrap):
    _ifRegExWrapWithString(tag.attrs['style'],regex,wrap,tag)

def _ifRegExWrapWithString(target,regex,wrap,tag):
    if regex.search(target):
        _wrapTagWith(tag,wrap)

def _wrapTagWith(tag, wrap):
    tag.insert_before(wrap)
    tag.insert_after(wrap)



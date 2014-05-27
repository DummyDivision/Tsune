import random
from comic.sources.questionablecontent import QuestionableContent
from comic.sources.xkcd import XKCD


sources = [XKCD, QuestionableContent]

def get_comic_source():
    cls = random.choice(sources)
    return cls()
from django.views.generic.base import TemplateView
from comic.comic_sources import get_comic_source


class ComicView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['comic_url'], context['comic_title'], context['comic_alt'] = get_comic_source().get_comic()
        return context
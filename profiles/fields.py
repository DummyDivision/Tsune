from django.template.loader import render_to_string
from inplaceeditform.fields import AdaptorTextAreaField
from pygments.filter import apply_filters


class AdaptorMarkItUp(AdaptorTextAreaField):

    @property
    def name(self):
        return 'markitup'


    def save(self, value):
        super(AdaptorMarkItUp,self).save(value)
        print value

    def render_value_edit(self,template_name="profiles/profile/markdown.html"):
        field_name = self.field_name_render
        value = super(AdaptorMarkItUp, self).render_value(field_name)
        print value.rendered
        context = {
            'rendered':value.rendered
        }
        return render_to_string(template_name, context)

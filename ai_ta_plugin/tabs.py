from lms.djangoapps.courseware.tabs import EnrolledTab
from django.utils.translation import gettext_noop
from django.conf import settings


class AITab(EnrolledTab):
    """
    The main courseware view.
    """
    type = 'ai_ta_plugin'
    title = gettext_noop('AI TA Plugin')
    priority = 40
    view_name = 'ai_ta_plugin'
    is_hideable = False
    is_default = True
    is_dynamic = True

    @property
    def link_func(self):
        def _link_func(course, reverse_func):
            return "http://apps.local.overhang.io:8080/ai/"
        return _link_func

    @classmethod
    def is_enabled(cls, course, user=None):
        """
        Courseware tabs are viewable to everyone, even anonymous users.
        """
        return True

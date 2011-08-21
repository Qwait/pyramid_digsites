from pyramid.threadlocal import get_current_request

from pyramid_digsites.models import Site

def add_renderer_globals(event):
    """ add's **site** to template
    """
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = {
        'site': Site.get_current(request)
    }
    event.update(globs)

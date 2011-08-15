from sqlalchemy import engine_from_config

from pyramid_digsites.interfaces import IPyramidDigsites
from pyramid_digsites.interfaces import PyramidDigsitesImplementation

from pyramid_digsites.models import initialize_sql

def includeme(config):
    settings = config.registry.settings

    initialize_sql(engine_from_config(settings, 'sqlalchemy.'))

    config.registry.registerUtility(PyramidDigsitesImplementation, IPyramidDigsites)
    
    config.add_subscriber('pyramid_digsites.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')
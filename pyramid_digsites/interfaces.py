from zope.interface import implements
from zope.interface import Interface

class IPyramidDigsites(Interface):
    """ IPyramidDigsites Interface
    """
    pass
    
class PyramidDigsitesImplementation(object):
    """ IPyramidDigsites Interface
    """
    implements(IPyramidDigsites)

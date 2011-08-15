from zope.interface import implements
from zope.interface import Interface

class IPyramidDigsites(Interface):
    pass
    
class PyramidDigsitesImplementation(object):
    implements(IPyramidDigsites)
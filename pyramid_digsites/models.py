from pyramid.threadlocal import get_current_request

from sqlalchemy import Column
from sqlalchemy import Unicode
from sqlalchemy import types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension 

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Site(Base):
    """ table created: digsite_site
    """
    __tablename__ = 'digsite_site'
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(types.Integer(), primary_key=True)
    name = Column('domain_name', Unicode(80), unique=True)
    display = Column('display_name', Unicode(80))

    def __repr__(self):
        return 'Site(domain=%r, display=%r)' % (self.name, self.display)

    @classmethod
    def get_current(cls, request=None):
        if not request:
            request = get_current_request()

        return DBSession.query(cls).filter_by(name=unicode(request.host)).first()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

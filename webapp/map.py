class Station(Base):
    __tablename__ = 'DublinBikesData'
    __tableargs__ = {'autoload': True}

def loadsession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


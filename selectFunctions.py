from sqlalchemy import select, Table, create_engine, MetaData

def selectByName(name_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    connection = engine.connect()
    metadata = MetaData(engine)
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    s = select([navires]).where(navires.c.name == name_ship)
    rp = connection.execute(s)
    results = rp.fetchall()
    print results

def selectByCode(code_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    connection = engine.connect()
    metadata = MetaData(engine)
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    s = select([navires]).where(navires.c.imo == code_ship)
    rp = connection.execute(s)
    results = rp.fetchall()
    print results

def filterByName(name_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    connection = engine.connect()
    metadata = MetaData(engine)
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    s = select([navires]).where(navires.c.name.like('%HARMONY%'))
    rp = connection.execute(s)
    results = rp.fetchall()
    print results

def selectJourneys(name_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    metadata = MetaData(engine)
    connection = engine.connect()
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    trajets = Table('trajets', metadata, autoload=True, autoload_with=engine)
    s = select([trajets]).where(trajets.c.ship_name == name_ship)
    rp = connection.execute(s)
    results=rp.fetchall()
    print results
from sqlalchemy import select, Table, create_engine, MetaData

def selectByName(name_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    connection = engine.connect()
    metadata = MetaData(engine)
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    s = select([navires]).where(navires.c.name == name_ship)
    rp = connection.execute(s)
    try:
        results = rp.fetchall()
        print 'Name : {} \nIMO : {} \nCountry : {} \nSize : {} x {} \nGT : {}\nType : {} \nSubtype : {}'.format(results[0][1],
                                                           int(results[0][2]),
                                                           results[0][3],
                                                           results[0][4],results[0][5],
                                                           results[0][6],
                                                            results[0][7],
                                                            results[0][8]
                                                            )
    except:
        print("Mauvais nom")
        exit(1)

def selectByCode(code_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    connection = engine.connect()
    metadata = MetaData(engine)
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    s = select([navires]).where(navires.c.imo == code_ship)
    rp = connection.execute(s)
    try:
        results = rp.fetchall()
        print 'Name : {} \nIMO : {} \nCountry : {} \nSize : {} x {} \nGT : {}\nType : {} \nSubtype : {}'.format(results[0][1],
                                                           int(results[0][2]),
                                                           results[0][3],
                                                           results[0][4],results[0][5],
                                                           results[0][6],
                                                            results[0][7],
                                                            results[0][8]
                                                            )
    except:
        print("Mauvais code")
        exit(1)

def filterByName(name_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    connection = engine.connect()
    metadata = MetaData(engine)
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    s = select([navires]).where(navires.c.name.like('%HARMONY%'))
    rp = connection.execute(s)
    results = rp.fetchall()
    for i in range(len(results)):
        print results[i][1]

def selectJourneys(name_ship):
    engine = create_engine('sqlite:///mon_sgbd.db')
    metadata = MetaData(engine)
    connection = engine.connect()
    navires = Table('navires', metadata, autoload=True, autoload_with=engine)
    trajets = Table('trajets', metadata, autoload=True, autoload_with=engine)
    s = select([trajets]).where(trajets.c.ship_name == name_ship)
    rp = connection.execute(s)
    results=rp.fetchall()
    print "{}\n{} --> {}".format(results[0][1], results[0][2], results[0][3])


from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, create_engine)

metadata = MetaData()

navires = Table('navires', metadata,
                Column('name', Integer()),
                Column('imo', String(), primary_key=True),
                Column('country', String()),
                Column('width', Integer()),
                Column('height', Integer()),
                Column('gt', Integer()),
                Column('type', String()),
                Column('subtype', String())
                )
cargaison = Table('cargaison', metadata,
                  Column('Produit', String()),
                  Column('Quantite', Integer()),
                  Column('Unite', String())
                    )
trajet = Table('trajet', metadata,
               Column('nomNavire', String()),
               Column('portDepart', String()),
               Column('portArrivee', String()),
               Column('cargaison', String())
               )
engine = create_engine('sqlite:///mon_sgbd.db')
connection = engine.connect()
metadata.create_all(engine)

from dbManagerServer import SimpleDatabaseServer

dbServer = SimpleDatabaseServer(Name='TestDBServer', Port=51133)

dbServer.add_element('carfreq', 'Carrier Frequency','Hz', 2e9, Type='float')
dbServer.add_element('carlvl', 'Carrier Level','dBm', -5.0, Type='float')
dbServer.add_element(Name='sometext', FullName='Some Text', DefaultValue="Empty", Type='str')

dbServer.run()
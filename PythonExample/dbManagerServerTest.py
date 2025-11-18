from dbManagerServer import SimpleDatabaseServer

dbServer = SimpleDatabaseServer(Name='TestDBServer')

dbServer.add_element('carfreq','Carrier Frequency','Hz',2e9)
dbServer.add_element('carlvl','Carrier Level','dBm',-5.0)
dbServer.add_element('carlvl2','Carrier Level 2','dBm',-5.0)

print(f"DB elements: {dbServer.get_elements()}")

dbServer.remove_element('carlvl2')
dbServer.remove_element('carlvl3')
print(f"DB elements: {dbServer.get_elements()}")

def test_getter(Name, Unit=None):
    print(f"\nLooking to get {Name} in {Unit}")
    try:
        if Unit is None:        
            result = dbServer.get_element_value(Name)
        else:
            result = dbServer.get_element_value(Name, Unit)
        print(f"Got as result: {result} {Unit}.")
    except Exception as e:
        print(f"Whoops, error: P{e}")

def test_setter(Name, Value, Unit=None):
    print(f"\nLooking to set {Name} {Value} {Unit}")
    try:
        if Unit is None:        
            dbServer.set_element_value(Name, Value)
        else:
            dbServer.set_element_value(Name, Value, Unit)
    except Exception as e:
        print(f"Whoops, error: P{e}")


test_getter('carfreq')
test_setter('carfreq',5e9)
test_getter('carfreq','GHz')
test_getter('carfreq')
test_setter('carfreq',3,'GHz')
test_getter('carfreq','kHz')
test_getter('carfreq')


# print("\n\n\n### Starting running server ###\n\n")
# dbServer.run()


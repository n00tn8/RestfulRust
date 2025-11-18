import socket
import datetime
from threading import Thread
from dbElements import BasicThing

class SimpleDatabaseServer():
    def __init__(self, Name = 'SimpleDB', Address = 'localhost', Port = 4321):
        self.db_dict = {}
        self.name = Name
        self.address = Address
        self.port = Port

    def add_element(self, Name, FullName, Unit=None, DefaultValue=None, Type=None):
        if Name in self.db_dict.keys():
            print(f"Overwriting {Name} in DB.")
        self.db_dict[Name] = BasicThing(Name, FullName, DefaultValue, Unit, Type)

    def get_element_value(self, Name, Unit=None):
        get_db_element = self.db_dict[Name]
        return(get_db_element.get(Unit=Unit))

    def set_element_value(self, Name, Value, Unit=None):
        print(f"Trying to set element {Name} to {Value} - {type(Value)} and {Unit} - {type(Unit)}")
        get_db_element = self.db_dict[Name]
        return(get_db_element.set(Value=Value, Unit=Unit))
    
    def get_elements(self):
        resulting_dict = {}
        for name in self.db_dict:
            resulting_dict[name] = [self.db_dict[name].full_name, self.db_dict[name].base_unit]
        return(resulting_dict)

    def remove_element(self, Name):
        try:
            print(f"Removing {Name} from DB.")
            self.db_dict.pop(Name)
        except Exception as e:
            print(f"Could not remove {Name}.")
            
    def getCommand(self, split_request):
        requested_unit = None
        request_name = ""
        print(f"Got GET command with {split_request}")
        try:
            request_name = split_request[1]
            print(f"Got request name {request_name}")
        except Exception as e:
            print(f"ERROR - Could not extract name from {split_request}.")
            return(False)
        try:
            try:
                requested_unit = split_request[2]
                print(f"Got unit name {requested_unit}")
            except Exception as e:
                pass
            return(self.get_element_value(request_name, requested_unit))
        except Exception as e:
            print(f"ERROR - Problem finding {request_name}/{requested_unit} in database")
            return(False)
            
    def setCommand(self, split_request):
        try:
            request_name = split_request[1]
        except Exception as e:
            print(f"ERROR - Could not extract name from {split_request}.")
            return(False)
        try:
            requested_value = split_request[2]
        except Exception as e:
            print(f"ERROR - Could not extract value from {split_request}.")
            return(False)
        requested_unit = None
        try:
            requested_unit = split_request[3]
        except Exception as e:
            print("No unit found")
            pass
        try:
            print(f"Looking for {request_name} in {self.db_dict}")
            self.set_element_value(request_name, requested_value, requested_unit)
            return(False)
        except Exception as e:
            print(f"ERROR - Problem finding {request_name} in database: {e}")
            return('ERROR')

    def replyOn(self,request):
        while request[-1] in ["\r","\n"]:
            request = request[:-1]
        split_request = request.split(' ')
        if request[:4] == 'GET ':
            return(self.getCommand(split_request))
        elif request[:4] == 'SET ':
            return(self.setCommand(split_request))
        elif request[:4] == 'ADD ':
            return(self.addCommand(split_request))
        elif request[:4] == 'LIST':
            return(str(self.get_elements()))

    def new_lan_connection(self, clientsocket, addr):
        print(self.name, "new connection made!",addr)
        with clientsocket:
            while True:
                try:
                    data = clientsocket.recv(1024)
                except ConnectionResetError:
                    print(self.name," - Connection to ",addr," lost.")
                    break
                if not data:
                    break
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                receiveddata = data.decode("utf-8")
                receiveddata = receiveddata.split("\r\n")
                    
                for data_element in receiveddata:
                    if data_element != "":
                        print(timestamp," - Received request for ", self.name,": ",repr(data_element))
                        print(type(data_element))
                        reply = self.replyOn(data_element)
                        print(f"Reply: {reply}")
                        if reply:
                            print(timestamp," - Sending answer to ", self.name,": ",reply,"\n")
                            clientsocket.sendall(str(reply).encode('utf-8')) # send back for now
                        else:
                            print(timestamp," - No reply required on ",repr(data_element),", sending OK.\n")
                            clientsocket.sendall(str("OK").encode('utf-8')) # send back for now

    def run(self):
        print(f"Running server {self.name}...")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((self.address, self.port))
                s.listen()
                
                while True:
                    conn, addr = s.accept()
                    clientthread = Thread(target=self.new_lan_connection,args=(conn, addr))
                    clientthread.start()
            except KeyboardInterrupt:
                print(f"KeyboardInterrupt, shutting down.")
                s.shutdown(socket.SHUT_RDWR)
                s.close()
            except Exception as e:
                print(f"Shutting down server due to: {e}")
                s.shutdown(socket.SHUT_RDWR)
                s.close()

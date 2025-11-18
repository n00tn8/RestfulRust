from unitConverter import convert_units

class BasicThing():
    def __init__(self, Name="EmptyName", FullName=None, Value=None, Unit=None, Type = None):
        self.name = Name
        self.base_unit = Unit
        self.type = Type
        if FullName is None:
            self.full_name = self.name
        else:
            self.full_name = FullName
        #print(f"creating basic thing, trying to set value to {Value}")
        self.set(Value)

    def set(self, Value, Unit=None):
        try:
            if self.type == 'int':
                Value = int(Value)
            if self.type == 'float':
                Value = float(Value)
            if self.type == 'str':
                if Unit is not None:
                    raise Exception(f"{self.name} is of type {self.type}, but unit {Unit} was provided.")
            val_to_set = Value
            if Unit is not None:
                val_to_set = convert_units(Value, Unit, self.base_unit)
            self.value = val_to_set
        except Exception as e:
            raise Exception(f"Could not set {Value} (unit {Unit}) to {self.name}, due to:\n{e}")

    def get(self, Unit=None):
        try:
            return(convert_units(self.value, self.base_unit, Unit))
        except Exception as e:
            raise Exception(f"Could not get value of {self.name} (with unit {Unit}, optional), due to:\n{e}")

class LimitedThing(BasicThing):
    def __init__(self, Name="EmptyName", FullName=None, Value=None, Unit=None, LowerLimit=-999, UpperLimit=999):
        self.lower_limit = LowerLimit
        self.upper_limit = UpperLimit
        #print(f"Created limited thing with {LowerLimit} as lower limit.")
        super(LimitedThing, self).__init__(Name, FullName, Value, Unit)

    def set(self, Value, Unit=None):
        val_to_set = Value
        if Unit is not None:
            val_to_set = convert_units(Value, Unit, self.base_unit)
        if val_to_set > self.upper_limit or val_to_set < self.lower_limit:
            print(f"Value {val_to_set} {self.base_unit} out of bounds for {self.name}. {self.lower_limit}..{self.upper_limit}")
        else:
            super(LimitedThing, self).set(Value, Unit)
            
### Create a LimitedThing from a BasicThing
def add_limits(FromBasicThing, LowerLimit=-999, UpperLimit=999):
    FromName = FromBasicThing.name
    FromFullName = FromBasicThing.full_name
    FromUnit = FromBasicThing.base_unit
    FromType = FromBasicThing.type
    FromValue = FromBasicThing.get(FromUnit)
    return LimitedThing(FromName, FromFullName, FromValue, FromUnit, LowerLimit, UpperLimit)

    



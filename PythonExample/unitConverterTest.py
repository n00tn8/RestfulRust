from unitConverter import *

def test_converter(value, InUnit, OutUnit):
    print(f"\nLooking to convert {value} {InUnit} to {OutUnit}")
    try:
        result = convert_units(value, InUnit, OutUnit)
        print(f"Got as result: {result} {OutUnit}.")
    except Exception as e:
        print(f"Whoops, error: {e}")

test_converter(1,'Hz','kHz')
test_converter(1,'Hz','Hz')
test_converter(10.5,'Hz','kHz')
test_converter(10,'Hz','kHz')
test_converter(10.5,'GHz','kHz')
test_converter(10,'GHz','kHz')
test_converter(10.5,'GHz','Hz')
test_converter(10,'GHz','Hz')
test_converter(10,None,'kHz')
test_converter(10.5,'GHz',None)
test_converter(10.5,'GHz','Hertz')
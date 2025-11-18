conv_dict = {
    'k' : 1e3,
    'G' : 1e9,
    'M' : 1e6,
    'T' : 1e12,
    'm' : 1e-3,
    'u' : 1e-6,
    'n' : 1e-9,
    'p' : 1e-12
}

def convert_units(Value, FromUnit, ToUnit):
    if (FromUnit==ToUnit) or FromUnit is None or ToUnit is None:
        return(Value)
    
    def simplify_input(input_str):
        input_str = input_str.replace('Hertz','Hz')
        input_str = input_str.replace('meter','m')
        
        input_str = input_str.replace('Tera','T')
        input_str = input_str.replace('Giga','G')
        input_str = input_str.replace('Mega','M')
        input_str = input_str.replace('kilo','k')
        input_str = input_str.replace('milli','m')
        input_str = input_str.replace('micro','u')
        input_str = input_str.replace('nano','n')
        input_str = input_str.replace('pico','p')
        return(input_str)
    
    FromUnit = simplify_input(FromUnit)
    ToUnit = simplify_input(ToUnit)
    
    if FromUnit[-2:] == 'Hz' and ToUnit[-2:] == 'Hz':
        if len(FromUnit) == 2:
            return(Value/conv_dict[ToUnit[:-2]])
        elif len(ToUnit) == 2:
            return(conv_dict[FromUnit[:-2]]*Value)
        else:
            return((conv_dict[FromUnit[:-2]]*Value)/conv_dict[ToUnit[:-2]])    
    else:
        raise Exception(f"Cannot convert between {FromUnit} and {ToUnit}.")




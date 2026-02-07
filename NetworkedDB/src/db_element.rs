use crate::unit_converter;

pub struct DataThing {
    pub name: String,
    pub base_unit: String,
    pub data_type: String,
    pub value: f64,
    limited: bool,
    min_value: f64,
    max_value: f64,
}

impl DataThing {
    pub fn new(name: &str, base_unit: &str, data_type: &str) -> Self {
        DataThing {
            name: name.to_string(),
            base_unit: base_unit.to_string(),
            data_type: data_type.to_string(),
            value: 0.0,
            limited: false,
            min_value: 0.0,
            max_value: 0.0,
        }
    }
    pub fn new_limited(name: &str, base_unit: &str, data_type: &str, limited: bool, min_value: f64, max_value: f64) -> Self {
        DataThing {
            name: name.to_string(),
            base_unit: base_unit.to_string(),
            data_type: data_type.to_string(),
            value: 0.0,
            limited,
            min_value,
            max_value,
        }
    }
}

pub fn set_value(thing: &mut DataThing, new_value: f64, unit: &str) {
    if thing.data_type != "float" {
        panic!("Data type mismatch for {}: expected float, got {}", thing.name, thing.data_type);
    }
    let converted_value = unit_converter::convert_units(new_value, unit, &thing.base_unit);
    if thing.limited {
        if converted_value >= thing.min_value && converted_value <= thing.max_value {
            thing.value = converted_value;
        }
    } else {
        thing.value = converted_value;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_unlimited_data_thing() {
        let mut thing = DataThing::new("Temperature", "C", "float");
        assert_eq!(thing.value, 0.0);
        set_value(&mut thing, 100.0, "C");
        assert_eq!(thing.value, 100.0);
        // This is not limited, so this should work
        set_value(&mut thing, 200.0, "C");
        assert_eq!(thing.value, 200.0);
    }
    #[test]
    fn test_limited_data_thing() {
        let mut thing = 
        
        DataThing::new_limited("Frequency","Hz","float",true,0.0,10e9);
        assert_eq!(thing.value, 0.0);
        set_value(&mut thing, 1.0, "GHz");
        assert_eq!(thing.value, 1000000000.0);
        // Set outside of limits, shouldn't work
        set_value(&mut thing, 11.0, "GHz");
        assert_eq!(thing.value, 1000000000.0);
        // Set outside of limits, shouldn't work
        set_value(&mut thing, -11.0, "Hz");
        assert_eq!(thing.value, 1000000000.0);

    }
}
// Convert SI prefixes
fn convert_prefixes(prefix: &str) -> f64 {
    return match prefix {
        "p" => 1e-12,
        "n" => 1e-9,
        "u" => 1e-6,
        "m" => 1e-3,
        "k" => 1e3,
        "M" => 1e6,
        "G" => 1e9,
        "T" => 1e12,
        _ => 1.0
    };
}

// Simply fully written SI names to abbreviations
pub fn simplify_input(input: &str) -> String {
    let temp = input;
    let temp = str::replace(&temp, "Hertz","Hz");
    let temp = str::replace(&temp, "meter","m");
    
    let temp = str::replace(&temp, "Tera","T");
    let temp = str::replace(&temp, "Giga","G");
    let temp = str::replace(&temp, "Mega","M");
    let temp = str::replace(&temp, "kilo","k");
    let temp = str::replace(&temp, "milli","m");
    let temp = str::replace(&temp, "micro","u");
    let temp = str::replace(&temp, "nano","n");
    let temp = str::replace(&temp, "pico","p");
    return temp;
}

// Convert supported values by unit name
pub fn convert_units(value: f64, from_unit: &str, to_unit: &str) -> f64 {

    if (from_unit==to_unit) || from_unit == "" || to_unit == ""{
        return value;
    }

    let from_unit = simplify_input(from_unit);
    let to_unit = simplify_input(to_unit);
    if from_unit[from_unit.len()-2..] == *"Hz" && to_unit[from_unit.len()-2..] == *"Hz"{
        if from_unit.len() == 2 {
            return value / convert_prefixes(&to_unit[..to_unit.len()-2]);

        }
        else if to_unit.len() == 2 {
            return value * convert_prefixes(&from_unit[..from_unit.len()-2]);
        }
        else {
            return (value * convert_prefixes(&from_unit[..from_unit.len()-2])) / convert_prefixes(&to_unit[..to_unit.len()-2]);
        }
    }
    else{
        println!("Conversion from {} to {} not yet supported.",from_unit,to_unit);
        return value;
    }

}
// Convert SI prefixes to the factor needed to remove them: k -> 1e3
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
        _ => 1.0,
    };
}

// Simplify fully written SI names to abbreviations
pub fn simplify_input(input: &str) -> String {
    let mut temp = str::replace(&input, "Hertz", "Hz");
    temp = str::replace(&temp, "meter", "m");
    temp = str::replace(&temp, "gram", "g");
    temp = str::replace(&temp, "Tera", "T");
    temp = str::replace(&temp, "Giga", "G");
    temp = str::replace(&temp, "Mega", "M");
    temp = str::replace(&temp, "kilo", "k");
    temp = str::replace(&temp, "milli", "m");
    temp = str::replace(&temp, "micro", "u");
    temp = str::replace(&temp, "nano", "n");
    temp = str::replace(&temp, "pico", "p");
    return temp;
}

// Convert supported values by unit name
pub fn convert_units(value: f64, from_unit: &str, to_unit: &str) -> f64 {
    if (from_unit == to_unit) || from_unit == "" || to_unit == "" {
        return value;
    }

    let from_unit = simplify_input(from_unit);
    let to_unit = simplify_input(to_unit);

    let si_unit_length: usize = 2;
    let second_to_last_from: usize = from_unit.len() - si_unit_length;
    let second_to_last_to: usize = to_unit.len() - si_unit_length;

    // TODO allow other easy units, more generally
    if from_unit[second_to_last_from..] == *"Hz" && to_unit[second_to_last_to..] == *"Hz" {
        if from_unit.len() == si_unit_length {
            return value / convert_prefixes(&to_unit[..second_to_last_to]);
        } else if to_unit.len() == si_unit_length {
            return value * convert_prefixes(&from_unit[..second_to_last_from]);
        } else {
            return (value * convert_prefixes(&from_unit[..second_to_last_from]))
                / convert_prefixes(&to_unit[..second_to_last_to]);
        }
    } else {
        // TODO: log INFO, don't just print
        println!(
            "Conversion from {} to {} not yet supported.",
            from_unit, to_unit
        );
        return value;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_convert_prefixes() {
        assert_eq!(convert_prefixes("G"), 1e9);
        assert_eq!(convert_prefixes("unknown"), 1.0);
        assert_eq!(convert_prefixes("k"), 1e3);
    }

    #[test]
    fn test_simplify_input() {
        assert_eq!(simplify_input("GHertz"), "GHz");
        assert_eq!(simplify_input("GigaHertz"), "GHz");
        assert_eq!(simplify_input("GigaHz"), "GHz");
        assert_eq!(simplify_input("kilo"), "k");
        assert_eq!(simplify_input("kilogram"), "kg");
        assert_eq!(simplify_input("unknown"), "unknown");
    }

    #[test]
    fn test_convert_units() {
        assert_eq!(convert_units(3.0, "unknown", "other"), 3.0);
        assert_eq!(convert_units(3.0, "unknown", "unknown"), 3.0);
        assert_eq!(convert_units(3.0, "Hertz", "unknown"), 3.0);
        assert_eq!(convert_units(3.0, "TeraHertz", "THz"), 3.0);
        assert_eq!(convert_units(3.0, "kHz", "Hz"), 3e3);
        assert_eq!(convert_units(3.0, "Hz", "mHz"), 3e3);
        assert_eq!(convert_units(3.0, "mHz", "Hz"), 3e-3);
        assert_eq!(convert_units(3.0, "kHz", "THz"), 0.000000003);
    }
}

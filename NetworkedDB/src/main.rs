mod db_element;
mod unit_converter;

fn main() {
    println!("Hello, world!");

    println!("Let's try some things");

    println!("\n==============================\n First showcasing unit conversion \n");
    println!(
        "\nconversion results in {}\n",
        unit_converter::convert_units(1.0, "Hz", "Hz")
    );
    println!(
        "\nconversion results in {}\n",
        unit_converter::convert_units(10.0, "kHz", "GHz")
    );
    println!(
        "\nconversion results in {}\n",
        unit_converter::convert_units(10.0, "MHz", "GHertz")
    );
    println!(
        "\nconversion results in {}\n",
        unit_converter::convert_units(10.0, "dBm", "GHz")
    );
    println!(
        "\nconversion results in {}\n",
        unit_converter::convert_units(3.0, "kHz", "Hz")
    );

    println!("\n==============================\n Showcasing Base Unit \n");
    let mut thing = db_element::DataThing::new_limited("Frequency","Hz","float",true,0.0,10e9);

    println!("\nInitial value of {} is {} {}\n", thing.name, thing.value, thing.base_unit);
    db_element::set_value(&mut thing, 1.0, "GHz");
    println!("\nValue of {} after setting to 1 GHz is {} {}\n", thing.name, thing.value, thing.base_unit);

    println!("\n==============================\n Showcasing Limits \n");
    println!("\nTrying to set {} to 20 GHz, which is above the max limit of 10 GHz\n", thing.name);
    db_element::set_value(&mut thing, 20.0, "GHz");
    println!("\nHz - Value of {} after trying to set to 20 GHz is {} {}\n", thing.name, thing.value, thing.base_unit);
    println!("\nGHz - Value of {} after trying to set to 20 GHz is {} {}\n", thing.name, unit_converter::convert_units(thing.value, &thing.base_unit, "GHz"), "GHz");








}

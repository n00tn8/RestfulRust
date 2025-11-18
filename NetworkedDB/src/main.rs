mod unit_converter;
fn main() {
    println!("Hello, world!");

    println!("Let's try some things");

    println!("conversion results in {}",unit_converter::convert_units(1.0,"Hz","Hz"));
    println!("conversion results in {}",unit_converter::convert_units(10.0,"kHz","GHz"));
    println!("conversion results in {}",unit_converter::convert_units(10.0,"MHz","GHertz"));
    println!("conversion results in {}",unit_converter::convert_units(10.0,"dBm","GHz"));
}

mod unit_converter;
fn main() {
    println!("Hello, world!");

    println!("Let's try some things");

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
}

pub fn parse_alter(alter_str: &str) -> Result<u32, String> {
    match alter_str.trim().parse::<u32>() {
        Ok(alter) if alter <= 120 => Ok(alter),
        Ok(_) => Err("Alter unplausibel".to_string()),
        Err(_) => Err("Keine gültige Zahl".to_string()),
    }
}
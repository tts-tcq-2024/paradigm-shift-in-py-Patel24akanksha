def battery_is_ok(temperature, soc, charge_rate):
    valid_temperature = 0 <= temperature <= 45
    valid_soc = 20 <= soc <= 80
    valid_charge_rate = charge_rate <= 0.8
    
    return valid_temperature and valid_soc and valid_charge_rate

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False

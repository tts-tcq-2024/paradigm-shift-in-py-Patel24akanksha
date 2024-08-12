def battery_is_ok(temperature, soc, ch_rate):
  temp_check(temperature)
  soc_check(soc)
  charge_rate_check(ch_rate)
  
def temp_check(temp):
  if temp < 0 or temp > 45:
    low_high_temp(temp)
    #print('Temperature is out of range!')
    #return False
  else:
    check_temp(temp)
    
def low_high_temp(temp):
  if temp <0:
    print('Temperature is LOW!')
  else:
    print('Temperature is HIGH!')

def check_temp(temp):
  if temp <=2.25 or temp >42.75:
    warning_check_temp(temp)
  else:
    print('Temperature is NORMAL')

def warning_check_temp(temp):
  if temp <=2.25:
    print('State of Charge is LOW WARNING')
  else:
    print('State of Charge is HIGH WARNING')
    
def soc_check(soc):
  if soc <=20 or soc > 80:
    low_high_soc(soc)
  else:
    check_soc(soc)

def low_high_soc(soc):
  if soc<20:
    print('State of Charge is LOW BREACH')
  else:
    print('State of Charge is HIGH BREACH')

def check_soc(soc):
  if soc <25 or soc >75:
    warning_check(soc)
  else:
    print('State of Charge is NORMAL')

def warning_check(soc):
  if soc <25:
    print('State of Charge is LOW WARNING')
  else:
    print('State of Charge is HIGH WARNING')
    
def charge_rate_check(ch):
  if ch > 0.8:
    print('Charge rate is out of range!')
  else:
    charge_rate_warning(ch)
    
def charge_rate_warning(ch):
  if ch> 0.6:
    print('Charge rate is WARNING')
  else:
    print('Charge rate is NORMAL')
    
if __name__ == '__main__':
  battery_is_ok(25, 70, 0.7)
  battery_is_ok(50, 85, 0)

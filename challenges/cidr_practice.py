def _convert_ip_to_int(ip: str) -> int:
  if not ip:
    raise ValueError('IP must not be empty')
  
  parts = ip.split('.')
  if len(parts) != 4:
    raise ValueError('IP address must have 4 parts')
  
  result = 0
  for part in parts:
    if not part or not part.isdigit():
      raise ValueError('IP address mut all be digits')
    
    part_value = int(part)
    if part_value < 0 or part_value > 255:
      raise ValueError('IP address part must be an integer between 0 and 255')
    
    result = (result << 8) | (part_value & 0xFF)

  return result


def _convert_mask(mask: str) -> int:
  if not mask:
    raise ValueError('Mask must be a digit')
  
  if not mask.isdigit():
    mask_val = _convert_ip_to_int(mask)
    
    binary_mask_val = bin(mask_val)[2:]
    if '01' in binary_mask_val:
      raise ValueError('Mask IP must have continuous 1 in the prefix')

    return mask_val
  
  base_len = int(mask)
  if base_len <= 0 or base_len >= 32:
    raise ValueError('Must must be a valid integer between 1 and 32')
  
  return int('1'*base_len + '0'*(32-base_len), 2)


class CIDR:
  def __init__(self, ip: str):
    parts = ip.split('/')
    if len(parts) < 0 or not parts[0] or not parts[1]:
      raise ValueError('The IP must follow the 123.123.123.123/23 format')
    
    self.ip_val = _convert_ip_to_int(parts[0])
    self.mask = _convert_mask(parts[1])

  def contains(self, ip: str) -> bool:
    ip_val = _convert_ip_to_int(ip)
    return (self.ip_val & self.mask) == (ip_val & self.mask)
    

cidr = CIDR('192.168.1.0/24')
print(cidr.contains('192.188.1.10'))

from typing import Union, Optional

def _ip_to_int(ip_str: str) -> int:
    """Converts a dotted-decimal IPv4 address string to a 32-bit integer."""
    try:
        octets = list(map(int, ip_str.split('.')))
        if len(octets) != 4 or any(not (0 <= o <= 255) for o in octets):
            raise ValueError("Invalid IPv4 address format or octet value.")
        
        # Perform bitwise shifts to combine octets into a single 32-bit integer
        return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]
    except Exception as e:
        raise ValueError(f"Invalid IP address format: {ip_str}") from e

def _int_to_ip(ip_int: int) -> str:
    """Converts a 32-bit integer back to a dotted-decimal IPv4 address string."""
    # Extract each octet using bitwise shifts and AND operations
    return ".".join([
        str((ip_int >> 24) & 0xFF),
        str((ip_int >> 16) & 0xFF),
        str((ip_int >> 8) & 0xFF),
        str(ip_int & 0xFF)
    ])

def _mask_to_prefix(mask_str: str) -> int:
    """Converts a dotted-decimal subnet mask string (e.g., '255.255.240.0') to a prefix length (e.g., 20)."""
    mask_int = _ip_to_int(mask_str)
    # Count the number of contiguous set bits (1s) in the mask's binary representation
    prefix_len = bin(mask_int).count('1')
    
    # Basic validation: ensure the mask is contiguous (no 0s followed by 1s)
    # By checking if the number of leading 1s equals the total 1s count
    mask_binary_str = bin(mask_int)[2:].zfill(32)
    if '01' in mask_binary_str:
         raise ValueError(f"Invalid non-contiguous subnet mask: {mask_str}")

    return prefix_len

def get_network_cidr(ip_address: str, subnet_mask: Optional[Union[str, int]] = None) -> str:
    """
    Manually converts an IPv4 address and its subnet mask (or prefix length) 
    into the canonical network address in CIDR notation (e.g., '192.168.1.0/24') 
    using only Python standard functions (no 'ipaddress' module).

    Args:
        ip_address: The host's IPv4 address (e.g., '192.168.1.42').
        subnet_mask: The subnet mask (e.g., '255.255.255.0') or the prefix
                     length (e.g., 24).

    Returns:
        The network address in CIDR notation (e.g., '192.168.1.0/24').
        Returns an error message string if the input is invalid.
    """
    try:
        ip_int = _ip_to_int(ip_address)
        prefix_len = 0
        
        if subnet_mask is None:
            # Fallback for when no mask is provided (uses classful default)
            first_octet = (ip_int >> 24) & 0xFF
            if 1 <= first_octet <= 126: # Class A
                prefix_len = 8
            elif 128 <= first_octet <= 191: # Class B
                prefix_len = 16
            elif 192 <= first_octet <= 223: # Class C
                prefix_len = 24
            else:
                # Assuming /32 for other ranges (multicast/reserved/private)
                prefix_len = 32 
        elif isinstance(subnet_mask, int) or (isinstance(subnet_mask, str) and subnet_mask.isdigit()):
            # subnet_mask is an integer prefix length (e.g., 24)
            prefix_len = int(subnet_mask)
            if not (0 <= prefix_len <= 32):
                raise ValueError("Prefix length must be between 0 and 32 for IPv4.")
        else:
            # subnet_mask is a dotted-decimal mask (e.g., '255.255.255.0').
            prefix_len = _mask_to_prefix(str(subnet_mask))

        # 1. Create the 32-bit mask integer from the prefix length
        # Example for /24: (1 << 24) - 1 results in 0x00FFFFFF. Invert this to get 0xFFFFFF00
        # The mask is 32 ones shifted by the number of host bits (32 - prefix_len)
        mask_int = ((1 << prefix_len) - 1) << (32 - prefix_len)
        
        # 2. Perform the bitwise AND operation to get the Network Address
        network_int = ip_int & mask_int

        # 3. Format the result
        network_address = _int_to_ip(network_int)
        
        return f"{network_address}/{prefix_len}"

    except ValueError as e:
        return f"Error: Invalid IP or Subnet Mask provided. Details: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Examples ---

# Example 1: Using a prefix length
ip1 = "172.16.5.10"
prefix1 = 20
print(f"IP: {ip1}, Prefix: /{prefix1} -> CIDR: {get_network_cidr(ip1, prefix1)}")

# Example 2: Using a dotted-decimal subnet mask
ip2 = "192.168.1.42"
mask2 = "255.255.255.0"
print(f"IP: {ip2}, Mask: {mask2} -> CIDR: {get_network_cidr(ip2, mask2)}")

# Example 3: A non-standard subnet (sub-netted Class B)
ip3 = "130.10.10.13"
mask3 = "255.255.240.0" # This is a /20 mask
print(f"IP: {ip3}, Mask: {mask3} -> CIDR: {get_network_cidr(ip3, mask3)}")

# Example 4: Invalid Input (Invalid Octet)
ip_invalid_octet = "256.0.0.1"
mask_invalid_octet = 24
print(f"IP: {ip_invalid_octet}, Prefix: /{mask_invalid_octet} -> CIDR: {get_network_cidr(ip_invalid_octet, mask_invalid_octet)}")

# Example 5: Invalid Input (Non-contiguous mask)
ip_invalid_mask = "10.0.0.1"
mask_invalid_mask = "255.254.255.0"
print(f"IP: {ip_invalid_mask}, Mask: {mask_invalid_mask} -> CIDR: {get_network_cidr(ip_invalid_mask, mask_invalid_mask)}")

# Example 6: Just the IP (uses classful assumption - Class C in this case)
ip6 = "192.1.2.3"
print(f"IP: {ip6}, No Mask -> CIDR: {get_network_cidr(ip6)}")

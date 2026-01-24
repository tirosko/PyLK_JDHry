import math

# Function to calculate the angle BCD in degrees
def calculate_angle_BCD():
    # Given conditions
    # Let the length of side AD and diagonal BD be equal to 'x'
    x = 1  # You can set this to any positive value
    # Let the length of side DC be 'y'
    y = math.sqrt(2) * x  # Since BD is perpendicular to DC

    # Using the right triangle BDC to find angle BCD
    # tan(BCD) = opposite / adjacent = DC / BD
    angle_BCD_rad = math.atan(y / x)
    angle_BCD_deg = math.degrees(angle_BCD_rad)

    return angle_BCD_deg

# Main function to execute the calculation
if __name__ == '__main__':
    angle_BCD = calculate_angle_BCD()
    print(f'Veľkosť uhla BCD je: {angle_BCD:.2f}°')
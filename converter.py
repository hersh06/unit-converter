# Unit Converter Program
# Author: Hershey (@hersh06)
# Description: Command-line tool for converting between temperature, distance, weight, and speed units.

# ------------------------------
# Temperature Conversion
# ------------------------------
def temp_convert():
    # prompt user for type of temperature conversion
    temp_input = input("What conversion woud you like to make?\n(A) ˚C to ˚F\n(B) ˚F to ˚C\n")
    if temp_input.lower() == "a":
        try:
            # Get temperature in Celsius from user
            c_temp = float(input("Enter temperature in ˚C: "))
            # Convert Celsius to Fahrenheit
            f_conv = (c_temp * 9/5) + 32
            print(f"{c_temp}˚C = {f_conv:.2f}˚F\n")
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a valid number.")
    elif temp_input.lower() == "b":
        try:
            # Get temperature in Fahrenheit from user
            f_temp = float(input("Enter temperature in ˚F: "))
            # Convert Fahrenheit to Celsius
            c_conv = (f_temp - 32) * 5/9
            print(f"{f_temp}˚F = {c_conv:.2f}˚C\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        # Handle invalid menu selection
        print("Error: Invalid Input")
        return()


# ------------------------------
# Distance Conversion
# ------------------------------
def dist_convert():
    # Prompt user for type of distance conversion
    dist_input = input("What conversion would you like to make?\n(A) Meters to Feet\n(B) Feet to Meters\n")
    if dist_input.lower() == "a":
        try:
            # Get distance in meters from user
            m_dist = float(input("Enter distance in Meters: "))
            # Convert meters to feet
            ft_conv = (m_dist * 3.28084)
            print(f"{m_dist} m = {ft_conv:.2f} ft\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif dist_input.lower() == "b":
        try:
            # Get distance in feet from user
            ft_dist = float(input("Enter distance in Feet: "))
            # Convert feet to meters
            m_conv = (ft_dist / 3.28084)
            print(f"{ft_dist} ft = {m_conv:.2f} m\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Error: Invalid Input")
        return()


# ------------------------------
# Weight Conversion
# ------------------------------
def wt_convert():
    # Prompt user for type of weight conversion
    wt_input = input("What conversion would you like to make?\n(A) Kilograms to Pounds\n(B) Pounds to Kilograms\n")
    if wt_input.lower() == "a":
        try:
            # Get weight in Kilograms from user
            kg_wt = float(input("Enter weight in Kilograms: "))
            # Convert Kilograms to Pounds
            lbs_conv = (kg_wt * 2.20462)
            print(f"{kg_wt} Kg = {lbs_conv:.2f} Lbs\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif wt_input.lower() == "b":
        try:
            # Get weight in Pounds from user
            lbs_wt = float(input("Enter weight in Pounds: "))
            # Convert Pounds to Kilograms
            kg_conv = (lbs_wt / 2.20462)
            print(f"{lbs_wt} Lbs = {kg_conv:.2f} Kg\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Error: Invalid Input")
        return()


# ------------------------------
# Speed Cinversion
# ------------------------------
def spd_convert():
    # Prompt user for type of speed conversion
    spd_input = input("What conversion would you like to make?\n(A) KMPH to MPH\n(B) MPH to KMPH\n")
    if spd_input.lower() == "a":
        try:
            # Get speed in KMPH from user
            kmph_spd = float(input("Enter speed in KMPH: "))
            # Convert KMPH to MPH
            mph_conv = (kmph_spd * 0.621371)
            print(f"{kmph_spd} KMPH = {mph_conv:.2f} MPH\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif spd_input.lower() == "b":
        try:
            # Get speed in MPH from user
            mph_spd = float(input("Enter speed in MPH: "))
            # Convert MPH to KMPH
            kmph_conv = (mph_spd / 0.621371)
            print(f"{mph_spd} MPH = {kmph_conv:.2f} KMPH\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Error: Invalid Input")
        return()


# ------------------------------
# Main Program Loop
# ------------------------------
def main():
    while True:
        # Display main menu ad get user selection
        user_input = input("Choose what units you would like to convert:\n(A) Temperature\n(B) Distance\n(C) Weight\n(D) Speed\n(E) Exit\n")
        if user_input.lower() in ["e", "done"]:
            # Exit the program
            print("Goodbye!")
            break
        elif user_input.lower() == "a":
            temp_convert()
        elif user_input.lower() == "b":
            dist_convert()
        elif user_input.lower() == "c":
            wt_convert()
        elif user_input.lower() == "d":
            spd_convert()
        else:
            # Handle invalid menu selection
            print("Error: Invalid input. Please choose from the available options or type 'done' to exit.")


# Run the program
main()
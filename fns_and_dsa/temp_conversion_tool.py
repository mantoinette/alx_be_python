# Define global conversion factors (ensure consistent indentation)
FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)  # Factor to convert Celsius to Fahrenheit


def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit.

  Returns:
      The temperature converted to Celsius.
  """
  return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature converted to Fahrenheit.
  """
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


def main():
  while True:
    try:
      # Get user input for temperature and unit
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      # Call appropriate conversion function based on unit
      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "°C"
        converted_unit_label = "°F"
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = "°F"
        converted_unit_label = "°C"
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      # Display the converted temperature
      print(f"{temperature:.1f}{unit_label} is {converted_temp:.1f}{converted_unit_label}")
      break

    except ValueError as e:
      print(f"Error: {e}")
      print("Please enter a numeric value and a valid unit (C or F).")


if __name__ == "__main__":
  main()

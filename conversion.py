import pandas as pd

def celsius_to_kelvin(celsius):
    """
    Function to return Kelvin degrees from Celsius input.
    
    :param celsius: Float with temperature in Celsius.

    :returns: the temperature converted to kelvin
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return celsius * 9./5 + 32

def mean_temperature(data):
    """
    Get the mean temperature.

    Args:
        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.

    Returns:
        The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return sum(temperatures)/len(temperatures)

def get_spreadsheet_columns(file_loc, print_columns=False):
    """Gets and prints the spreadsheet's header columns
    
    Args:
       file_loc (str): The file location of the spreadsheet
       print_columns (bool, optional) : A flag used to print the columns to the console (default is False)

    Returns:
       a list of strings used that are the header columns
    """
    file_data = pd.read_excel(file_loc)
    column_headers = list(file_data.columns.values)
    if print_columns:
        print("\n".join(column_headers))
    return column_headers
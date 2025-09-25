from . import *

class DateTimeUtils:
    """
    This class provides utility functions for working with dates and times.
    """
    @staticmethod
    def get_current_datetime():
        """
        Returns the current date and time formatted as "DD-MM-YYYY__HH-MM-SS".

        Returns:
            str: The current date and time in the specified format.
        """
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y__%H-%M-%S")
        return date_time
    
    @staticmethod
    def format_date_sap(date_obj, format_str='%d.%m.%Y'):
        """
        Formate a date object according to the specified format string.

        Args:
            date_obj (datetime.date): The date object to be formatted.
            format_str (str, optional): The format string to use for formatting. Defaults to '%d.%m.%Y' (SAP standard).
                                        The format string follows the standard strftime directives (https://strftime.org/)

        Returns:
            _type_: _description_
        """
        return date_obj.strftime(format_str)
    
    @staticmethod
    def get_date_range():
        """
        Calculates the dates 30 days before the current one, the current 
        one and 180 days after the current one,formatting them according 
        to the SAP standard.

        Returns:
            tuple: A tuple containing the three formatted dates.
        """

        present_day = date.today()
        day_before = present_day - timedelta(days=30)
        day_after = present_day + timedelta(days=180)

        formatted_dates = (
            DateTimeUtils.format_date_sap(present_day),
            DateTimeUtils.format_date_sap(day_before),
            DateTimeUtils.format_date_sap(day_after)
        )

        return formatted_dates


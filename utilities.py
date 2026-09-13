from datetime import datetime


def format_date(date):
    """Format a date from YYYY-MM-DD to DD-MM-YYYY."""

    date = datetime.strptime(date, "%Y-%m-%d")  # noqa: DTZ007

    return date.strftime("%d-%m-%Y")

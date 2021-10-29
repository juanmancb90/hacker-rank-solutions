from datetime import datetime


def timeConversion(s: str) -> str:
    """[summary]

    Args:
        s (str): [description]

    Returns:
        str: [description]
    """
    format_in = "%I:%M:%S%p"
    format_out = "%H:%M:%S"
    initial = datetime.strptime(s, format_in)
    final = datetime.strftime(initial, format_out)
    print(final)


if __name__ == "__main__":
    timeConversion("12:01:00PM")
    timeConversion("12:01:00AM")

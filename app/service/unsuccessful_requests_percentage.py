from app.service.read_log_file import LogFile


def unsuccessful_percentage() -> dict:
    """
        Generate a report with percentage number of unsuccessful requests based on the status code of requests.

        Returns:
        dict: A dictionary containing detailed information.

        Example:
        {
          "unsuccessful_percentage": 0.6473691733583815
        }
    """
    log_file = LogFile()

    status_codes = log_file.extract_status_codes()

    # Count the occurrences of unsuccessful requests (status codes not starting with 2 or 3)
    unsuccessful_requests = sum(1 for code in status_codes if not code.startswith(('2', '3')))

    # Calculate the percentage of unsuccessful requests
    total_requests = len(status_codes)
    unsuccessful_percentage = (unsuccessful_requests / total_requests) * 100 if total_requests > 0 else 0

    # Create a dictionary for the JSON response
    result = {'unsuccessful_percentage': unsuccessful_percentage}

    return result


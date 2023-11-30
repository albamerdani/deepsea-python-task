from service.read_log_file import LogFile


def unsuccessful_percentage():
    # Extract status codes using a regular expression
    # Assuming the format is "HTTP/1.0" followed by a space and a 3-digit status code
    status_codes = LogFile.extract_status_codes()

    # Count the occurrences of unsuccessful requests (status codes not starting with 2 or 3)
    unsuccessful_requests = sum(1 for code in status_codes if not code.startswith(('2', '3')))

    # Calculate the percentage of unsuccessful requests
    total_requests = len(status_codes)
    unsuccessful_percentage = (unsuccessful_requests / total_requests) * 100 if total_requests > 0 else 0

    # Create a dictionary for the JSON response
    result = {'unsuccessful_percentage': unsuccessful_percentage}

    return result


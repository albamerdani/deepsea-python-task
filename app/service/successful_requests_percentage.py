from service.read_log_file import LogFile


def success_percentage()-> dict:
    log_file = LogFile()
    # Extract status codes using a regular expression
    # Assuming the format is "HTTP/1.0" followed by a space and a 3-digit status code
    status_codes = log_file.extract_status_codes()

    # Count the occurrences of successful requests (status codes 2xx and 3xx)
    successful_requests = sum(1 for code in status_codes if code.startswith(('2', '3')))

    # Calculate the percentage of successful requests
    total_requests = len(status_codes)
    success_percentage = (successful_requests / total_requests) * 100 if total_requests > 0 else 0

    # Create a dictionary for the JSON response
    result = {'success_percentage': success_percentage}

    return result

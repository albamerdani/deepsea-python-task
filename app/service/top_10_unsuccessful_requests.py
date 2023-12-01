from app.service.read_log_file import LogFile
from collections import Counter
import re


def top_10_unsuccessful() -> dict:
    """
        Generate a detailed report of the top 10 unsuccessful requests based on the status code of requests.

        Returns:
        dict: A dictionary containing detailed information about the top 10 unsuccessful requests.
        For each entry is the path name and number of requests to those.

        Example:
        {
          "top_10_unsuccessful_requests": [
            {
              "count": 601,
              "path": "/images/NASA-logosmall.gif"
            },
            {
              "count": 476,
              "path": "/images/KSC-logosmall.gif"
            },
            {
              "count": 448,
              "path": "/images/MOSAIC-logosmall.gif"
            },
            {
              "count": 395,
              "path": "/images/WORLD-logosmall.gif"
            },
            {
              "count": 389,
              "path": "/images/ksclogo-medium.gif"
            },
            {
              "count": 383,
              "path": "/images/USA-logosmall.gif"
            },
            {
              "count": 256,
              "path": "/ksc.html"
            },
            {
              "count": 246,
              "path": "/history/apollo/images/apollo-logo1.gif"
            },
            {
              "count": 238,
              "path": "/images/launch-logo.gif"
            },
            {
              "count": 194,
              "path": "/"
            }
          ]
        }
    """
    log_file = LogFile()
    log_data = log_file.read_log_file()

    status_codes = log_file.extract_status_codes()

    paths = []
    # Extract paths requested by the current host
    for host in log_data:
        try:
            pattern = r'"GET\s([^"]+)\sHTTP/1.0"'
            match = re.search(pattern, host)
            if match:
                # Count the occurrences of each path
                path = match.group(1)
                paths.append(path)
        except Exception as e:
            return [{'error': str(e), 'line': host}]

    # Filter out successful requests (status codes starting with 2 or 3)
    unsuccessful_requests = [path for code, path in zip(status_codes, paths) if not code.startswith(('2', '3'))]

    # Count the occurrences of each unsuccessful request
    unsuccessful_counts = Counter(unsuccessful_requests)

    # Get the top 10 unsuccessful requests
    top_10_unsuccessful_requests = unsuccessful_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top_10_unsuccessful_requests': [{'path': path, 'count': count}
                                               for path, count in top_10_unsuccessful_requests]}

    return result


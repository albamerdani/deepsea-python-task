from service.read_log_file import LogFile
from collections import Counter


def top_10_unsuccessful() ->dict:
    status_codes = LogFile.extract_status_codes()

    paths = LogFile.extract_paths()

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


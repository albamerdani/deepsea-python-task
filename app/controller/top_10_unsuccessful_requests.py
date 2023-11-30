import re
from flask import Flask, jsonify
from collections import Counter

app = Flask(__name__)


@app.route('/top10Unsuccessful')
def top_10_unsuccessful():
    log_file_path = 'D:\\Merdani_ITServices\\DeepSea\\deepsea-python-task\\app\\http_log_file\\new_final_final_01.log'  # Update with the actual path to your log file

    # Read the log file and extract status codes and corresponding paths
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()

    # Extract status codes and paths using regular expressions
    # Assuming the format is "HTTP/1.0" followed by a space and a 3-digit status code
    status_codes = []
    # Extract requested pages using regular expressions
    for line in log_data:
        pattern = r'HTTP/1.0" (\d{3})'
        match = re.search(pattern, line)
        if match:
            # Count the occurrences of each status code
            status_code = match.group(1)
            status_codes.append(status_code)

    paths = []
    for line in log_data:
        pattern = r'"GET\s([^"]+)\sHTTP/1.0"'
        match = re.search(pattern, line)
        if match:
            # Count the occurrences of each path
            path = match.group(1)
            paths.append(path)

    # Filter out successful requests (status codes starting with 2 or 3)
    unsuccessful_requests = [path for code, path in zip(status_codes, paths) if not code.startswith(('2', '3'))]

    # Count the occurrences of each unsuccessful request
    unsuccessful_counts = Counter(unsuccessful_requests)

    # Get the top 10 unsuccessful requests
    top_10_unsuccessful_requests = unsuccessful_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top10_unsuccessful_requests': [{'path': path, 'count': count} for path, count in top_10_unsuccessful_requests]}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

import re
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/successPercentage')
def success_percentage():
    log_file_path = 'D:\\Merdani_ITServices\\DeepSea\\deepsea-python-task\\app\\http_log_file\\new_final_final_01.log'  # Update with the actual path to your log file

    # Read the log file and extract status codes
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()

    # Extract status codes using a regular expression
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

    # Count the occurrences of successful requests (status codes 2xx and 3xx)
    successful_requests = sum(1 for code in status_codes if code.startswith(('2', '3')))

    # Calculate the percentage of successful requests
    total_requests = len(status_codes)
    success_percentage = (successful_requests / total_requests) * 100 if total_requests > 0 else 0

    # Create a dictionary for the JSON response
    result = {'success_percentage': success_percentage}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

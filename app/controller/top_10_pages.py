from flask import Flask, jsonify
from collections import Counter
import re
from pathlib import Path


app = Flask(__name__)


@app.route('/top10pages')
def top_10_pages():
    cwd = Path.cwd()
    print(cwd)
    path = Path("app", "http_log_file", "new_final_final_01.log")
    print(path)

    log_file_path = 'D:\\Merdani_ITServices\\DeepSea\\deepsea-python-task\\app\\http_log_file\\new_final_final_01.log'  # path to your log file

    # Read the log file and extract requested pages
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()

    pages = []
    # Extract requested pages using regular expressions
    for line in log_data:
        pattern = r'GET /([^ ]+.html) HTTP/1.0'
        match = re.search(pattern, line)
        if match:
            page_name = match.group(1)
            pages.append(page_name)

    # Count the occurrences of each page
    page_counts = Counter(pages)

    # Get the top 10 pages
    top_10_pages = page_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top10_pages': [{'page': page, 'requests': count} for page, count in top_10_pages]}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

import re
import os
from dotenv import load_dotenv

"""
@author Alba Merdani
Python file with methods to read the log file and extract hosts, pages, paths of requests, status codes
using regular expressions.
"""


class LogFile:
    # Load environment variables from .env file
    load_dotenv()

    # Get the file path from the environment variable
    log_file_path = os.getenv("FILE_PATH")

    # Check if the file path is available
    if log_file_path:
        print(f"File path from .env: {log_file_path}")
    else:
        print("File path not found in .env file.")

    #log_file_path = 'D:\\Merdani_ITServices\\DeepSea\\new_final_final_01.log'

    def read_log_file(self):
        try:
            with open(self.log_file_path, 'r') as file:
                return file.readlines()
        except Exception as e:
            return [{'error': str(e), 'line': None}]

    def extract_pages(self) -> list:
        """
            Read the log file to extract data. Generate a list of page names.

            Returns:
            list: Return a list of page names ending with .html extension, using regular expression
        """
        log_data = self.read_log_file()

        pages = []
        # Extract requested pages using regular expressions
        for line in log_data:
            try:
                pattern = r'GET /([^ ]+.html) HTTP/1.0'
                match = re.search(pattern, line)
                if match:
                    page_name = match.group(1)
                    pages.append(page_name)
            except Exception as e:
                return [{'error': str(e), 'line': line}]
        return pages

    def extract_hosts(self) -> list:
        """
            Read the log file to extract data. Generate a list of hosts.

            Returns:
            list: Return a list of hosts(IP or domain name), using regular expression
        """
        # Extract requested hosts using regular expressions
        log_data = self.read_log_file()
        hosts = []
        pattern = r'^(\S+)\s+-\s+-\s+\['
        for line in log_data:
            try:
                host_match = re.search(pattern, line)
                if host_match:
                    # Count the occurrences of each host
                    host = host_match.group(1)
                    hosts.append(host)
            except Exception as e:
                return [{'error': str(e), 'line': line}]
        return hosts

    def extract_status_codes(self) -> list:
        """
            Read the log file to extract data. Generate a list of status codes.

            Returns:
            list: Return a list of status codes, using regular expression
        """
        log_data = self.read_log_file()
        # Extract status codes and paths using regular expressions
        # Assuming the format is "HTTP/1.0" followed by a space and a 3-digit status code
        status_codes = []
        # Extract requested pages using regular expressions
        for line in log_data:
            try:
                pattern = r'HTTP/1.0" (\d{3})'
                match = re.search(pattern, line)
                if match:
                    # Count the occurrences of each status code
                    status_code = match.group(1)
                    status_codes.append(status_code)
            except Exception as e:
                return [{'error': str(e), 'line': line}]
        return status_codes

    def extract_paths(self, host_entries) -> list:
        """
            Read the log file to extract data. Generate a list of request paths.

            Returns:
            list: Return a list of request paths, using regular expression
        """
        # Extract requested paths using regular expressions
        paths = []
        # Extract paths requested by the current host
        for host in host_entries:
            try:
                pattern = r'"GET\s([^"]+)\sHTTP/1.0"'
                match = re.search(pattern, host)
                if match:
                    # Count the occurrences of each path
                    path = match.group(1)
                    paths.append(path)
            except Exception as e:
                return [{'error': str(e), 'line': host}]
        return paths

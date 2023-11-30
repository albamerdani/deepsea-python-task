import re
"""
@author Alba Merdani
Python file with methods to read the log file and extract hosts, pages, paths of requests, status codes using regular expressions
"""


class LogFile:

    log_file_path = 'D:\\Merdani_ITServices\\DeepSea\\new_final_final_01.log'

    def read_log_file(self):
        try:
            with open(self.log_file_path, 'r') as file:
                return file.readlines()
        except Exception as e:
            return [{'error': str(e), 'line': None}]

    def extract_pages(self):
        log_data = self.read_log_file()

        pages = []
        # Extract requested pages using regular expressions
        for line in log_data:
            pattern = r'GET /([^ ]+.html) HTTP/1.0'
            match = re.search(pattern, line)
            if match:
                page_name = match.group(1)
                pages.append(page_name)
        return pages

    def extract_hosts(self):
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

    def extract_status_codes(self):
        log_data = self.read_log_file()
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
        return status_codes

    def extract_paths(self, host_entries):
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

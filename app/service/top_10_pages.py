from collections import Counter
from service.read_log_file import LogFile


def top_10_pages() ->dict:
    pages = LogFile.extract_pages()

    # Count the occurrences of each page
    page_counts = Counter(pages)

    # Get the top 10 pages
    top_10_pages = page_counts.most_common(10)

    # Create a dictionary for the JSON response
    result = {'top10_pages': [{'page': page, 'requests': count} for page, count in top_10_pages]}

    return result

import csv
import re

log_file_path = 'gb.log'
csv_file_path = 'data.csv'

# Define regular expressions to extract information
url_regex = r'Trying site: (.*?)$'
accept_info_regex = r'INFO:root:Finding consent element...'
accept_element_regex = r'INFO:root:Element found: (\w+) with text: (.+)$'
reject_info_regex = r'INFO:root:Finding reject element...'
reject_element_regex = r'INFO:root:Element found: (\w+) with text: (.+)$'
error_regex = r'ERROR:root:(.*)'

# Initialize the CSV data list
csv_data = [['index', 'url', 'accept-found', 'accept-type', 'accept-text', 'reject-found', 'reject-type', 'reject-text', 'error']]

# Read the log file
with open(log_file_path, 'r') as log_file:
    lines = log_file.readlines()

# Initialize variables
index = 0
url = ''
accept_found = False
accept_type = ''
accept_text = ''
reject_found = False
reject_type = ''
reject_text = ''
error = False

# Process each line of the log file
for line in lines:
    line = line.strip()

    # Extract URL
    url_match = re.search(url_regex, line)
    if url_match:
        if url:
            # Append the extracted data to the CSV data list
            accept_found = bool(accept_type)
            reject_found = bool(reject_type)
            csv_data.append([index, url, accept_found, accept_type, accept_text, reject_found, reject_type, reject_text, error])
            index += 1

        url = url_match.group(1)
        accept_found = False
        accept_type = ''
        accept_text = ''
        reject_found = False
        reject_type = ''
        reject_text = ''
        error = False

    # Check for accept element info
    accept_info_match = re.search(accept_info_regex, line)
    if accept_info_match:
        accept_found = True
        reject_found = False

    # Extract accept element
    accept_element_match = re.search(accept_element_regex, line)
    if accept_element_match and accept_found:
        accept_type = accept_element_match.group(1)
        accept_text = accept_element_match.group(2)

    # Check for reject element info
    reject_info_match = re.search(reject_info_regex, line)
    if reject_info_match:
        reject_found = True
        accept_found = False

    # Extract reject element
    reject_element_match = re.search(reject_element_regex, line)
    if reject_element_match and reject_found:
        reject_type = reject_element_match.group(1)
        reject_text = reject_element_match.group(2)

    # Check for error
    error_match = re.search(error_regex, line)
    if error_match:
        error = True

# Append the last extracted data to the CSV data list
accept_found = bool(accept_type)
reject_found = bool(reject_type)
csv_data.append([index, url, accept_found, accept_type, accept_text, reject_found, reject_type, reject_text, error])

# Write the CSV data to a file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)

print("CSV file has been created successfully.")
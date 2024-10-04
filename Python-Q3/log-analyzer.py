import re
from collections import defaultdict

# Function to parse individual log entries using a regular expression
def parse_logs(logs):
    """
    Parses a single log entry and extracts relevant information.

    Args:
        logs (str): A string representing one line from the log file.

    Returns:
        tuple: Contains the pod name, request path, response code, and bytes sent.
               Returns None if the log entry doesn't match the expected pattern.
    """
    # Regular expression pattern to match a typical log entry structure , I used the help of AI to generate it
    log_pattern = re.compile(r'(\S+)\s+(\S+)\s+(\S+)\s+-\s+-\s+\[(.*?)\]\s+"GET\s+(\S+)\s+HTTP/[^"]+"\s+(\d+)\s+(\d+)')
    
    # Attempt to match the log entry to the pattern
    match = log_pattern.match(logs)
    
    # If a match is found, extract the necessary fields
    if match:
        pod_name = match.group(1)           # The pod name where the request was processed
        request_path = match.group(5)       # The path of the request
        response_code = int(match.group(6)) # The HTTP response code
        bytes_sent = int(match.group(7))    # The number of bytes sent in the response
        return pod_name, request_path, response_code, bytes_sent
    
    # If the log entry doesn't match the pattern, return None
    return None

# Function to process a list of logs and summarize the data
def process_logs(logs):
    """
    Processes a list of log entries to compute summaries such as requests per pod, 
    response code distribution, and total bytes sent.

    Args:
        logs (list): A list of log entries (strings).

    Returns:
        dict: Contains summaries for requests per pod, response codes, total bytes sent, and unique paths.
    """
    # Initialize defaultdicts for counting and summarizing log data
    requests_per_pod = defaultdict(int)          # Stores the number of requests per pod
    response_code_summary = defaultdict(int)     # Stores the count of each HTTP response code
    total_bytes_sent_per_pod = defaultdict(int)  # Tracks the total bytes sent per pod
    unique_request_paths = set()                 # Stores unique request paths

    # Loop through each log entry in the list
    for log in logs:
        # Parse the log entry using the parse_logs function
        parsed_entry = parse_logs(log)
        
        # If the log entry is valid, update the summaries
        if parsed_entry:
            pod_name, request_path, response_code, bytes_sent = parsed_entry
            
            # 1. Increment the request count for the respective pod
            requests_per_pod[pod_name] += 1

            # 2. Increment the count for the response code
            response_code_summary[response_code] += 1

            # 3. Add the bytes sent to the total for the respective pod
            total_bytes_sent_per_pod[pod_name] += bytes_sent

            # 4. Add the request path to the set of unique paths
            unique_request_paths.add(request_path)
    
    # Return the summaries as a dictionary
    return {
        'requests_per_pod': requests_per_pod,
        'response_code_summary': response_code_summary,
        'total_bytes_sent_per_pod': total_bytes_sent_per_pod,
        'unique_request_paths': unique_request_paths
    }

# Function to read log entries from a file
def read_logs(file_path):
    """
    Reads log entries from a specified file.

    Args:
        file_path (str): The path to the log file.

    Returns:
        list: A list of strings where each string is a log entry (line).
    """
    # Open the file and read all lines into a list
    with open(file_path, 'r') as log_file:
        logs = log_file.readlines()
    return logs

# Function to display the summary results
def print_output(summary):
    """
    Prints the processed summary results from the logs.

    Args:
        summary (dict): Contains the summarized data such as requests per pod and response code counts.
    """
    # Print total requests per pod
    print("\n--- Total Requests per Pod ---")
    for pod, count in summary['requests_per_pod'].items():
        print(f"Pod name: {pod}, Total Requests: {count}")

    # Print the summary of response codes
    print("\n--- Response Code Summary ---")
    for code, count in summary['response_code_summary'].items():
        print(f"Response Code: {code}, Count: {count}")

    # Print total bytes sent per pod
    print("\n--- Total Bytes Sent per Pod ---")
    for pod, bytes_sent in summary['total_bytes_sent_per_pod'].items():
        print(f"Pod: {pod}, Total Bytes Sent: {bytes_sent}")

    # Print unique request paths
    print("\n--- Unique Request Paths ---")
    for path in summary['unique_request_paths']:
        print(f"Path: {path}")

# Main function to orchestrate the log processing workflow
def main(log_file_path):
    """
    Main function to handle the log file processing and display results.

    Args:
        log_file_path (str): The path to the log file to be processed.
    """
    # Step 1: Read log entries from the file
    logs = read_logs(log_file_path)

    # Step 2: Process the log entries to generate a summary
    summary = process_logs(logs)

    # Step 3: Print the summarized results
    print_output(summary)

# Example usage (update with your actual log file path)
if __name__ == "__main__":
    log_file_path = './fp-sre-challenge.log'  # Change this to the actual path of the log file
    main(log_file_path)

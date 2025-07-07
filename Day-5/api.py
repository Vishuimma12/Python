import json      # Used to format and print the JSON response nicely
import requests  # For sending HTTP requests to the iTunes API
import sys       # To access command-line arguments and exit the program


# Check if the user provided exactly one argument (excluding the script name)
if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <search_term>")  # Exit if usage is incorrect

# Get the search term entered by the user from command-line argument
search_term = sys.argv[1]

# Construct the API URL with:
# - entity=song: only return songs
# - limit=50: limit the result to 50 entries
# - term=<search_term>: the term to search for
url = f"https://itunes.apple.com/search?entity=song&limit=50&term={search_term}"


# Send a GET request to the iTunes Search API
response = requests.get(url)


# Check if the request was successful (HTTP status code 200)
if response.status_code != 200:
    sys.exit("Error fetching data from iTunes API")  # Exit on failure


try:
    # Attempt to parse the response content as JSON
    data = response.json()

    # Pretty-print the JSON data with indentation
    print(json.dumps(data, indent=2))

except ValueError:
    # Handle case where response is not valid JSON
    sys.exit("Failed to parse JSON response")


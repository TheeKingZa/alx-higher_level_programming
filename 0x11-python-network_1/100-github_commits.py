#!/usr/bin/python3
"""
Lists of 10 most recent commits
on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    # Construct the URL for the GitHub API using command-line arguments
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Make an HTTP GET request to the GitHub API
    r = requests.get(url)

    # Parse the JSON response into a list of commits
    commits = r.json()

    try:
        # Iterate through the first 10 commits and print relevant information
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        # Handle the case where there are fewer than 10 commits
        pass

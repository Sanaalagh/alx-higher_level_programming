#!/usr/bin/python3
"""
Uses the GitHub API to list 10 commits
(from the most recent to oldest) of a repository by a user
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")

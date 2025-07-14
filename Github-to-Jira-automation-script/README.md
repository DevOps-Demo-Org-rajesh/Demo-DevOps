Script.py file contains the python script to create the Epic work item type in the Jira when a comment(/Jira, /JIRA, /jira) is added inside the Issue.

1. Python Flask API to integrate GitHub Issues with Jira.

2. Triggers when someone comments /jira, /JIRA, or /Jira on a GitHub Issue.

3. A GitHub webhook sends the comment data to the Flask API.

4. The API creates a Jira Epic using the Jira REST API.

5. Requires a GitHub account and a Jira Cloud account.

6. Webhook should listen to the issue_comment event in GitHub.

7. Built with Flask and requests libraries.

8. Use ngrok for local testing or deploy on a public server.

9. Jira API token, email, and project key are needed in the script.

10. Useful for automating Jira ticket creation directly from GitHub discussions.

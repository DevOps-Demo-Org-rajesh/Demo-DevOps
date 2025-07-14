from flask import Flask,request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/createJiraTicket", methods=['POST'])

def createJiraTicket():

  github_payload = request.json

  if github_payload["comment"]["body"] == "/Jira" or github_payload["comment"]["body"] == "/JIRA" or github_payload["comment"]["body"] == "/jira":
    url = "https://<JIRA-Account-Name>.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("<mail-address>", "<PAT-Token>")

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "fields": {
        "issuetype": {
          "id": "<Issue-Tpye-Id>"
        },
        "project": {
          "key": "<Project-Key>"
        },
        "summary": github_payload["issue"]["title"],
      }
    })

    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
    )
    return (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

@app.route("/hello", methods=['GET'])
def hello():
  return "hello world"

app.run('0.0.0.0', port=3500)

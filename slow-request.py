"""
Module to check for available tickets with a minimum of 10 seconds delay
"""

import requests
import time
import webbrowser
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://atleta.cc/api/graphql"

HEADERS = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,nl;q=0.8,de;q=0.7",
    "atleta-locale": "en",
    "atleta-session-id": "",  # Your session ID
    "content-type": "application/json",
    "origin": "https://atleta.cc",
    "priority": "u=1, i",
    "referer": "https://atleta.cc/",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-fetch-storage-access": "active",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    ),
}

# GraphQL query payload copied from the cURL request
DATA = {
    "operationName": "GetRegistrationsForSale",
    "variables": {"id": "zRLhtOq7pOcB", "tickets": None, "limit": -1},
    "query": """
    query GetRegistrationsForSale($id: ID!, $tickets: [String!], $limit: Int!) {
      event(id: $id) {
        id
        registrations_for_sale_count
        filtered_registrations_for_sale_count: registrations_for_sale_count(
          tickets: $tickets
        )
        tickets_for_resale {
          id
          title
        }
        registrations_for_sale(tickets: $tickets, limit: $limit) {
          id
          ticket {
            id
            title
          }
          resale {
            available
            total_amount
            fee
            public_url
          }
        }
      }
    }""",
}

def check_tickets(counter):
    """Sends request through a proxy and checks for available tickets"""
    
    response = requests.post(
          URL, headers=HEADERS, json=DATA, timeout=10
      )

    if response.status_code == 200:
        data = response.json()
        event = data.get("data", {}).get("event", {})

        if event and event.get("registrations_for_sale"):
            available_tickets = [
                ticket for ticket in event["registrations_for_sale"]
                if ticket["resale"]["available"]
            ]

            if available_tickets:
                print(f"\nTicket(s) available! Request: {counter}")
                for ticket in available_tickets:
                    ticket_title = ticket["ticket"]["title"]
                    price = ticket["resale"]["total_amount"]
                    url = ticket["resale"]["public_url"]
                    print(f"- {ticket_title}: €{price} | [Buy Here]({url})")
                    webbrowser.open(url)  # Automatically opens in the default browser
            else:
                print(f"No available tickets. Request: {counter}")

        else:
          print(f"No tickets available. Request: {counter}")

    else:
        print(f"Error {response.status_code}: {response.text}")
        
counter = 0
while True:
    check_tickets(counter)
    counter += 1
    time.sleep(11)  # Adjust interval if needed

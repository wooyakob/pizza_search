import openai
import os
import requests

openai.api_key = os.environ["OPENAI_API_KEY"]
search_url = "https://api.yelp.com/v3/businesses/search"

print("Hello! I'm a ChatGPT-powered assistant. Ask me to find pizza places near you, and I'll do my best to help.")

while True:
  prompt = input("You: ")
  
  if "pizza places near me" in prompt:
    headers = {
      "Authorization": f"Bearer {os.environ['YELP_API_KEY']}"
    }
    params = {
      "term": "pizza",
      "location": "your location",
      "limit": 5
    }
    response = requests.get(search_url, headers=headers, params=params).json()
    businesses = response.get("businesses", [])

    if len(businesses) > 0:
      for business in businesses:
        name = business.get("name", "No name found")
        rating = business.get("rating", "No rating found")
        address = business.get("location", {}).get("address1", "No address found")
        print(f"{name} ({rating}): {address}")
    else:
      print("Sorry, I couldn't find any pizza places near you.")
  
  else:
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=60,
      n=1,
      stop=None,
      temperature=0.5,
    )
    print("Chatbot:", response.choices[0].text.strip())
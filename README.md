# 4daagse-bot
Request bot for Nijmeegse vierdaagse

# Prerequisites
* [CrawlBase](https://crawlbase.com/) account

# Setup
1. Fill in your API key from CrawlBase in the API_KEY variable (optionally, add a .env file)
2. Fill in your session ID
It's located under *Request Headers* as `atleta-session-id`
![image](https://github.com/user-attachments/assets/2d1f5a9d-513d-4df4-a3b0-9093eae23b96)
3. *Optionally* adjust eventID for upcoming years
It's located under *Payload* `variables->{id: xxx}`
![image](https://github.com/user-attachments/assets/1b900be7-6016-4765-9023-63512e02424e)

# Running
Run [request.py](https://github.com/Pepijnvdliefvoort/4daagse-bot/blob/main/request.py) script.

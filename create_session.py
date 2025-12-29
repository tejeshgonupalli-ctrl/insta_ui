from instagrapi import Client

cl = Client()

# Replace with your Instagram credentials
USERNAME = "mysel_f3249"
PASSWORD = "insta_auto"

# Log in and save session
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session_account1.json")
print("✅ Session file created successfully!")

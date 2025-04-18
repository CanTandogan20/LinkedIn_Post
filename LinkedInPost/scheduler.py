import schedule
import time
from post_linkedin import post_to_linkedin
from generate_post import generate_post

def job():
    prompt = "Schreibe einen LinkedIn-Post über die Vorteile von KI im Marketing."
    post_content = generate_post(prompt)
    status_code = post_to_linkedin(post_content)
    print(f"Post Status: {status_code}")

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

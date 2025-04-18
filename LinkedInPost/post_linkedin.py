import requests
import os
from linkedin_auth import get_linkedin_token

def post_to_linkedin(content):
    access_token = get_linkedin_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    post_data = {
        "author": f"urn:li:person:{os.getenv('LINKEDIN_ID')}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, json=post_data)
    return response.status_code

def get_response_time(url: str):
    if "google" in url:
        return 0.3
    elif "youtube" in url:
        return 0.4
    else:
        return "Information not found."
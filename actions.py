def get_response_time(url: str):
    if "google" in url:
        return 0.3
    elif "facebook" in url:
        return 0.4
    elif url.contains("youtube"):
      return 0.3
    else:
        return "Information not found."
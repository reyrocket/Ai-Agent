# def get_response_time(url: str):
#     if "google" in url:
#         return 0.3
#     elif "youtube" in url:
#         return 0.4
#     else:
#         return "Information not found."
from SimplerLLM.tools.rapid_api import RapidAPIClient
def get_seo_page_report(url :str):
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {
        'url': url,
    }
    api_client = RapidAPIClient() 
    response = api_client.call_api(api_url, method='GET', params=api_params)
    return response
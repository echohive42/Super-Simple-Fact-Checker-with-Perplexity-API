import requests
from config import PERPLEXITY_API_KEY, PERPLEXITY_BASE_URL, MODEL_NAME, SYSTEM_MESSAGE, print_status

class PerplexityService:
    def __init__(self):
        try:
            self.headers = {
                "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
                "Content-Type": "application/json"
            }
            self.url = f"{PERPLEXITY_BASE_URL}/chat/completions"
            print_status("Perplexity API client initialized", "success")
        except Exception as e:
            print_status(f"Error initializing Perplexity API client: {str(e)}", "error")
            raise

    async def fact_check(self, content: str) -> dict:
        """
        Fact check the provided content using Perplexity API
        """
        try:
            print_status("Starting fact-checking process", "info")
            
            payload = {
                "model": MODEL_NAME,
                "messages": [
                    {"role": "system", "content": SYSTEM_MESSAGE},
                    {"role": "user", "content": content}
                ],
                "temperature": 0.2,
                "top_p": 0.9,
                "search_domain_filter": ["perplexity.ai"],
                "return_images": False,
                "return_related_questions": False,
                "search_recency_filter": "week",
                "top_k": 0,
                "stream": False,
                "presence_penalty": 0,
                "frequency_penalty": 1
            }

            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()
            response_data = response.json()
            
            # Extract the main content and citations
            result = response_data['choices'][0]['message']['content']
            
            # Format citations as objects with url
            citations = []
            if 'citations' in response_data:
                citations = [{"url": url} for url in response_data['citations']]
            
            print_status("Fact-checking completed successfully", "success")
            return {
                "result": result,
                "citations": citations,
                "status": "success"
            }
            
        except Exception as e:
            error_message = f"Error during fact-checking: {str(e)}"
            print_status(error_message, "error")
            return {
                "result": error_message,
                "citations": [],
                "status": "error"
            } 
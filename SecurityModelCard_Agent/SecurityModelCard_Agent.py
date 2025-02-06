import os
import PyPDF2
from crewai import Agent, Task
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityModelCard:
    def __init__(self):
        self.model_details = {}
        self.intended_use = {}
        self.factors = {}
        self.metrics = {}
        self.evaluation_data = {}
        self.training_data = ""
        self.quantitative_analyses = {}
        self.ethical_considerations = ""
        self.caveats_and_recommendations = ""
        self.security_considerations = {}

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        logging.error(f"Error extracting text: {e}")
        return None

def generate_security_model_card(text):
    card = SecurityModelCard()

    try:
        security_agent = Agent(
            #... your agent configuration:  model, tools, etc....
            # Example: model="gpt-3.5-turbo", api_key="YOUR_API_KEY"
        )

        extract_task = Task(
            "Extract key security information from the provided text.",
            agent=security_agent
        )

        prompt = f"""
        Analyze the following text and extract the following information, matching the JSON structure provided below EXACTLY.  Return ONLY the JSON.  If any information is not found, return an empty string or list for that field.  Do not include any explanatory text, only the JSON.

        ```json
        {{
            "model_details": {{
                "developer": "",
                "date": "",
                "version": "",
                "type": "",
                "information": "",
                "resource": "",
                "citation": "",
                "license": "",
                "contact": ""
            }},
            "intended_use": {{
                "primary_uses": "",
                "primary_users": "",
                "out_of_scope_uses": ""
            }},
            "factors": {{
                "relevant_factors": "",
                "evaluation_factors": ""
            }},
            "metrics": {{
                "performance_measures": "",
                "decision_thresholds": "",
                "variation_approaches": ""
            }},
            "evaluation_data": {{
                "datasets": "",
                "motivation": "",
                "preprocessing": ""
            }},
            "training_data": "",
            "quantitative_analyses": {{
                "unitary_results": "",
                "intersectional_results": ""
            }},
            "ethical_considerations": "",
            "caveats_and_recommendations": "",
            "security_considerations": {{
                "threat_modeling": "",
                "security_testing": ""
            }}
        }}
        ```

        Text:
        ```
        {text}
        ```
        """

        result = extract_task.run(prompt=prompt)

        try:
            extracted_data = json.loads(result)
            card.model_details = extracted_data.get("model_details", {})
            card.intended_use = extracted_data.get("intended_use", {})
            card.factors = extracted_data.get("factors", {})
            card.metrics = extracted_data.get("metrics", {})
            card.evaluation_data = extracted_data.get("evaluation_data", {})
            card.training_data = extracted_data.get("training_data", "")
            card.quantitative_analyses = extracted_data.get("quantitative_analyses", {})
            card.ethical_considerations = extracted_data.get("ethical_considerations", "")
            card.caveats_and_recommendations = extracted_data.get("caveats_and_recommendations", "")
            card.security_considerations = extracted_data.get("security_considerations", {})

        except json.JSONDecodeError as e:
            logging.error(f"JSON decode error: {e}")
            logging.error(f"Agent Output: {result}")
            card = SecurityModelCard()

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            card = SecurityModelCard()

    except Exception as e:
        logging.error(f"Error with Crew AI: {e}")
        card = SecurityModelCard()

    return card

def main():
    pdf_file_path = input("Enter the path to the PDF file: ")

    if not os.path.exists(pdf_file_path):
        print("PDF file not found.")
        return

    extracted_text = extract_text_from_pdf(pdf_file_path)

    if extracted_text:
        security_card = generate_security_model_card(extracted_text)

        import json
        print(json.dumps(security_card.__dict__, indent=4))

if __name__ == "__main__":
    main()
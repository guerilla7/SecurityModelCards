import json
import PyPDF2

def generate_security_model_card():
    """
    Interactively gathers information from the user to generate a Security Model Card in JSON format,
    with an option to load data from a PDF document, and saves the output to a JSON file.
    """

    model_card = {}

    # --- Load data from PDF ---
    load_from_pdf = input("Load data from a PDF document? (yes/no): ")
    if load_from_pdf.lower() == "yes":
        pdf_file_path = input("Enter the path to the PDF file: ")
        try:
            with open(pdf_file_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text_from_pdf = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text_from_pdf += page.extract_text()

                # (You'll still need to customize this PDF parsing logic)
                # Example:
                lines = text_from_pdf.splitlines()
                for line in lines:
                    if "Model Name:" in line:
                        model_card["model_details"] = {"name": line.split("Model Name:")[-1].strip()}
                    # ... and so on for other fields

        except FileNotFoundError:
            print(f"Error: PDF file not found at {pdf_file_path}")
            return
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return

    # --- Model Details ---
    if "model_details" not in model_card:
        model_card["model_details"] = {}

    model_card["model_details"]["developer"] = input("Enter person or organization developing model: ")
    model_card["model_details"]["date"] = input("Enter model date (YYYY-MM-DD): ")
    model_card["model_details"]["version"] = input("Enter model version: ")
    model_card["model_details"]["type"] = input("Enter model type: ")
    model_card["model_details"]["information"] = input("Enter information about training algorithms, parameters, etc.: ")
    model_card["model_details"]["resource"] = input("Enter paper or other resource for more information: ")
    model_card["model_details"]["citation"] = input("Enter citation details: ")
    model_card["model_details"]["license"] = input("Enter license: ")
    model_card["model_details"]["contact"] = input("Enter where to send questions or comments: ")

    # --- Intended Use ---
    model_card["intended_use"] = {
        "primary_uses": input("Enter primary intended uses: "),
        "primary_users": input("Enter primary intended users: "),
        "out_of_scope_uses": input("Enter out-of-scope use cases: ")
    }

    # --- Factors ---
    model_card["factors"] = {
        "relevant_factors": input("Enter relevant factors: "),
        "evaluation_factors": input("Enter evaluation factors: ")
    }

    # --- Metrics ---
    model_card["metrics"] = {
        "performance_measures": input("Enter model performance measures: "),
        "decision_thresholds": input("Enter decision thresholds: "),
        "variation_approaches": input("Enter variation approaches: ")
    }

    # --- Evaluation Data ---
    model_card["evaluation_data"] = {
        "datasets": input("Enter datasets used for evaluation: "),
        "motivation": input("Enter motivation for dataset selection: "),
        "preprocessing": input("Enter preprocessing steps applied to evaluation data: ")
    }

    # --- Training Data ---
    model_card["training_data"] = input("Enter details about training data (or minimal allowable information): ")

    # --- Quantitative Analyses ---
    model_card["quantitative_analyses"] = {
        "unitary_results": input("Enter unitary results: "),
        "intersectional_results": input("Enter intersectional results: ")
    }

    # --- Ethical Considerations ---
    model_card["ethical_considerations"] = input("Enter ethical considerations: ")

    # --- Caveats and Recommendations ---
    model_card["caveats_and_recommendations"] = input("Enter caveats and recommendations: ")

    # --- Security Considerations ---
    model_card["security_considerations"] = {
        "threat_modeling": input("Describe threat modeling performed: "),
        "security_testing": input("Describe security testing conducted: ")
    }

    # Convert to JSON
    json_output = json.dumps(model_card, indent=4)

    # --- Save to JSON file ---
    try:
        with open("security_model_card_report.json", "w") as f:
            f.write(json_output)
        print("\nSecurity Model Card saved to security_model_card_report.json")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

if __name__ == "__main__":
    generate_security_model_card()
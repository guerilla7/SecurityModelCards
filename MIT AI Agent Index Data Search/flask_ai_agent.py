from flask import Flask, jsonify, request, render_template
import pandas as pd
import json

app = Flask(__name__)

def load_csv_data(file_path):
    """Loads CSV data from a file and returns it as a list of dictionaries."""
    try:
        df = pd.read_csv(file_path, header=2)  # Assuming header is on the third row
        df = df.dropna(how='all')
        df = df.fillna("Unknown")
        data = df.to_dict(orient='records')
        return data
    except Exception as e:
        return {"error": str(e)}

def search_data(data, search_term):
    """Filters the data to include only items that contain the search term."""
    if not data or "error" in data:
        return data

    search_term_lower = search_term.lower()
    results = []
    for item in data:
        item_str = json.dumps(item, ensure_ascii=False).lower()
        if search_term_lower in item_str:
            results.append(item)
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles displaying the data and search functionality."""
    data = load_csv_data("AI_Agent_IndexV2.csv")
    ##  data = load_csv_data("AI_Agent_IndexV1.csv")
    search_term = request.args.get('search')

    if search_term:
        results = search_data(data, search_term)
        return render_template('index.html', results=results, search=search_term)
    else:
        return render_template('index.html', results=data, search=None)

if __name__ == '__main__':
    app.run(debug=True)
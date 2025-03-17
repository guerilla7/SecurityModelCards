
# MIT AI Agent Index Search
https://aiagentindex.mit.edu/

This Flask application displays data from a CSV file, with dynamic header detection, and allows users to search the data.

## Prerequisites

* Python 3.6 or higher
* pip (Python package installer)

## Installation

1.  **Clone the repository (or download the files):**

    If you have the files in a repository, you can clone it:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

    If you've downloaded the files, navigate to the directory containing the files using your terminal.

2.  **Install the dependencies:**

    Use pip to install the required Python packages:

    ```bash
    pip install Flask pandas
    ```

## File Structure

Ensure your files are structured as follows:

```
AI_Agent_Index_App/
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── AI Agent Index.csv
    └── README.md
```

* `app.py`: Contains the Flask application code.
* `templates/index.html`: Contains the HTML template for the user interface.
* `AI Agent Index.csv`: The CSV file containing the data.
* `README.md`: This file, providing instructions.

## Running the Application

1.  **Navigate to the application directory:**

    ```bash
    cd AI_Agent_Index_App
    ```

2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

3.  **Open your browser:**

    Go to `http://127.0.0.1:5000/` in your web browser.

## Using the Application

* **Viewing the data:** The application will display the data from the CSV file in a table.
* **Searching the data:**
    * Enter a search term in the input field.
    * Click the "Search" button.
    * The application will display the results that match your search term.

## Notes

* The application uses dynamic header detection to correctly display headers from the CSV file.
* The application assumes the CSV file is named `AI Agent Index.csv` and is located in the same directory as `app.py`.
```
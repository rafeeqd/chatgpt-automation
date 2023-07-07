# Food Details and Nutrition

This Python script interacts with the OpenAI GPT-3.5-Turbo model to retrieve and format food nutrition details. The script makes use of the OpenAI API to query the model and save the formatted data to an Excel file.

## Prerequisites

- Python 3.x
- OpenAI library (`pip install openai`)
- Requests library (`pip install requests`)
- Pandas library (`pip install pandas`)

## Usage

1. Install the required dependencies mentioned in the Prerequisites section.

2. Clone the repository or download the script file.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Modify the `df` variable in the script to specify the path or name of the input Excel file containing food details.

5. Ensure that the OpenAI GPT-3.5-Turbo API key is assigned to the `openai.api_key` variable.

6. Run the following command to execute the script:

   ```bash
   python script.py

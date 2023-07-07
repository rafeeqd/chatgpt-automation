import openai
import requests
import re
import pandas as pd
import ast


def format_data(content):
    """
    Formats the content by extracting relevant information and saving it to a DataFrame.

    Args:
        content (str): The content to format.

    Returns:
        None
    """
    pattern = r'(?<=[ -])\d+(?:\.\d+)?'  # To match only digits after space ex: Calories 123 or protein 13.4
    temp_dict = []
    remove_info = content.split(':', maxsplit=1)[1].strip()
    remove_info = remove_info.replace(":", "")
    split_by_line = remove_info.split("\n\n")

    for i in split_by_line:
        get_only_num = re.findall(pattern, i)
        temp_dict.append({"Food_Item": i.split("\n")[0],
                          "Calories": ast.literal_eval(get_only_num[0]),
                          "Proteins": ast.literal_eval(get_only_num[1]),
                          "Carbs": ast.literal_eval(get_only_num[2]),
                          "Fats": ast.literal_eval(get_only_num[3])
                          })

    df = pd.DataFrame.from_dict(temp_dict)
    food_details = ['Calories', 'Proteins', 'Carbs', 'Fats']
    length_of_df = len(df.index.to_list())

    for i in food_details:
        df.loc[length_of_df + 2, i] = df.loc[:, i].sum()

    df.to_excel("food.xlsx", index=False)


def query_gpt(f_details):
    """
    Queries GPT-3.5-Turbo model to get the total calories and nutrients for food details.

    Args:
        f_details (str): The food details.

    Returns:
        None
    """
    construct_question = f"what are the total calories and nutrients in {f_details} \
        provide me in this format \
        Calories \
        Protein \
        Carbs \
        Fats \
        Give me the TOTAL number for everything listed above. \
        Give me average numbers, no ranges."

    openai.api_key = "YOUR  KEY"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": construct_question}]
    )
    
    content = completion.choices[0].message.content
    print(content)
    format_data(content)


# Usage example
df = pd.read_excel(io="food.xlsx")
f_details = ''.join(df.columns.values)
query_gpt(f_details)

import openai
import pandas as pd

openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def ask_gpt(question, context):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="local-model",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=250,
    )
    answer = response['choices'][0]['message']['content'].strip()
    return answer

file_context = ['JD_1.txt','JD_2.txt','JD_3.txt','JD_4.txt','JD_5.txt']

job_titles = []
experienced_years = []
academic_qualifications = []

for file in file_context:
    context = read_text_file(file)

    prompts = [
        "Mention the job title using less than four words.",
        "Mention the number of experience years needed for positions using less than six words.",
        "Mention the academic qualification using less than ten words.",
    ]

    for prompt in prompts:
        answer = ask_gpt(prompt, context)
        answer = answer.split('\n')

        index = prompts.index(prompt)
        if index == 0:
            job_titles.append(answer)
        elif index == 1:
            experienced_years.append(answer)
        elif index == 2:
            academic_qualifications.append(answer)

data = {
    "Job title": job_titles,
    "Experienced years": experienced_years,
    "Academic Qualification": academic_qualifications
}

df = pd.DataFrame(data)

print(df)

print("Experienced years")
for i in experienced_years:
    print(i)

print("Academic Qualification")    
for i in academic_qualifications:
    print(i)

# import pandas as pd
# df = pd.read_csv('./data/available_counter.csv')
# print(df)
#
# df["Count"][0]=2
#
# df.loc[0:1].fillna("[insert]")
#
#
import openai
openai.api_key = "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"



with open('./data/celebrity_tracker.csv') as f:
    lines=f.readlines()[1:]

NUM_LINES = len(lines)

print(lines)


def predict_via_insert(prompt):
    prompt=prompt.rstrip()
    # assert(prompt=="yes,no,yes,2,\nyes,no,no,")
    print(f"{prompt=}")
    print("====== CHECK that this is till valid CSV")
    print(prompt)
    print("=========================================")
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt="yes,no,yes,2,\nyes,no,no,",
        prompt=prompt,
        suffix="\n",
        temperature=0.1,
        max_tokens=463,
        top_p=0.45,
        best_of=3,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[","]
    )
    return response.choices[0].text

def predict_via_edit(prompt):
    print(f"{prompt=}")
    # print(r"prompt='yes,no,yes,2\nyes,no,no,\n'")
    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=prompt,
        instruction="Add missing values.",
        temperature=0.1,
        top_p=0.45,
    )
    return response.choices[0].text


cursor=2
prompt = "".join(lines[:cursor]).rstrip()
while cursor<=NUM_LINES:


    print(prompt)
    print(" ")

    pred = predict_via_insert(prompt)
    print(f"The prediction is {pred} if this is correct press y, else press n")
    answer = input();
    if answer=="y":
        pred=pred

    else:
        print("Ok, what was the correct answer?")
        pred=input()

    prompt=prompt+pred+','
    if cursor<len(lines)-1:
        prompt=prompt+"\n"+lines[cursor].rstrip()
    cursor+=1

# prompt = "".join(lines[:2]).rstrip()
# assert(prompt=="yes,no,yes,2\nno,yes,yes,")
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="yes,no,yes,2\nno,yes,yes,",
#     suffix="",
#     # temperature=0.7,
#     # max_tokens=512,
#     # top_p=0.5,
#     # # frequency_penalty=0,
#     # # presence_penalty=0,
#     # best_of=10,
#     n=2
# )
#
# print(f"{response.choices=}")
# print(f"{response.choices[0].text}")
# print(f"{response.choices[1].text}")
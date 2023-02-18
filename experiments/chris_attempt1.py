import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.1,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1,
        # stop=["!"]
    )
    # print(f"{response=}")
    assert len(response.choices) == 1
    assert response.choices[0].finish_reason == "stop"
    return response.choices[0].text


def get_edit(prompt: str):
    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=prompt,
        instruction="Insert missing values",
        temperature=0,
        top_p=1,
    )
    return response.choices[0].text


def read_csv(filename):
    with open(filename, 'r') as f:
        return f.read()


if __name__ == '__main__':
    # prompt = "def sum_list(arr) -> int:"
    # print(get_completion(prompt))
    prefix = "" \
    #  "Complete this csv and include the headers\n\n" \
    # "Return as csv" \
    # "\n\n" \
    # "This is an csv file. The first column is A, and the first row is 1." \
    #  "For example, the cell D7 represents column D, row 7." \
    # "Suggest autocompletes in the form cell:value. For example F8:ten, B3:Tony, etc."
    postfix = "" \
        # "\n!" \


    def create_query(query: str) -> str:
        return prefix + query + postfix


    rel_path = "../data/"
    fnames = [
        "sign_up",
        "available_counter",
        "celebrity_tracker",
        "office_costs",
    ]

    X = [rel_path + fname + ".csv" for fname in fnames]
    Y_gt = [rel_path + fname + "_res.csv" for fname in fnames]

    print(f"{X=}")
    correct = 0
    for x, y_gt in zip(X, Y_gt):
        excel_state = read_csv(x)
        query = create_query(excel_state)
        y_pr = get_edit(query).strip()
        y_gt = read_csv(y_gt)
        print(f"{query=}\n{y_pr=}\n{y_gt=}\n{y_pr == y_gt}\n")
        if y_pr == y_gt:
            correct += 1
    print(f"accuracy: {correct / len(X)}")

import json
import time

from openai import OpenAI

from config import (
    OPENROUTER_API_KEY,
    MODEL,
    MAX_TOKENS
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def ask_ai(prompt):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=MAX_TOKENS
    )

    return response.choices[0].message.content


with open(
    "prompts.txt",
    "r",
    encoding="utf-8"
) as file:

    prompts = [
        p.strip()
        for p in file.readlines()
        if p.strip()
    ]


results = []

print("\nStarting Prompt Testing...\n")


for i, prompt in enumerate(
        prompts,
        start=1
):

    print(f"Running Prompt {i}")

    try:

        start_time = time.time()

        output = ask_ai(prompt)

        end_time = time.time()

        response_time = round(
            end_time - start_time,
            2
        )

    except Exception as e:

        output = f"ERROR: {str(e)}"

        response_time = 0

    length_score = len(output)

    results.append(
        {
            "prompt_number": i,
            "prompt": prompt,
            "response": output,
            "response_time": response_time,
            "length_score": length_score
        }
    )


with open(
    "results.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4,
        ensure_ascii=False
    )


with open(
    "results.txt",
    "w",
    encoding="utf-8"
) as file:

    for item in results:

        file.write(
            f"PROMPT {item['prompt_number']}\n"
        )

        file.write(
            f"{item['prompt']}\n\n"
        )

        file.write(
            f"TIME: {item['response_time']} sec\n"
        )

        file.write(
            f"LENGTH: {item['length_score']}\n\n"
        )

        file.write(
            item["response"]
        )

        file.write(
            "\n\n"
        )

        file.write(
            "=" * 60
        )

        file.write(
            "\n\n"
        )


winner = max(
    results,
    key=lambda x: x["length_score"]
)


with open(
    "summary_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "PROMPT TEST SUMMARY\n\n"
    )

    file.write(
        f"Total Prompts: {len(results)}\n\n"
    )

    file.write(
        "Winner Prompt:\n"
    )

    file.write(
        f"{winner['prompt']}\n\n"
    )

    file.write(
        f"Response Length: "
        f"{winner['length_score']}\n"
    )

    file.write(
        f"Response Time: "
        f"{winner['response_time']} sec\n"
    )

print("\nTesting Complete\n")
print(
    f"Winner Prompt: "
    f"{winner['prompt']}"
)
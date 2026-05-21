import json
import re


def converter(texto):
    matches = re.findall(r'\{[^{}]*\}', texto)
    for m in matches:
        try:
            data = json.loads(m)
            return data
        except:
            continue

    return {
        "final_answer": "xxx",
        "classification": "xxx",
        "language": "xxx"
    }

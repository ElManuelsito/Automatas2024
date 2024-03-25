import re

def validate_string(string):
    results = []
    results.append(bool(re.search(r"[a-zA-Z0-9]", string)))
    results.append(bool(re.search(r"[a-zA-Z]", string)))
    results.append(bool(re.search(r"[A-Z]", string)))
    results.append(bool(re.search(r"[a-z]", string)))
    results.append(bool(re.search(r"\d", string)))
    results.append(bool(re.search(r"({8, })", string)))
    return results

resultado = validate_string("Au")
print("\n".join(map(str, resultado)))
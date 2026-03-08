# Space O(N) | Time O(N)
def solution(sentence: str) -> str:
    sanitized: str = sentence.replace(" ", "")
    return ''.join(dict.fromkeys(sanitized))

print(solution("Interviews asks you question that are not always relevant in what you will do in the actual job"))

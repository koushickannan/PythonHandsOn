class CamelCase:
    def __init__(self, s: str):
        self.s = s

    def convert(self) -> str:
        words = self.s.strip().split()
        if not words:
            return ""
        
        result = [words[0]]
        for word in words[1:]:
            if word[0].islower():
                result.append(word[0].upper() + word[1:])
            else:
                result.append(word)
        return ''.join(result)

if __name__ == "__main__":
    s = "i like spicy chicken burger"
    camel_case = CamelCase(s)
    print(camel_case.convert())

class Story:

    def __init__(self, words, text):

        self.prompts = words
        self.template = text

    def generate(self, answers):

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text



story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

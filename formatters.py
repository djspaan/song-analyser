import re


class SongFormatter:
    def __init__(self):
        pass

    @staticmethod
    def remove_parentheses(text):
        return re.sub(r'\([^()]*\)', '', text)

    @staticmethod
    def remove_brackets(text):
        return re.sub(r'\[[^()]*\]', '', text)

    @staticmethod
    def strip(text):
        text = SongFormatter.remove_parentheses(text)
        text = SongFormatter.remove_brackets(text)
        return text

# Python Code for Object
# Oriented Concepts without
# using Factory method


class FrenchLocalizer:

    """it simply returns the french version"""

    def __init__(self):
        self.translations = {
            "hello": "bonjour",
            "world": "le monde",
            "without": "sans",
            "design patterns": "modèles de conception",
        }

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class PersianLocalizer:
    """it simply returns the persian version"""

    def __init__(self):
        self.translations = {
            "hello": "سلام",
            "world": "دنیا",
            "without": "بدون",
            "design patterns": "الگو های طراحی",
        }

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


if __name__ == "__main__":
    # main method to call others
    french = FrenchLocalizer()
    english = EnglishLocalizer()
    persian = PersianLocalizer()

    # list of strings
    message = ["hello", "world", "without", "design patterns"]

    for msg in message:
        print("-" * 30)
        print(french.localize(msg))
        print(english.localize(msg))
        print(persian.localize(msg))
        print("-" * 30)

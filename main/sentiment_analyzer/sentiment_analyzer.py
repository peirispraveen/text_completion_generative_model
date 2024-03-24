from string import punctuation
from collections import Counter
from collections import defaultdict

post_comments_with_labels = [  # 1 = positive, 0 = negative
    ("I love this post.", "1"),
    ("This post is your best work.", "1"),
    ("I really liked this post.", "1"),
    ('I agree 100 percent. This is true', '1'),
    ("This post is spot on!", "1"),
    ("So smart!", "1"),
    ("What a good point!", "1"),
    ("Bad stuff.", "0"),
    ("I hate this.", "0"),
    ("This post is horrible.", "0"),
    ("I really disliked this post.", "0"),
    ("What a waste of time.", "0"),
    ("I do not agree with this post.", "0"),
    ("I can't believe you would post this.", "0"),
]


class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"1": [], "0": []}
        self.sample_count = len(samples)
        for text, label in samples:
            self.mapping[label] += self.tokenize(text)
        self.pos_counter = Counter(self.mapping["1"])
        self.neg_counter = Counter(self.mapping["0"])

    @staticmethod
    def tokenize(text):
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def classify(self, text):
        tokens = self.tokenize(text)
        pos = []
        neg = []

        for token in tokens:
            pos.append(self.pos_counter[token]/self.sample_count)
            neg.append(self.neg_counter[token]/self.sample_count)

        if sum(pos) > sum(neg):
            return "positive"
        elif sum(neg) > sum(pos):
            return "negative"
        else:
            return "neutral"


cl = NaiveBayesClassifier(post_comments_with_labels)

show_expected_result = False
show_hints = False


def get_sentiment(text):
    cl = NaiveBayesClassifier(post_comments_with_labels)
    return cl.classify(text)


text = "I hate"
print(text, "\n", get_sentiment(text))

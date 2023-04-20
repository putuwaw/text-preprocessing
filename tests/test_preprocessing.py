from preprocessing import (
    lowercase,
    number_removal,
    punctuation_removal,
    tokenization,
    stopword_removal,
    stemming
)


def test_lowercase():
    actual = "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil."
    expected = "the 5 biggest countries by population in 2017 are china, india, united states, indonesia, and brazil."
    assert lowercase(actual) == expected


def test_number_removal():
    actual = "Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls."
    expected = "Box A contains red and white balls, while Box B contains red and blue balls."
    assert number_removal(actual) == expected


def test_punctuation_removal():
    actual = "This &is [an] example? {of} string. with.? punctuation!!!!"
    expected = "This is an example of string with punctuation"
    assert punctuation_removal(actual) == expected


def test_tokenization():
    actual = '''
    Here's to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes. 
    The ones who see things differently — they're not fond of rules. 
    You can quote them, disagree with them, glorify or vilify them, but the only thing you can't do is ignore them because they change things. 
    They push the human race forward, and while some may see them as the crazy ones, we see genius, because the ones who are crazy enough to think that they can change the world, are the ones who do.
    '''
    expected = ["Here's", 'to', 'the', 'crazy', 'ones,', 'the', 'misfits,', 'the', 'rebels,', 'the', 'troublemakers,', 'the', 'round', 'pegs', 'in', 'the', 'square', 'holes.', 'The', 'ones', 'who', 'see', 'things', 'differently', '—', "they're", 'not', 'fond', 'of', 'rules.', 'You', 'can', 'quote', 'them,', 'disagree', 'with', 'them,', 'glorify', 'or', 'vilify', 'them,', 'but', 'the', 'only', 'thing',
                'you', "can't", 'do', 'is', 'ignore', 'them', 'because', 'they', 'change', 'things.', 'They', 'push', 'the', 'human', 'race', 'forward,', 'and', 'while', 'some', 'may', 'see', 'them', 'as', 'the', 'crazy', 'ones,', 'we', 'see', 'genius,', 'because', 'the', 'ones', 'who', 'are', 'crazy', 'enough', 'to', 'think', 'that', 'they', 'can', 'change', 'the', 'world,', 'are', 'the', 'ones', 'who', 'do.']
    assert tokenization(actual) == expected


def test_stopword_removal():
    actual = "NLTK is a leading platform for building Python programs to work with human language data."
    expected = "NLTK leading platform building Python programs work human language data."
    assert stopword_removal(actual) == expected


def test_stemming():
    actual = "There are several types of stemming algorithms."
    expected = "there are sever type of stem algorithm."
    assert stemming(actual) == expected

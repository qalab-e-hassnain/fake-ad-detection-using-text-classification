from nltk.stem import WordNetLemmatizer
import re
import inflect
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def text_lowercase(text):
    return text.lower()


def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result


p = inflect.engine()


def convert_number(text):
    temp_str = text.split()
    new_string = []

    for word in temp_str:
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)

    temp_str = ' '.join(new_string)
    return temp_str


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def remove_whitespace(text):
    return " ".join(text.split())


def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text


stemmer = PorterStemmer()


def stem_words(text):
    stems = [stemmer.stem(word) for word in text]
    return stems


lemmatizer = WordNetLemmatizer()


def lemmatize_word(text):
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in text]
    return lemmas


def pre_processing(in_string):
    lc_string = text_lowercase(in_string)
    rp_string = remove_punctuation(lc_string)
    cn_string = convert_number(rp_string)
    rw_string = remove_whitespace(cn_string)
    sw_string = stem_words(rw_string)
    return sw_string

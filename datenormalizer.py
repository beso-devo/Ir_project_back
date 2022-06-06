import datefinder
from dateutil import parser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk
from datetime import datetime


class DateNormalizer:

    def normalizeText(self, document):
        dates = [datetime]
        date_rege_1 = re.compile(
            "(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?,?(\d{1,2}\D?)?\D?(\d\d\d\d|\d{2})")
        date_rege_2 = re.compile(
            "\d{1,2} (Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?,?(\d\d\d\d|\d{2})")
        for statement in nltk.sent_tokenize(document.get_words()):
            dates = datefinder.find_dates(statement, source=True)

        for date in dates:

            if date_rege_1.match(date[1]) is not None:
                print(date)
                print(str(document.get_words()).replace(str(date[1]),
                                                        str(str(date[0].day) + " " + str(date[0].month) + " " + str(
                                                            date[0].year))))

            if date_rege_2.match(date[1]) is not None:
                print(date)
                print(str(document.get_words()).replace(str(date[1]),
                                                        str(str(date[0].day) + " " + str(date[0].month) + " " + str(
                                                            date[0].year))))

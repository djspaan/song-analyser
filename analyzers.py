from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import collections
import numpy
from nlp_rake import rake


class Rake:
    def __init__(self, min_chars=5, min_words=3, min_appearance=4):
        self.rake_impl = rake.Rake('data/stoplist.txt', min_chars, min_words, min_appearance)

    def extract(self, text):
        return self.rake_impl.run(text)


class SongAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def plot(dictionary, title=None, ylim=None, xlabel=None, ylabel=None):
        plt.bar(range(len(dictionary)), list(dictionary.values()), color='yellow', align='center')
        plt.xticks(range(len(dictionary)), dictionary.keys(), rotation=90)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if ylim:
            plt.ylim(ylim)
        plt.show()


class VaderSongAnalyzer(SongAnalyzer):
    @staticmethod
    def get_sentiment(text, sentiment_type='compound'):
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(text)[sentiment_type]

    @staticmethod
    def get_sentiment_by_year(songs, sentiment_type='compound'):
        years = sorted(set(songs.pluck('Year')))
        analyzed_years = collections.OrderedDict()
        for year in years:
            songs_by_year = songs.where('Year', year)
            analyzed_songs = [VaderSongAnalyzer.get_sentiment(song.Lyrics) for song in songs_by_year]
            analyzed_years[year] = numpy.mean(analyzed_songs)
        return analyzed_years

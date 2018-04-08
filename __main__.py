from readers import CSVReader
from mappers import SongMapper
from stores import SongStore
from analyzers import VaderSongAnalyzer
from analyzers import Rake
import math
from wordcloud import WordCloud
import matplotlib.pyplot as plt

SONG_FILE = './data/songdata-all.csv'


class Main:
    def __init__(self):
        """
        Initialization of the song analyzer.
        Reads the song file and stores it in memory.
        """
        mapper = SongMapper(CSVReader(SONG_FILE))
        self.store = mapper.map_to_store(SongStore())

    def run(self):
        """
        Here you can run commands to retrieve the wanted result.
        A few examples are shown below.
        """


        # Print the keywords extracted from all songs
        songs = self.store.all().where('Genre', 'Pop').where('Year', '1992')
        analyzer = Rake(4, 3, 2)
        result = []
        for song in songs:
            result = result + analyzer.extract(song.Lyrics)

        keywords = []
        for t in result:
            for i in range(1,int(math.ceil(t[1]))):
                keywords.append(t[0])

        wordcloud = WordCloud(background_color='black', scale=3,random_state=1,relative_scaling=0).generate(' '.join(keywords))
        plt.figure(figsize=(12,10))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

        # # Print the keywords extracted from all songs
        # songs = self.store.all()
        # analyzer = Rake(4, 3, 2)
        # for song in songs:
        #     print('')
        #     print(song.Title + ' - ' + song.Artist)
        #     print(analyzer.extract(song.Lyrics))

        # # Print all the songs retrieved from the song file.
        # print(self.store.all())

        # # Plot a graph of the mean compound sentiment of songs per year.
        # songs = self.store.all()
        # analyzed_by_year = VaderSongAnalyzer.get_sentiment_by_year(songs)
        # VaderSongAnalyzer.plot(analyzed_by_year, title='Mean compound sentiment per year', ylabel='Compound sentiment')
        #
        # # Plot a graph of the mean compound sentiment of hiphop songs per year.
        # songs = self.store.all().where('Genre', 'Hip-Hop')
        # analyzed_by_year = VaderSongAnalyzer.get_sentiment_by_year(songs)
        # VaderSongAnalyzer.plot(analyzed_by_year,
        #   title='Average compound sentiment of hip-hop songs per year', ylabel='Compound Sentiment')
        #
        # # Plot a graph of the mean compound sentiment of pop songs per year.
        # songs = self.store.all().where('Genre', 'Pop')
        # analyzed_by_year = VaderSongAnalyzer.get_sentiment_by_year(songs)
        # VaderSongAnalyzer.plot(analyzed_by_year,
        #                        title='Average compound sentiment of pop songs per year', ylabel='Compound Sentiment')


if __name__ == '__main__':
    Main().run()

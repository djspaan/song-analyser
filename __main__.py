from readers import CSVReader
from mappers import SongMapper
from stores import SongStore
from analyzers import VaderSongAnalyzer
from analyzers import Rake

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
        songs = self.store.all()

        analyzer = Rake(5,2,2)

        for song in songs:
            print(song.Title + ' - ' + song.Artist)
            print(analyzer.extract(song.Lyrics))



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

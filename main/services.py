import pandas as pd
import re


class Service:

    def __init__(self):
        self.df = pd.read_csv('main/datos/final.csv', sep=',')
        self.clean_data()

    def clean_data(self):
        self.df = self.df[['Artist','Title', 'Track','Duration_ms','Album','Album_type','Url_spotify','Uri','Url_youtube','Likes', 'Comments', 'Views']].dropna()
        self.df[['Likes', 'Comments', 'Views','Duration_ms']] = self.df[['Likes', 'Comments', 'Views','Duration_ms']].applymap('{:.0f}'.format)
        self.df[['Likes', 'Comments', 'Views','Duration_ms']] = self.df[['Likes', 'Comments', 'Views','Duration_ms']].applymap(lambda x: int(x))
        self.df['Rating'] = ((self.df['Likes']/self.df['Views']) * 100).apply(lambda x: round(x, 2))
        self.df['Duration_ms'] = pd.to_datetime(self.df['Duration_ms'], unit='ms').dt.strftime('%M:%S')
        self.df.rename(columns={'Duration_ms': 'Duration'}, inplace=True)

    def get_top_n_by_column(self, name, column, n=5):
        return self.df.groupby([name], as_index=False).agg({column: 'sum'}).nlargest(n, column)

    def get_most_duration(self):
        return self.df.sort_values(by=['Duration'], ascending=False).head(10)

    def search_song(self, song):
        return self.df[self.df['Track'].str.contains(song, flags=re.IGNORECASE)]

    def add_song(self, song_data):

        # Validar campos obligatorios
        required_fields = ['Artist', 'Url_spotify', 'Track', 'Album', 'Album_type', 'Uri', 'Duration', 'Url_youtube', 'Title']
        if any(pd.isna(song_data[field]) for field in required_fields):
            raise ValueError("Todos los campos obligatorios deben ser proporcionados.")

        new_song = pd.DataFrame(song_data, index=[0])

        return pd.concat([self.df, new_song]).tail(1)

    def get_df(self):
        return self.df.head(10)

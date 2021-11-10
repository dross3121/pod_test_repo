# Spotify-Challenge

## **Question 1**

**a)**	A better way to model genre data in this database would be to create new relational tables between genre, song, and album thereby reducing the time for any genre queries which may occur.  Additionally a genreID foreign key would need to be created so it can link various songs and albums to each specific genre.

### Sample Genre table:

| genreID |  Genre  |
|:-------:|:-------:|
|    1    |   Rock  |
|    2    | Hip Hop |
|    3    | Country |
|    4    |   EDM   |

Then you can add a genreID field in the Songs and Album table so that if there need to be any changes, like renaming, you won’t have to query each and every song.  The “Rock” genre can be changed simply through a song’s (or album’s) genreID.

**b)** A one to many relationship best describes the relationship between genre and song because a single genre can classify and be found on several different songs.





## Question 2

If you wanted a song to have multiple genres then an intermediary table would need to be created (many to many relationships, i.e., because now a song can have many genres, and a genre can have many songs) so that a song can have more than one genre (like Paul McCartney belonging to 2 different bands, Beatles and Wings, in the class example).  We will have to connect songID to genreID using an intermediary table.

### Sample SongGenre table where the first song has 2 different genres:

| ID | SongID | genreID |
|:--:|:------:|:-------:|
|  1 |    1   |    1    |
|  2 |    1   |    3    |
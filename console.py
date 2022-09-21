import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist1 = Artist('David Bowie')
artist_repository.save(artist1)

album1 = Album('Hunky Dory', 'Pop', artist1)
album_repository.save(album1)

results = artist_repository.select_all()
for result in results:
    print(result.__dict__)

results = album_repository.select_all()
for result in results:
    print(result.__dict__)

# result = album_repository.select(6)
# # for result in results:
# print(result.__dict__)

# result = artist_repository.select(8)
# # for result in results:
# print(result.__dict__)

result = artist_repository.albums(artist1)
for result in results:
    print(result.__dict__)



# pdb.set_trace()
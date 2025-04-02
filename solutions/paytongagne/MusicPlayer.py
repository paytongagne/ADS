from collections import deque, OrderedDict

class Ipud:
    def __init__(self):
        self.songs = {}  # Stores song details: O(1) complexity for access
        self.playlist = deque()  # Manage songs in playlist: O(1) for append and pop from ends
        self.recently = OrderedDict()  # Maintain order of recently played songs: O(1) for update and move-to-end operations

    def addSong(self, S, A, D):
        # O(1) complexity for adding a song (dictionary operation)
        if S in self.songs:
            print("ERROR addSong")
        else:
            self.songs[S] = {'artist': A, 'duration': D}

    def addToPlaylist(self, S):
        # O(1) complexity to check and add to playlist
        if S not in self.songs:
            print("ERROR addToPlaylist")
        elif S not in self.playlist:
            self.playlist.append(S)

    def play(self):
        # O(1) complexity to play from the playlist and update recently played
        if not self.playlist:
            print("No hay canciones en la lista.")
        else:
            song = self.playlist.popleft()
            self.recently[song] = self.recently.pop(song, None)  # Move to the end if exists
            print(f"Sonando {song}")

    def totalTime(self):
        # O(m) complexity where m is the number of songs in the playlist
        total_time = sum(self.songs[song]['duration'] for song in self.playlist)
        print(f"Tiempo total {total_time}")

    def recent(self, N):
        # O(N) complexity to retrieve up to N recently played songs
        if not self.recently:
            print("No hay canciones recientes")
        else:
            print(f"Las {min(N, len(self.recently))} más recientes:")
            count = 0
            for song in self.recently:
                if count < N:
                    print(f"    {song}")
                    count += 1
                else:
                    break

    def deleteSong(self, S):
        # O(m) complexity to delete a song from all structures, where m is the number of instances in the playlist
        if S in self.songs:
            self.songs.pop(S)
            # Remove all occurrences from the playlist
            self.playlist = deque(song for song in self.playlist if song != S)
            self.recently.pop(S, None)
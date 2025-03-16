# Music Player

The engineers at Apel are currently designing the software for their new music player, **iPud**. 
his software must allow users to:

- Add and remove songs.
- Add an existing song to the playlist.
- Skip to the next song.
- Get the total playback time of the playlist.
- Retrieve a list of recently played songs.

## Operations

The **iPud** ADT must support the following operations:

- **`addSong(S, A, D)`**: Adds the song `S` (a string) by artist `A` (a string) with duration `D` (an int) to iPud. If a song with the same name already exists, the operation will result in an error.
- **`addToPlaylist(S)`**: Adds the song `S` to the end of the playlist. If the song is already in the playlist, it is not added again (the playlist does not contain duplicates). If the song is not in iPud, an error is returned.
- **`current()`**: Returns the first song in the playlist. If the playlist is empty, an error is returned.
- **`play()`**: Removes the first song from the playlist and marks it as played. If the playlist is empty, the action has no effect.
- **`totalTime()`**: Returns the sum of the durations of all songs in the current playlist. If the playlist is empty, it returns `0`.
- **`recent(N)`**: Retrieves a list of the last `N` (where `N > 0`) recently played songs (via the `play` operation), ordered from most recent to oldest. If the number of played songs is less than `N`, all available songs are returned. The list does not contain duplicates, so if a song has been played multiple times, only the most recent play is recorded.
- **`deleteSong(S)`**: Completely removes the song `S` from iPud. If the song does not exist, the operation has no effect.

💡 Songs are uniquely identified by their name (a string).

## Implementation Requirements

A suitable data structure must be chosen to ensure all operations run in constant time, except for `recent`, which should have a linear time complexity in its argument `N`.

## Input Format

The input consists of multiple test cases. Each test case is a sequence of **iPud** operation calls, ending with the word `FIN`. Each operation call starts with the operation name followed by its arguments (if any). Song and artist names do not contain spaces.

## Output Format

The operations that produce output are as follows:

- **`play`**: Prints `Sonando` followed by the song name. If the playlist is empty, it prints `No hay canciones en la lista`.
- **`totalTime`**: Prints `Tiempo total` followed by the total playlist duration.
- **`recent`**: Prints `Las R mas recientes` (where `R` is the actual number of displayed songs), followed by the song names, each indented by four spaces. If the list is empty, it prints `No hay canciones recientes` instead.
- If an operation results in an error, it prints `ERROR` followed by the operation name and produces no further output.

Each test case ends with a line containing three hyphens (`---`).

## Example Input
```
addSong HumanTouch BruceSpringsteen 392
addSong BornToRun BruceSpringsteen 270
addToPlaylist BornToRun
addToPlaylist HumanTouch
play
totalTime
addSong LuckyTown BruceSpringsteen 207
addToPlaylist LuckyTown
play
play
deleteSong HumanTouch
recent 2
FIN
play
current
FIN
```

## Example Output
```
Sonando BornToRun
Tiempo total 392
Sonando HumanTouch
Sonando LuckyTown
Las 2 mas recientes
    LuckyTown
    BornToRun
---
No hay canciones en la lista
ERROR current
---
```


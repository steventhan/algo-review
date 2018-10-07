def solution(S):
    music = set(["mp3", "acc", "flac"])
    image = set(["jpg", "bmp", "gif"])
    movie = set(["mp4", "avi", "mkv"])
    files = S.split("\n")
    stat = analyze(files)
    order = ["music", "images", "movies", "other"]
    return "\n".join(["{} {}b".format(category, stat[category]) for category in order])

def analyze(files):
    categories = {
        "mp3": "music",
        "acc": "music",
        "flac": "music",
        "jpg": "images",
        "bmp": "images",
        "gif": "images",
        "mp4": "movies",
        "avi": "movies",
        "mkv": "movies"
    }
    stat = {
        "music": 0,
        "images": 0,
        "movies": 0,
        "other": 0
    }
    for file in files:
        file_name, size = file.split(" ")
        size = int(size[:-1])
        ext = file_name.split(".")[-1]
        stat[categories.get(ext, "other")] += size
    return stat

test = "my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b"
print(solution(test))

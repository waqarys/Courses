# M3-03_Changing_Lists - playlist.py
playlist = ["Roar", "Happy", "Shake", "Happy"]
print(len(playlist))
print(playlist.count("Happy"))
print(playlist.index("Shake"))
del playlist[0]
print(playlist)
playlist.extend(["Firework", "Hello"])
print(playlist)
print(len(playlist))

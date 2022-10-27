from importlib.resources import read_binary
import json
import os.path
from os import path

def main():
    print("------- Welcome to your JSON DB! -------\n")
    print("Will you be:\n1. Creating a new playlist file for a new user\n2. Adding a song to an existing playlist for a user?\n3. Adding a new playlist to an existing user?\n(Enter 1, 2, or 3)")
    sel = input()
    print(type(sel))

    while (len(sel) != 1 or int(sel) > 3 or int(sel) < 1):
        print("\nInvalid entry")
        print("Will you be:\n1. Creating a new playlist file for a new user\n2. Adding a song to an existing playlist for a user?\n3. Adding a new playlist to an existing user?\n(Enter 1, 2, or 3)")
        sel = input()

    if int(sel) == 1:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        print("What is the first song and artist you would like to add to the playlist?")
        firstsongartist = input()
        json_create(username, playlistname, firstsongartist)
    elif int(sel) == 2:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        print("What is the song and artist you would like to add to the playlist?")
        songnameartist = input()
        json_add_to_playlist(username, playlistname, songnameartist)
    elif int(sel) == 3:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        print("What is the song and artist you would like to add to the playlist?")
        songnameartist = input()
        json_add_new_playlist(username, playlistname, songnameartist)


def json_create(username, playlistname, firstsongartist):
        userfile = username + ".json"
        if not path.exists(userfile):
            data_begin = {"Playlists" : {playlistname: [firstsongartist]}}
            with open(userfile, "w") as write_file:
                json.dump(data_begin, write_file)
        else:
            print("This file already exists. Add this song to an existing playlist file.")


def json_add_to_playlist(username, playlistname, songnameartist):
    userfile = username + ".json"
    if path.exists(userfile):
        with open(userfile,"r+") as read_file: 	
            data = json.load(read_file)
            data["Playlists"][playlistname].append(songnameartist)
            read_file.seek(0)
            json.dump(data, read_file, indent=1)
    else:
        print("User has no playlist file generated. First create a playlist file.")

def json_add_new_playlist(username, playlistname, songnameartist):
    userfile = username + ".json"
    if path.exists(userfile):
        with open(userfile, "r+") as read_file:
            data = json.load(read_file)
            data["Playlists"].update({playlistname: [songnameartist]})
            read_file.seek(0)
            json.dump(data, read_file)
    else:
        print("This playlist file does not exits. Create a new file first.")





if __name__ == "__main__":
    main()
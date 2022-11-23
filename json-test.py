from importlib.resources import read_binary
import json
import os.path
from os import path

def main():
    print("------- Welcome to your JSON DB! -------\n")
    print("Will you be:\n1. Creating a new playlist file for a new user\n2. Adding a song to an existing playlist for a user?\n3. Adding a new playlist to an existing user?\n4. Viewing an existing playlist?\n5. Viewing all of a user's playlists?\n6. Deleting a song from a playlist?\n7. Deleting an entire playlist for a user?\n8. Clear an entire playlist file for a user?\n9. Listing all playlist files?\n(Enter 1, 2, 3, 4, 5, 6, 7, 8, or 9)")
    sel = input()
    print(type(sel))

    while (len(sel) != 1 or int(sel) > 9 or int(sel) < 1):
        print("\nInvalid entry")
        print("Will you be:\n1. Creating a new playlist file for a new user\n2. Adding a song to an existing playlist for a user?\n3. Adding a new playlist to an existing user?\n4. Viewing an existing playlist?\n5. Viewing all of a user's playlists?\n6. Deleting a song from a playlist?\n7. Deleting an entire playlist for a user?\n8. Clear an entire playlist file for a user?\n9. Listing all playlist files?\n(Enter 1, 2, 3, 4, 5, 6, 7, 8, or 9)")
        sel = input()

    if int(sel) == 1:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        json_create(username, playlistname)
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
        json_add_new_playlist(username, playlistname)
    elif int(sel) == 4:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        json_view_playlist(username, playlistname)
    elif int(sel) == 5:
        print("\nWhat is the user's name?")
        username = input()
        json_view_all_playlists(username)
    elif int(sel) == 6:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        json_del_song_from_playlist(username, playlistname)
    elif int(sel) == 7:
        print("\nWhat is the user's name?")
        username = input()
        print("What is the playlist's name?")
        playlistname = input()
        json_del_playlist(username, playlistname)
    elif int(sel) == 8:
        print("\nWhat is the user's name?")
        username = input()
        json_clear_playlists(username)
    else:
        json_list_files()




def json_create(username, playlistname):
        userfile = "./playlists/"  + username + ".json"
        if not path.exists(userfile):
            data_begin = {"Playlists" : {playlistname: []}}
            with open(userfile, "w") as write_file:
                json.dump(data_begin, write_file)
                print("Playlist file created for " + str(username) + " containing one playlist named " + str(playlistname) + "! ")
        else:
            print("This file already exists. Add this song to an existing playlist file.")


def json_add_to_playlist(username, playlistname, songnameartist):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile,"r+") as read_file: 	
            data = json.load(read_file)
            try:
                data["Playlists"][playlistname].append(songnameartist)
                read_file.seek(0)
                json.dump(data, read_file, indent=1)
                print("Song added to " + username + "'s playlist: " + playlistname + "!")
            except:
                print("The requested playlist does not exist. Would you like to create a new playlist with the name " + str(playlistname) + "? (Enter y or n)")
                decision = input()
                while decision != 'y' and decision != 'n':
                    print("Invalid entry")
                    print("Would you like to create a new playlist with the name " + str(playlistname) + "? (Enter y or n)")
                    decision = input()
                if decision == 'y':
                    json_add_new_playlist(username, playlistname, songnameartist)
                else:
                    print("Command aborted. Please try again.")
    else:
        print("This playlist file does not exist. Creating a new file.")
        json_create(username, playlistname)


def json_add_new_playlist(username, playlistname):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile, "r+") as read_file:
            data = json.load(read_file)
            if playlistname in data["Playlists"]:
                print("Playlist with this name already exists.")
            else:
                data["Playlists"].update({playlistname: []})
                read_file.seek(0)
                json.dump(data, read_file)
                print("Playlist named " + str(playlistname) + " created for " + str(username) + "!")
    else:
        print("This playlist file does not exist. Creating a new file.")
        json_create(username, playlistname)


def json_view_playlist(username, playlistname):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile, "r") as read_file:
            data = json.load(read_file)
            try:
                print("\n--- " + playlistname + " ---")
                for song in data["Playlists"][playlistname]:
                    print(song)
                print("\n")
            except:
                print("The requested playlist does not exist.")
    else:
        print("This playlist file does not exist. Create a new file first.")


def json_view_all_playlists(username):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile, "r") as read_file:
            data = json.load(read_file)
            print("\n--- " + username + "'s Playlists ---")
            for playlist in data["Playlists"]:
                print(playlist)
            print("\n")
    else:
        print("This playlist file does not exist. Create a new file first.")


def json_del_song_from_playlist(username, playlistname):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile, "r+") as read_file:
            data = json.load(read_file)
            try:
                i = 0
                print("\n--- Which song would you like to delete from " + playlistname + "? ---")
                for song in data["Playlists"][playlistname]:
                    print(str(i) + ". " + song)
                    i = i + 1
                print("\nMake your selection by number:")
                sel = input()
                while (len(sel) != len(str(len(data["Playlists"][playlistname]))) or int(sel) > len(data["Playlists"][playlistname]) or int(sel) < 0):
                    print("Invalid entry.")
                    print("\nMake your selection by number:")
                    sel = input()
                del(data["Playlists"][playlistname][int(sel)])
                read_file.seek(0)
                json.dump(data, read_file, indent=1)
                read_file.truncate() #Use in the case of the new data smaller than past data to eliminate any overlapping trash data.
                print("Selected song has been removed!")
            except:
                print("The requested playlist does not exist.")
    else:
        print("This playlist file does not exist. Create a new file first.")


def json_del_playlist(username, playlistname):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile, "r+") as read_file:
            data = json.load(read_file)
            try:
                del(data["Playlists"][playlistname])
                read_file.seek(0)
                json.dump(data, read_file, indent=1)
                read_file.truncate() #Use in the case of the new data smaller than past data to eliminate any overlapping trash data.
                print("Selected playlist has been removed!")
            except:
                print("The requested playlist does not exist.")
    else:
        print("This playlist file does not exist. Create a new file first.")


def json_clear_playlists(username):
    userfile = "./playlists/"  + username + ".json"
    if path.exists(userfile):
        with open(userfile, "r+") as read_file:
            data = json.load(read_file)
            try:
                data["Playlists"].clear()
                read_file.seek(0)
                json.dump(data, read_file, indent=1)
                read_file.truncate() #Use in the case of the new data smaller than past data to eliminate any overlapping trash data.
                print("All playlists have been deleted for this user!")
            except:
                print("The requested playlist does not exist.")
    else:
        print("This playlist file does not exist. Create a new file first.")


def json_list_files():
    try:    
        print("\n--- Playlist Files ---")
        file_list = os.listdir("./playlists")
        if len(file_list) == 0:
            print("There are no playlist files.")
        else:
            for file in file_list:
                print(file)
    except:
        print("Files could not be accessed.")


if __name__ == "__main__":
    main()
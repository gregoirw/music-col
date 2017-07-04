import csv
import random

def delete_space(string):
    '''
    This function deletes space in string from csv file
    '''

    string = string.strip(" ").upper()
    return string


def search_through_list(all_tuples):
    '''
    This function search through list to find proper elements.
    '''

    artist = all_tuples[0][0]
    album = all_tuples[0][1]
    year = all_tuples[1][0]
    genre = all_tuples[1][1]
    times = all_tuples[1][2]

    return artist, album, year, genre, times


start = 1

while start == 1 :

    music = []

    with open('music.csv', 'r') as music_file:
        read_csv = csv.reader(music_file, delimiter="|")

        for element in read_csv:
            element = list(map(delete_space, element))
            artist = element[0]
            album = element[1]
            year = element[2]
            genre = element[3]
            time = element[4]

            name_tuple = (artist, album)
            information_tuple = (year, genre, time)

            all_information_tuple = (name_tuple, information_tuple)

            music.append(all_information_tuple)

    menu_answer = input("\n1) Add new album\n"
                  "2) Find albums by artist\n"
                  "3) Find albums by year\n"
                  "4) Find musician by album\n"
                  "5) Find album by letter(s)\n"
                  "6) Find albums by genre\n"
                  "7) Calculate the age of all albums\n"
                  "8) Choose a random album by genre\n"
                  "0) Exit\n")

    if menu_answer == "1":

        add_ans_1 = input("Enter artist:  ")
        add_ans_2 = input("Enter name of album: ")
        while True:
            try:
                add_ans_3 = int(input("The year of album: "))
                break
            except ValueError:
                print("Well ... that isn't a year ...")
        if add_ans_3 not in range(1900,2017):
            print("Enter years in range 1900 - 2017")
            continue
        add_ans_4 = input("Enter genre of album: ")
        add_ans_5 = input("Enter duration time: ")

        print("\nNew album is added!!!\n")

        with open('music.csv', 'a') as file_write:
            file_write.writer = csv.writer(file_write, delimiter="|")
            file_write.writer.writerow([(add_ans_1),(add_ans_2),
                        (add_ans_3), (add_ans_4.lower()), (add_ans_5)])
            file_write.close()

    if menu_answer == "2":

        search_artist = input("Enter name of the artist: \n")
        for all_tuples in music:
            if search_artist.upper() == all_tuples[0][0]:
                artist, album, year, genre, times = search_through_list(all_tuples)
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)

    if menu_answer == "3":

        search_by_year = input("Enter year: \n")
        for all_tuples in music:
            if search_by_year == all_tuples[1][0]:
                artist, album, year, genre, times = search_through_list(all_tuples)
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)

    if menu_answer == "4":

        search_by_album = input("Enter name of album: \n")
        for all_tuples in music:
            if search_by_album.upper() == all_tuples[0][1]:
                artist, album, year, genre, times = search_through_list(all_tuples)
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)

    if menu_answer == "5":

        search_by_letter = input("Type letter or letters: \n")
        for all_tuples in music:
            if search_by_letter.upper() in all_tuples[0][1]:
                artist, album, year, genre, times = search_through_list(all_tuples)
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)


    if menu_answer == "6":
        search_by_genre = input("Enter genre: \n")
        for all_tuples in music:
            if search_by_genre.upper() == all_tuples[1][1]:
                artist, album, year, genre, times = search_through_list(all_tuples)
                print("\n", artist, "-", album, ",", "was released in", year, "." "\n Genre:", genre, ", Length:",
                      times)

    if menu_answer == "7":
        years = 0
        for albums in music:
            years += int(albums[1][0])

        print(years ,"years - summary time of all years")


    if menu_answer == "0":
        start = 0

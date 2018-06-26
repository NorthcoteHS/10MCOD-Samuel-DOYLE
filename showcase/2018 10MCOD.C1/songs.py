"""
Prog: Working
Date: 14/06/2018
Name: BPM Calculator
Desc: Finds the bpm and duration of different songs then prints them
"""

from selenium import webdriver ##Imports the web driver off desktop this asset must be installed prior to running the code
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import selenium

chrome_options = Options()
chrome_options.add_argument("--headless") ##This makes the chrome driver invisible
chrome_options.add_argument("--window-size=1920x1080")

chrome_driver = ("chromedriver.exe") ##Location of driver in folder
again = "yes" 
songs = []
bpms = []
lengths = []
number = 0

print("Welcome to the BPM calculator this will calculate the bpms (beats per minute) of the songs you enter and tell you how long the go for") ##Welcome message

while again == "yes" or again == "y" or again == "YES" or again == "Y" or again == "Yes":
    band = input("what is the band/artist that plays the song you would you like to add? ")
    song = input("what is the song you would you like to add? ") ##This asks the user for the songs they would like to enter
    answer = (band + " " + song)
    songs.append(answer) ##This adds the songs to the list songs
    again = input("would you like to enter another song?(yes or no) ") ##This asks the user if they would like to enter another song
    while again != "yes" and again != "y" and again != "YES" and again != "Y" and again != "Yes" and again != "no" and again != "N" and again != "NO" and again != "n" and again != "No": ## This checks if fthe user entered the correct input and asks them to correct themselves if they didnt
        again = input("invalid input please answer either yes or no ")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver) 

for song in songs:
    driver.get("https://songbpm.com/") ##This gets the driver to open to the website songbpm.com
    elem = driver.find_element_by_name("q") ##This finds the searchbar on the website
    elem.send_keys(song) ##This sends one of the inputted songs into the search bar
    elem = driver.find_element_by_id("search-button").click() ##This clicks on the search button
    try:
        bpm = driver.find_element_by_xpath("/html/body/section[2]/div/div/div/div[1]/div/a/div[3]/div/div[2]/div/p[1]").text ##This attempts to copy the bpm from the website
    except:
        bpm = ("No Song Found")
    bpms.append(bpm)
    try:
        length = driver.find_element_by_xpath("/html/body/section[2]/div/div/div/div[1]/div/a/div[3]/div/div[1]/div/p[1]").text ##This attampts to copy the length of the song from the website
    except:
        length = ("No Song Found")
    lengths.append(length)
    
driver.quit() ##This closes the driver
print("")
print("Here is a list of your songs:")

for song in songs: ##This prints the songs and their bpms
    if bpms[number] == "No Song Found":
        print("N/A")
    else:
        print("Song: " + song + " BPM: " + bpms[number] + " Length: " + lengths[number])
    number = number + 1

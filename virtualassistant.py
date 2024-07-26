import datetime
import json
import os
import random
import re
import subprocess
import time
import tkinter
import urllib
import webbrowser
import winsound
from tkinter import filedialog

import imdb
import openai
import pyautogui
import pyjokes
import PyPDF4
import pyttsx3
import pytube
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

r = sr.Recognizer()

openai.api_key = "YOUR_OPENAI_API_KEY"

brave_path = r'C:\\Path\\To\\Your\\Brave.exe'
chrome_path = r'C:\\Path\\To\\Your\\Chrome.exe'
vscode_path = r"C:\\Path\\To\\Your\\VSCode.exe"

# Define the filename for the to-do list text file
filename = r"C:\\Path\\To\\Your\\to_do_list.txt"
file_path = r"C:\\Path\\To\\Your\\reminders.txt"

# Initialize the to-do list by reading from the text file
with open(filename, "r") as f:
    to_do_list = [line.strip() for line in f.readlines()]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")

def listen_for_wake_word():
    with sr.Microphone(device_index = 0) as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source, phrase_time_limit = 20)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
        if "genie" in query.lower() or "jini" in query.lower() or "jeene" in query.lower() or "alexa" in query.lower() or "hey siri" in query.lower() or "jarvis" in query.lower() or "okay google" in query.lower():
            return True
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Genie Not Available. Your Laptop is not connected to the Internet.")
        speak("Genie Not Available. Your Laptop is not connetced to the Internet.")
    return False

def takeCommand():
    with sr.Microphone(device_index = 0) as source:
        print("Listening....")
        speak("Listening")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source, phrase_time_limit = 30)
    try:
        print("Recognizing....")
        speak("Recognizing")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you try again")
        speak("I didn't get that. Could you try again?")
        return None
    return query

def makedecision():
    with sr.Microphone(device_index = 0) as source:
        print("Listening....")
        speak("Listening")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source, phrase_time_limit = 30)
    try:
        print("Recognizing....")
        speak("Recognizing")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you try again")
        speak("I didn't get that. Could you try again?")
        return "None"
    return query

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}"
    # Send a request to the API endpoint and get the response
    response = requests.get(url)
    # Convert the response content to a JSON object
    info = json.loads(response.content)
    price = info['market_data']['current_price']['usd']
    message = f"The current price of {crypto.capitalize()} is {price} USD."
    print(message)
    speak(message)

def play_video(query):
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    query = query.replace("play video", "")
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "https://www.youtube.com/watch?v=" + search_results[0]
    print("Playing video", query)
    speak("Playing video")
    speak(query)
    webbrowser.open(url)

def play_music(query):
    query = query.replace("play music", "")
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'\"\/watch\?v=(.{11})', html_content.read().decode())
    myurl = "https://www.youtube.com/watch?v=" + search_results[0]
    youtube = pytube.YouTube(myurl)
    audio_stream = youtube.streams.filter(only_audio = True).first()
    audio_url = audio_stream.url
    print("Playing music", query)
    speak("Playing music")
    speak(query)
    os.startfile(audio_url)

def search_wikipedia(query):
    try:
        # remove the word "wikipedia" from the query string
        query = query.replace("search in wikipedia about", "")
        # search for the query on wikipedia
        results = wikipedia.summary(query, sentences=2)
        # output the results
        print("According to Wikipedia...")
        print(results)
        # speak the results using text-to-speech library
        speak("According to Wikipedia...")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        # if the search query is ambiguous, print an error message
        print("The search query is ambiguous. Please try again with a more specific query.")
        speak("The search query is ambiguous. Please try again with a more specific query.")

def read_pdf_aloud(file_path):
    # Open the PDF file in binary mode
    with open(file_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF4.PdfFileReader(file)
        # Read each page of the PDF file
        # for page_num in range(pdf_reader.numPages):
        for page_num in range(1):
            # Get the page object
            page = pdf_reader.getPage(page_num)
            # Extract the text from the page
            text = page.extractText()
            # Split the text
            mylist = text.split("\n")
            newlist = []
            newtext = ""
            for a in mylist:
                if a != "" and a != " ":
                    newlist.append(a)
            # Read each line of the PDF file
            for a in range(10):
                newtext += newlist[a] + "\n"
            print(newtext)
            speak(newtext)

def browse_file_path():
    # Create a Tkinter root widget
    root = tkinter.Tk()
    # Hide the root window
    root.withdraw()
    # Show the file browse dialog and get the selected file path
    file_path = filedialog.askopenfilename()
    # Return the selected file path
    return file_path

def handle_openai_request(query):
    # Call the OpenAI API to generate text based on the user's input
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Get the generated text from the OpenAI API response
    generated_text = response.choices[0].text.strip()
    # Speak the generated text using the text-to-speech engine
    print(generated_text)
    speak(generated_text)

def get_news():
    # Fetch news headlines from NewsAPI.org
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=d12112e7b2254e33aa50d97b1bdf0294"
    response = requests.get(url)
    data = json.loads(response.text)
    # Extract the headlines from the API response
    headlines = []
    num_headlines = 5
    for i, article in enumerate(data["articles"]):
        if i >= num_headlines:
            break
        headlines.append(article["title"])
    # Speak the headlines using the text-to-speech engine
    print(f"Here are the top {num_headlines} news headlines:")
    speak(f"Here are the top {num_headlines} news headlines:")
    for headline in headlines:
        print(headline)
        speak(headline)

def get_weather():
    print("Which city's weather you would like to here?")
    speak("Which city's weather you would like to here?")
    with sr.Microphone(device_index=0) as source:
        print("Listening....")
        speak("Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        weather = r.listen(source, phrase_time_limit=15)
        print("Recognizing....")
        speak("Recognizing")
        try:
            city = r.recognize_google(weather, language='en-in')
            # Fetch weather data from OpenWeatherMap
            api_key = "YOUR_WEATHER_API_KEY"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Error fetching weather data: {response.status_code}")
                return
            data = json.loads(response.text)
            # Extract the current weather conditions from the API response
            try:
                description = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
            except KeyError as e:
                print(f"Error parsing weather data: {e}")
                print(data)
                return
            # Speak the weather conditions using the text-to-speech engine
            print(f"The weather in {city} is {description} with a temperature of {temperature} degrees Fahrenheit and a humidity of {humidity}%.")
            speak(f"The weather in {city} is {description} with a temperature of {temperature} degrees Fahrenheit and a humidity of {humidity} percent.")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand the name of the city.")
            speak("Sorry, I didn't understand the name of the city.")

# Define a function to add a task to the to-do list
def add_task(task):
    to_do_list.append(task)
    print(f"Added '{task}' to to-do list.")
    speak(f"Added '{task}' to to-do list.")
    write_to_do_list()

# Define a function to delete a task from the to-do list
def delete_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Deleted '{task}' from to-do list.")
        speak(f"Deleted '{task}' from to-do list.")
        write_to_do_list()
    else:
        print(f"'{task}' is not in the to-do list.")
        speak(f"'{task}' is not in the to-do list.")

# Define a function to speak the to-do list
def speak_to_do_list():
    if to_do_list:
        tasks = "\n".join(to_do_list)
        print("Here are the tasks on your to-do list:")
        print(tasks)
        speak("Here are the tasks on your to-do list:")
        speak(tasks)
    else:
        print("Your to-do list is empty.")
        speak("Your to-do list is empty.")

# Define a function to write the to-do list to the text file
def write_to_do_list():
    with open(filename, "w") as f:
        for task in to_do_list:
            f.write(task + "\n")

def schedule_reminder():
    stop_reminders = False  # Variable to keep track of whether to stop reminders
    while not stop_reminders:
        # Wait for an five minutes
        time.sleep(60*5)
        # Read the to-do list from file
        with open(filename, 'r') as f:
            to_do_list = f.read()
        # Check if the to-do list is not empty
        if to_do_list.strip():
            print("Reminder: Don't forget to check your to-do list!")
            speak("Reminder: Don't forget to check your to-do list!")
            # You could play a sound or display a message here to remind the user
        # Check if the user has requested to stop the reminders
        elif stop_reminders:
            print("Hourly reminders stopped.")
            speak("Hourly reminders stopped.")

def stop_reminder():
    global stop_reminders  # Access the global variable defined in the other function
    stop_reminders = True

def add_reminder(work, reminder_time):
    with open(file_path, 'a') as f:
        f.write(f"{work}|{reminder_time}\n")
    print(f"Reminder added: {work} at {reminder_time}.")
    speak(f"Reminder added: {work} at {reminder_time}.")

def get_all_reminders():
    with open(file_path, 'r') as f:
        reminders = f.readlines()
        if not reminders:
            print("There are no reminders.")
            speak("There are no reminders.")
        else:
            for reminder in reminders:
                work, reminder_time = reminder.strip().split("|")
                print(f"{work} at {reminder_time}.")
                speak(f"{work} at {reminder_time}.")

def get_reminders():
    with open(file_path, 'r') as f:
        reminders = f.readlines()
        if not reminders:
            return None
        else:
            return [reminder.strip().split("|") for reminder in reminders]

def check_reminders():
    reminders = get_reminders()
    if not reminders:
        print("There are no reminders.")
        speak("There are no reminders.")
    else:
        now = datetime.datetime.now()
        for reminder in reminders:
            work, reminder_time_str = reminder
            reminder_time = datetime.datetime.strptime(reminder_time_str, '%Y-%m-%d %H:%M')
            if reminder_time <= now:
                print(f"Reminder: {work} at {reminder_time}.")
                speak(f"Reminder: {work} at {reminder_time}.")
                # Play a sound to remind the user
                duration = 1500  # milliseconds
                frequency = 440  # Hz
                winsound.Beep(frequency, duration)
            else:
                print("Upcoming reminder:")
                speak("Upcoming reminder:")
                print(f"{work} at {reminder_time}.")
                speak(f"{work} at {reminder_time}.")

def delete_reminder(work):
    with open(file_path, 'r') as f:
        reminders = f.readlines()
    
    with open(file_path, 'w') as f:
        for reminder in reminders:
            if reminder.strip().split("|")[0] != work:
                f.write(reminder)
    print(f"Reminder deleted: {work}.")
    speak(f"Reminder deleted: {work}.")

def parse_time(time_str):
    try:
        return datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M')
    except ValueError:
        return None

def set_alarm():
    print("What time would you like to set the alarm for?")
    speak("What time would you like to set the alarm for?")
    with sr.Microphone(device_index=0) as source:
        print("Listening....")
        speak("Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        audio_time = r.listen(source, phrase_time_limit=15)
        print("Recognizing....")
        speak("Recognizing")
        try:
            time = r.recognize_google(audio_time, language='en-in')
            hour, minute = time.split(":")
            hour = int(hour)
            minute = int(minute)
            # Set the alarm using the schtasks command
            cmd = f'schtasks /create /tn "alarm" /tr "{os.getcwd()}\\alarm.wav" /sc once /st {hour:02d}:{minute:02d} /f'
            subprocess.run(cmd, shell=True)

            # Check that the alarm was created successfully
            cmd = 'schtasks /query /tn "alarm" /v /fo list | findstr "TaskName Next Run Time Last Run Time Status"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if f"TaskName:        alarm{os.linesep}Next Run Time:   {hour:02d}:{minute:02d}" in result.stdout:
                speak("Alarm set!")
            else:
                speak("Sorry, there was an error setting the alarm.")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand your time.")
            speak("Sorry, I didn't understand your time.")

def search_movie():
    # gathering information from IMDb
    moviesdb = imdb.IMDb()
    # search for title
    print("What movie you like to search?")
    speak("What movie you like to search?")
    with sr.Microphone(device_index=0) as source:
        print("Listening....")
        speak("Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        movie_text = r.listen(source, phrase_time_limit=15)
        print("Recognizing....")
        speak("Recognizing")
        try:
            text = r.recognize_google(movie_text, language='en-in')
            # passing input for searching movie
            movies = moviesdb.search_movie(text)
            print("Searching for " + text)
            speak("Searching for " + text)
            if len(movies) == 0:
                print("No result found")
                speak("No result found")
            else:
                print("I found these:")
                speak("I found these:")
                for movie in movies:
                    title = movie['title']
                    year = movie.get('year')
                    # speaking title with releasing year
                    print(f'{title}-{year}')
                    speak(f'{title}-{year}')
                    info = movie.getID()
                    movie = moviesdb.get_movie(info)
                    print(movie.keys())
                    title = movie['title']
                    year = movie.get('original year')
                    if year is None:
                        year = movie.get('year')
                    rating = movie['rating']
                    plot = movie['plot outline']
                    # the below if-else is for past and future release
                    if year < int(datetime.datetime.now().strftime("%Y")):
                        print(f'{title} was released in {year} has IMDB rating of {rating}.\
                            The plot summary of movie is{plot}')
                        speak(f'{title} was released in {year} has IMDB rating of {rating}.\
                            The plot summary of movie is{plot}')
                        break
                    else:
                        print(f'{title} will release in {year} has IMDB rating of {rating}.\
                            The plot summary of movie is{plot}')
                        speak(f'{title} will release in {year} has IMDB rating of {rating}.\
                            The plot summary of movie is{plot}')
                        break
        except sr.UnknownValueError:
            print("Sorry, I didn't understand your movie name.")
            speak("Sorry, I didn't understand your movie name.")

def calculate():
    print("What do you want to calculate?")
    speak("What do you want to calculate?")
    question = makedecision()
    client = wolframalpha.Client('YOUR_WOLFRAM_ALPHA_API_KEY')
    res = client.query(question)
    answer = next(res.results).text
    print(answer)
    speak(answer)
    
def ask():
    print("What question do you want to ask?")
    speak("What question do you want to ask?")
    question = makedecision()
    client = wolframalpha.Client('YOUR_WOLFRAM_ALPHA_API_KEY')
    res = client.query(question)
    answer = next(res.results).text
    print(answer)
    speak(answer)

def tell_joke():
    jokes = ["Why did the tomato turn red? Because it saw the salad dressing!",
             "Why did the coffee file a police report? It got mugged!",
             "Why did the scarecrow win an award? Because he was outstanding in his field!",
             "Why don’t scientists trust atoms? Because they make up everything!",
             "Why was the math book sad? Because it had too many problems.",
             "Why don’t oysters share their pearls? Because they’re shellfish.",
             "Why can’t you hear a pterodactyl go to the bathroom? Because the pee is silent.",
             "Why did the chicken cross the playground? To get to the other slide.",
             "Why did the cookie go to the doctor? Because it was feeling crumbly.",
             "Why don't seagulls fly by the bay? Because then they would be bay-gulls.",
             "What did the janitor say when he jumped out of the closet? 'Supplies!'",
             "What did one wall say to the other? I'll meet you at the corner.",
             "Why did the banana go to the doctor? Because it wasn't peeling well.",
             "Why was the computer cold? It left its Windows open!",
             "What do you call a boomerang that doesn't come back? A stick.",
             "Why did the frog call his insurance company? He had a jump in his car.",
             "Why do they call it a drive-through if you have to stop? Shouldn't it be called a stop-and-go?",
             "Why did the hipster burn his tongue? He drank his coffee before it was cool.",
             "Why did the tomato turn green? Because it was a green tomato!",
             "Why did the cow go to outer space? To see the moooon!"
             "Why did the bicycle fall over? Because it was two-tired.",
             "What's the best way to watch a fly fishing tournament? Live stream.",
             "Why did the math book look so sad? Because it had too many problems.",
             "Why was the broom late? It swept in.",
             "Why did the tomato blush? Because it saw the salad dressing.",
             "Why don't scientists trust atoms? Because they make up everything.",
             "Why did the banana go to the doctor? Because it wasn't peeling well.",
             "What did the grape say when it got stepped on? Nothing, it just let out a little wine.",
             "Why did the bee get married? Because he found his honey.",
             "Why did the dog go to the vet? Because he was feeling ruff.",
             "Why don't ants get sick? They have tiny ant-bodies.",
             "Why don't ghosts use elevators? They lift their spirits.",
             "Why did the frog call his insurance company? He had a jump in his car.",
             "Why did the tree go to the dentist? To get a root canal.",
             "Why did the coffee file a police report? It got mugged."]
    joke = random.choice(jokes)
    print(joke)
    speak(joke)

def openApp():
    if 'open vs code' in query.lower():
        os.startfile(vscode_path)
    
    if 'open chrome' in query.lower():
        os.startfile(chrome_path)
    
    if 'open brave' in query.lower():
        os.startfile(brave_path)

def closeApp():
    if 'close vs code' in query.lower():
        os.system("taskkill /im code.exe /f")
    
    if 'close chrome' in query.lower():
        os.system("taskkill /im chrome.exe /f")
    
    if 'close brave' in query.lower():
        os.system("taskkill /im brave.exe /f")

if os.path.isfile(file_path):
    pass
else:
    with open(file_path, 'w') as f:
        pass

if __name__ == "__main__" or 1:
    count = 0

    r = sr.Recognizer()
    
    wishMe()

    print("I am a virtual assistant designed to assist you with tasks on your desktop computer. You can activate me by using a wake word.")
    speak("I am a virtual assistant designed to assist you with tasks on your desktop computer. You can activate me by using a wake word.")
    
    while True:
        
        if listen_for_wake_word():
            query = takeCommand()

            if query is not None:
                query = query.lower()
            
                if "take a break" in query or "don't listen" in query or "stop listening" in query:
                    print("For how many seconds do you want me to take a break?")
                    speak("For how many seconds do you want me to take a break?")
                    with sr.Microphone(device_index=0) as source:
                        print("Listening....")
                        speak("Listening")
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source, phrase_time_limit=15)
                        print("Recognizing....")
                        speak("Recognizing")
                        try:
                            seconds = int(r.recognize_google(audio, language='en-in'))
                            print(f"Taking a break for {seconds} seconds...")
                            speak(f"Taking a break for {seconds} seconds.")
                            time.sleep(seconds)
                            print("I'm back! How can I help you?")
                            speak("I'm back! How can I help you?")
                        except:
                            pass
                
                elif 'google search' in query:
                    query = query.replace("google search", "")
                    pywhatkit.search(query)
                    print("This is what I found")
                    speak("This is what I found")
                
                elif 'search in wikipedia about' in query:
                    search_wikipedia(query)
                
                elif 'open chat gpt' in query:
                    chrome_path = 'C:\\Path\\To\\Your\\chrome.exe'
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                    url = 'chat.openai.com\chat'
                    webbrowser.open(url)
                
                elif 'open black box' in query:
                    brave_path = 'C:\\Path\\To\\Your\\brave.exe'
                    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
                    url = 'www.useblackbox.io\home-codesearch'
                    webbrowser.open(url)
            
                elif 'open stack overflow' in query:
                    brave_path = 'C:\\Path\\To\\Your\\brave.exe'
                    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
                    url = 'stackoverflow.com'
                    webbrowser.open(url)
                
                elif 'time' in query:
                    now = datetime.datetime.now()
                    hour = now.strftime('%H')
                    min = now.strftime("%M")
                    hour = int(datetime.datetime.now().hour)
                    if hour >= 0 and hour < 12:
                        print(f"It's {hour}:{min}am")
                        speak(f"It's {hour}:{min}am")
                    else:
                        print(f"It's {hour}:{min}pm")
                        speak(f"It's {hour}:{min}pm")
                
                elif "today's date" in query:
                    today = datetime.datetime.today()
                    day = today.strftime('%A')
                    month = today.strftime('%B')
                    date = today.strftime('%d')
                    year = today.strftime('%Y')
                    print(f"It's {day}, {month} {date}, {year}.")
                    speak(f"It's {day}, {month} {date}, {year}.")
                
                elif 'play video' in query:
                    title = query.replace("play video","")
                    play_video(title)
                
                elif 'play in youtube about' in query:
                    title = query.replace("play in youtube about","")
                    play_video(title)
                
                elif 'play music' in query or 'play song' in query:
                    title = query.replace("play music","")
                    play_music(title)
                
                elif "read pdf" in query:
                    title = query.replace("read pdf", "").strip()
                    pdfname = title + ".pdf"
                    print(f"PDF file name: {pdfname}")
                    pdfpathpdf = os.path.join(r"C:\Path\To\Your\Downloads", pdfname)
                    try:
                        read_pdf_aloud(pdfpathpdf)
                    except Exception as e:
                        print("File not found! Please download and then try to read.")
                        speak("File not found! Please download and then try to read.")
                
                elif "what's your name" in query or "who are you" in query:
                    messages = ["I am Genie. Pleased to meet you!",
                                "My name? It's Genie.",
                                "My name is Genie. I'm mononymic - like Prince. Or Stonehenge. Or Smarties.",
                                "I'm Genie... here to help."]
                    message = random.choice(messages)
                    print(message)
                    speak(message)
                
                elif "who built you" in query:
                    print("I was designed by Akash Choudhary and Hrushi Bhola.")
                    speak("I was designed by Akash Choudhary and Hrushi Bhola.")
                
                elif "open ai" in query:
                    text = query.replace("open ai", "").strip()
                    handle_openai_request(text)

                # Check if user wants to add a task
                elif "add" in query:
                    task = query.split("add")[1].strip()
                    add_task(task)
                
                # Check if user wants to delete a task
                elif "delete work" in query:
                    task = query.split("delete work")[1].strip()
                    delete_task(task)
                
                # Check if user wants to speak the to-do list
                elif "read to do list" in query:
                    speak_to_do_list()
                
                elif "remind to do list" in query:
                    schedule_reminder()
                
                elif "stop to do list" in query:
                    stop_reminder()
                
                elif "remind me of" in query:
                    work = query.split("remind me of")[1].strip()
                    print("When should I remind you? Please speak the year.")
                    speak("When should I remind you? Please speak the year.")
                    with sr.Microphone(device_index=0) as source:
                        print("Listening....")
                        speak("Listening")
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio_year = r.listen(source, phrase_time_limit=15)
                        print("Recognizing year....")
                        speak("Recognizing")
                    try:
                        reminder_year = int(r.recognize_google(audio_year, language='en-in'))
                        print("Please speak the month.")
                        speak("Please speak the month.")
                        print("Listening....")
                        speak("Listening")
                        with sr.Microphone(device_index=0) as source:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audio_month = r.listen(source, phrase_time_limit=15)
                            print("Recognizing....")
                            speak("Recognizing")
                        reminder_month = int(r.recognize_google(audio_month))
                        print("Please speak the day.")
                        speak("Please speak the day.")
                        print("Listening....")
                        speak("Listening")
                        with sr.Microphone(device_index=0) as source:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audio_day = r.listen(source, phrase_time_limit=15)
                            print("Recognizing....")
                            speak("Recognizing")
                        reminder_day = int(r.recognize_google(audio_day))
                        print("Please speak the hour.")
                        speak("Please speak the hour.")
                        print("Listening....")
                        speak("Listening")
                        with sr.Microphone(device_index=0) as source:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audio_hour = r.listen(source, phrase_time_limit=15)
                            print("Recognizing....")
                            speak("Recognizing")
                        reminder_hour = int(r.recognize_google(audio_hour))
                        print("Please speak the minute.")
                        speak("Please speak the minute.")
                        print("Listening....")
                        speak("Listening")
                        with sr.Microphone(device_index=0) as source:
                            r.adjust_for_ambient_noise(source, duration=1)
                            audio_minute = r.listen(source, phrase_time_limit=15)
                            print("Recognizing....")
                            speak("Recognizing")
                        reminder_minute = int(r.recognize_google(audio_minute))
                        reminder_time = datetime.datetime(reminder_year, reminder_month, reminder_day, reminder_hour, reminder_minute)
                        reminder_time_str = reminder_time.strftime('%Y-%m-%d %H:%M')
                        if reminder_time is not None:
                            add_reminder(work, reminder_time_str)
                        else:
                            print("Invalid time format. Please try again.")
                            speak("Invalid time format. Please try again.")
                    except sr.UnknownValueError:
                        print("Sorry, I didn't understand your time.")
                        speak("Sorry, I didn't understand your time.")
                
                elif "is there any reminder" in query:
                    check_reminders()
                
                elif "read all the reminder" in query:
                    get_all_reminders()
                
                elif "delete reminder" in query:
                    work = query.split("delete reminder")[1].strip()
                    delete_reminder(work)
                
                elif "write a note" in query:
                    print("What should I write?")
                    speak("What should I write?")
                    note = makedecision()
                    with open(r'C:\Path\To\Your\notes.txt', 'a') as file:
                        print("Should I include date and time?")
                        speak("Should I include date and time?")
                        snfm = makedecision().lower()
                        if 'yes' in snfm or 'sure' in snfm:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            file.write(f"\n{strTime} :- {note}")
                        else:
                            file.write(f"\n{note}")
                    print("Note saved successfully.")
                    speak("Note saved successfully.")

                elif "show note" in query:
                    print("Showing notes")
                    speak("Showing notes")
                    with open(r'C:\Path\To\Your\notes.txt', "r") as file:
                        notes = file.readlines()
                        for note in notes:
                            print(note.strip())
                            speak(note.strip())

                elif "append note" in query:
                    print("Which note should I append?")
                    speak("Which note should I append?")
                    note_to_append = makedecision()
                    with open(r'C:\Path\To\Your\notes.txt', 'a') as file:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(f"\n{strTime} :- {note_to_append}")
                    print("Note appended successfully.")
                    speak("Note appended successfully.")
                
                elif "news" in query:
                    get_news()
                
                elif "weather" in query:
                    get_weather()
                
                elif "get crypto currency info on" in query:
                    cryptoname = query.split("get crypto currency info on")[1].strip()
                    if cryptoname.lower() == "bitcoin":
                        get_crypto_price("bitcoin")
                    elif cryptoname.lower() == "ethereum":
                        get_crypto_price("ethereum")
                    elif cryptoname.lower() == "litecoin":
                        get_crypto_price("litecoin")
                
                elif "say joke" in query:
                    tell_joke()
                
                elif "set alarm" in query:
                    set_alarm()

                elif "search movie" in query:
                    search_movie()
                
                elif "calculate" in query:
                    calculate()
                
                elif "ask" in query or "find" in query:
                    ask()
                
                elif 'jokes' in query:
                    print(pyjokes.get_joke())
                    speak(pyjokes.get_joke())

                elif "lock window" in query:
                    pyautogui.hotkey('winleft', 'l')
                
                elif "logoff" in query or "sign out" in query:
                    print("Are you sure you want to Log Off?")
                    speak("Are you sure you want to Log Off?")
                    reply = makedecision().lower()
                    if "yes" in reply:
                        time.sleep(60*5)
                        os.system("shutdown /l")
                
                elif "shutdown" in query:
                    print("Are you sure you want to Shutdown?")
                    speak("Are you sure you want to Shutdown?")
                    reply = makedecision().lower()
                    if "yes" in reply:
                        time.sleep(60*5)
                        os.system("shutdown /s /t 1")
                
                elif "restart" in query:
                    print("Are you sure you want to Restart?")
                    speak("Are you sure you want to Restart?")
                    reply = makedecision().lower()
                    if "yes" in reply:
                        time.sleep(60*5)
                        os.system("shutdown /r /t 1")
                
                elif "hibernate" in query:
                    print("Are you sure you want to Hibernate?")
                    speak("Are you sure you want to Hibernate?")
                    reply = makedecision().lower()
                    if "yes" in reply:
                        time.sleep(60*5)
                        os.system("shutdown /h")
                
                elif "empty recycle bin" in query or "mt recycle bin" in query:
                    print("Are you sure you want to empty Recycle Bin?")
                    speak("Are you sure you want to empty Recycle Bin?")
                    reply = makedecision().lower()
                    if "yes" in reply:
                        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                        print("Recycle Bin is recycled")
                        speak("Recycle Bin is recycled")
                
                elif "open chrome" in query:
                    openApp()
                
                elif "close chrome" in query:
                    print("Are you sure you want to close Google Chrome?")
                    speak("Are you sure you want to close Google Chrome?")
                    reply = makedecision().lower()
                    if "yes" in query:
                        closeApp()
                        print("Application Closed!")
                        speak("Application Closed!")

                else:
                    messages = ["That may be beyond my abilities at the moment.",
                                "That may be beyond my present skill set.",
                                "I'm afraid the features you are seeking are not currently offered.",
                                "That may be beyond my current level of proficiency"]
                    message = random.choice(messages)
                    speak(message)
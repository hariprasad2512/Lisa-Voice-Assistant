# Lisa - Voice Assistant

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Introduction

Lisa is a Python-based voice assistant capable of performing various tasks, such as answering questions, searching Wikipedia, opening websites, getting the current temperature, playing YouTube videos, taking screenshots, and more.

## Features

- Voice recognition and speech synthesis using the `speech_recognition` and `pyttsx3` libraries.
- Wikipedia search using the `wikipedia` library.
- Language translation using the `googletrans` library.
- Weather information retrieval using web scraping and the `requests` library.
- Web browsing with `webbrowser`.
- Application launch and file opening using `os` and `subprocess`.
- Battery percentage retrieval with `psutil`.
- YouTube video search and playback control with `pyautogui`.
- Screenshot capture with `pyautogui`.
- Google search with `pywhatkit`.

## Prerequisites

- Python 3.8 or higher
- Required Python packages: `bs4`, `pyttsx3`, `requests`, `wikipedia`, `webbrowser`, `speech_recognition`, `psutil`, `pyautogui`, `playsound`, `googletrans`, `pywhatkit`, `datetime`

## Usage
Run the Lisa.py script:

Upon running, Lisa will greet you and wait for your command. You can communicate with Lisa using voice commands.

Available commands:

 - "Hello" - Greet Lisa.
 - "Wikipedia <query>" - Search for information on Wikipedia.
 - "Translate <text>" - Translate the given text to various languages.
 - "Temperature" - Get the current temperature in a specified city.
 - "Open YouTube" - Open the YouTube website.
 - "Open Google" - Open the Google website.
 - "Brave" - Open the Brave browser.
 - "Battery" - Get the battery percentage of your device.
 - "Play <query>" - Search and play a YouTube video.
 - "Screenshot" - Capture a screenshot.
 - "Bye" - Say goodbye to Lisa and exit the program.

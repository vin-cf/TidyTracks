# Tidy Tracks

Tidy Tracks is designed to take your scattered Bandcamp purchases and turn them into a beautifully
organized library. Just point it to the directory where your music zip files are, and let it do the rest.

📦 Unzips All Your Purchases: No more manual unzipping!

🎧 Automatically Sorts by Artist and Album: Say goodbye to clutter!

🏷️ Reads and Processes Tags: Even works with .wav and .flac files!

🖥️ Command-Line Friendly: Perfect for those who love the terminal!


## Requirements

- Tested with Python 3.11

## Installation and Setup

Install the dependencies as specified in requirements.txt

### For Windows Users:

```
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

To run the script, run the following command in the root directory of the repository:

```
python main.py {PATH_TO_ZIP_FILES} {PATH_TO_MUSIC_LIBRARY}
```

# TODO: Support .wav tags

import eyed3
import shutil
import os
from unidecode import unidecode
import zipfile
import argparse


def unzip_all_files(dir):
    """
    Unzip all files in the directory
    @param dir: Directory containing music zip files
    """
    zipfiles = [os.path.join(dir, f) for dir, dirs, files in os.walk(dir) for f in files if (f.endswith('.zip'))]
    [zipfile.ZipFile(zip, "r").extractall(dir) for zip in zipfiles]


def move_file(source, destination, message=None):
    """
    Move a file from source to destination
    @param source:
    @param destination:
    @param message:
    @return: None
    """
    if message:
        print(message)
    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f'ERROR: Failed to move file {source} to {destination} due to {e}')


def process_audio_files(sourcedir, musicdir):
    suff_list = [".mp3", ".wav", ".flac", ".aiff", ".mp4"]
    audiofiles = [os.path.join(dir, f) for dir, dirs, files in os.walk(sourcedir) for f in files if
                  f.endswith(tuple(suff_list))]

    for audiofile in audiofiles:
        print(f'Checking file {audiofile}')
        file_tags = eyed3.load(audiofile)
        if not file_tags:
            if audiofile.endswith((".wav", ".flac")):
                move_file(audiofile, musicdir, f'Moved {audiofile} to {musicdir}')
            continue

        # TODO: Remove diacritics when santitising name:
        # https://stackoverflow.com/questions/48445459/removing-diacritical-marks-using-python
        sanitised_artist_name = unidecode(file_tags.tag.artist.replace('/', '_'))
        sanitised_album_name = unidecode(
            file_tags.tag.album.replace('/', '_')) if file_tags.tag.album else "Unknown Album"
        artist_dir = os.path.join(musicdir, sanitised_artist_name)
        album_dir = os.path.join(artist_dir, sanitised_album_name)

        if not os.path.exists(artist_dir):
            print(f'Creating Artist folder {sanitised_artist_name} in {musicdir}')
            os.mkdir(artist_dir)

        if sanitised_album_name not in os.listdir(artist_dir):
            print(f'Creating Album folder {sanitised_album_name} in {album_dir}')
            os.mkdir(album_dir)

        try:
            shutil.move(audiofile, album_dir)
        except Exception as e:
            print(f'ERROR: Failed to move file {audiofile} to {album_dir} due to {e}')


def main(sourcedir, musicdir):
    unzip_all_files(sourcedir)
    process_audio_files(sourcedir, musicdir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Provide music directory path")
    parser.add_argument('sourcedir', type=str, help='Path to the directory containing unsorted zip files')
    parser.add_argument('musicdir', type=str, help='Path to the music directory to unzip files')
    args = parser.parse_args()
    main(args.sourcedir, args.musicdir)

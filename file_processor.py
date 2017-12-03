import io
import os

from google.cloud.speech import types

def open_file(path, name):
    file_name = os.path.join(
        os.path.dirname(__file__),
        path,
        name)

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    return audio

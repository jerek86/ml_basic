import datetime
import os
from abc import abstractmethod

class MediaFile:
    name: str
    size_byte: int
    create_date: datetime
    owner: str

    payload = bytearray()

    def create(self):
        with open(self.name, mode = 'wb') as file:
            self.write_header(file)
            file.write(self.payload)

    def delete(self):
        if os.path.exists(self.name):
            os.remove(self.name)

    @abstractmethod
    def write_header(self, file):
        raise NotImplementedError

class AudioFile(MediaFile):
    codec: str
    bit_rate: int

    # write format specific header data
    def write_header(self, file):
        file.write()

class VideoFile(MediaFile):
    audio_codec: str
    bit_rate: int

    video_codec: str
    width: int
    height: int

    # write format specific header data
    def write_header(self, file):
        file.write()

class PhotoFile(MediaFile):
    codec: str
    width: int
    height: int

    # write format specific header data
    def write_header(self, file):
        file.write()

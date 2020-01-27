#!/usr/bin/python3
import unittest
from spotify_bash_control.metadata_provider import MetadataProvider

"""
song spotify:track:2WKOn2ElTv5X3EuqlPPYqE
"""


class MetaDataProviderTestCase(unittest.TestCase):

    def setUp(self):
        self.provider = MetadataProvider()

    def test_metadata_provider_can_provide_song_id(self):
        song_id = self.provider.get_current_song_id()

        self.assertEqual(song_id, '2WKOn2ElTv5X3EuqlPPYqE')

    def test_metadata_provider_can_provide_song_title(self):
        song_name = self.provider.get_current_song_name()

        self.assertEqual(song_name, 'Auf Wiedersehen')

    def test_metadata_provider_can_provide_album(self):
        album_name = self.provider.get_current_album()

        self.assertEqual(album_name, 'Auf Wiedersehen')

    def test_metadata_provider_can_provide_artist(self):
        artist = self.provider.get_current_artist()

        self.assertEqual(artist, 'Finder')

    def test_full_metadata_can_be_provided(self):
        metadata = self.provider.get_current_song_metadata()
        self.assertEqual(11, len(metadata))


if __name__ == '__main__':
    unittest.main()

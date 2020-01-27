#!/usr/bin/python3
import dbus


class MetadataProvider:
    __spotify_property_interface = None
    __spotify_song_metadata = None

    def __init_spotify_interface(self):
        """Init a new spotify session bus if not present"""
        if self.__spotify_property_interface is None:
            session_bus = dbus.SessionBus()
            try:
                proxy_object = session_bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
                self.__spotify_property_interface = dbus.Interface(proxy_object, 'org.freedesktop.DBus.Properties')
            except dbus.DBusException:
                print('Could not create dbus proxy maybe, spotify player is not available')
                exit(1)

        return self.__spotify_property_interface

    def get_current_song_metadata(self):
        """Get metadata of current played song"""
        interface = self.__init_spotify_interface()
        self.__spotify_song_metadata = interface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

        return self.__spotify_song_metadata

    def get_current_song_id(self):
        """Get current spotify song id"""
        if self.__spotify_song_metadata is None:
            self.get_current_song_metadata()

        return self.__spotify_song_metadata['mpris:trackid'].replace('spotify:track:', '')

    def get_current_song_name(self):
        """Get current song name"""
        if self.__spotify_song_metadata is None:
            self.get_current_song_metadata()

        return self.__spotify_song_metadata['xesam:title']

    def get_current_album(self):
        """Get current album"""
        if self.__spotify_song_metadata is None:
            self.get_current_song_metadata()

        return self.__spotify_song_metadata['xesam:album']

    def get_current_artist(self):
        """Get current artist"""
        if self.__spotify_song_metadata is None:
            self.get_current_song_metadata()

        return self.__spotify_song_metadata['xesam:artist'][0]


if __name__ == '__main__':
    mdp = MetadataProvider()
    print(mdp.get_current_song_metadata())
    print(mdp.get_current_song_id())
    print(mdp.get_current_song_name())
    print(mdp.get_current_album())
    print(mdp.get_current_artist())

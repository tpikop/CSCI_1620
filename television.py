class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a Television object with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television. If muted, sets volume to MIN_VOLUME.
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume = self.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increases the channel by 1, considering the maximum channel value.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decreases the channel by 1, considering the minimum channel value.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increases the volume by 1, considering the maximum volume value.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MAX_VOLUME
            elif self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1, considering the minimum volume value.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MIN_VOLUME
            elif self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the Television object.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

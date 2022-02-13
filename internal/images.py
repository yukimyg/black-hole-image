import dataclasses


@dataclasses.dataclass(frozen=True)
class Sd:
    height: int = 480
    width: int = 640


@dataclasses.dataclass(frozen=True)
class Hd:
    height: int = 720
    width: int = 1280


@dataclasses.dataclass(frozen=True)
class Fhd:
    height: int = 1080
    width: int = 1920


@dataclasses.dataclass(frozen=True)
class Qhd:
    height: int = 1440
    width: int = 2560


@dataclasses.dataclass(frozen=True)
class Uhd:
    height: int = 2160
    width: int = 3840


@dataclasses.dataclass(frozen=True)
class Fuhd:
    height: int = 4320
    width: int = 7680

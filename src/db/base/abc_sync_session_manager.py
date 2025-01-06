from abc import ABC, abstractmethod


class BaseSyncSessionManager(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def sync_session(self):
        pass

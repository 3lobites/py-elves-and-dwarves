from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname}"
              f" has bow of the {str(self._bow_level)} level")

    def get_rating(self) -> int:
        return self._bow_level * 3
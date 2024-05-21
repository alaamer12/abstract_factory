from __future__ import annotations
from abc import ABC, abstractmethod


class CharacterFactory(ABC):
    @abstractmethod
    def create_warrior(self):
        pass

    @abstractmethod
    def create_mage(self):
        pass


class HumanFactory(CharacterFactory):
    def create_warrior(self):
        return HumanWarrior()

    def create_mage(self):
        return HumanMage()


class ElfFactory(CharacterFactory):
    def create_warrior(self):
        return ElfWarrior()

    def create_mage(self):
        return ElfMage()


class Warrior(ABC):
    @abstractmethod
    def attack(self):
        pass


class Mage(ABC):
    @abstractmethod
    def cast_spell(self):
        pass


class HumanWarrior(Warrior):
    def attack(self):
        print("Human Warrior attacks with a sword!")


class HumanMage(Mage):
    def cast_spell(self):
        print("Human Mage casts fireball!")


class ElfWarrior(Warrior):
    def attack(self):
        print("Elf Warrior attacks with a bow!")


class ElfMage(Mage):
    def cast_spell(self):
        print("Elf Mage casts frostbolt!")


def main():
    # Create factories
    human_factory = HumanFactory()
    elf_factory = ElfFactory()

    # Create characters
    human_warrior = human_factory.create_warrior()
    human_mage = human_factory.create_mage()
    elf_warrior = elf_factory.create_warrior()
    elf_mage = elf_factory.create_mage()

    # Interact with characters
    human_warrior.attack()
    human_mage.cast_spell()
    elf_warrior.attack()
    elf_mage.cast_spell()


if __name__ == "__main__":
    main()

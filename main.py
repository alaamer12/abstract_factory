from __future__ import annotations
from abc import ABC, abstractmethod


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Abstract Product
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


# Abstract Product
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# Concrete Factory for macOS
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


# Concrete Product for Windows
class WindowsButton(Button):
    def paint(self):
        return "Render a Windows style button"


# Concrete Product for Windows
class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Render a Windows style checkbox"


# Concrete Product for macOS
class MacOSButton(Button):
    def paint(self):
        return "Render a MacOS style button"


# Concrete Product for macOS
class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Render a MacOS style checkbox"


class Application:
    def __init__(self, factory):
        self.factory = factory

    def create_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()

        print(f"{button.paint()}\n{checkbox.paint()}")


# Client code
def main():
    windows_factory = WindowsFactory()
    app = Application(windows_factory)
    app.create_ui()

    macos_factory = MacOSFactory()
    app = Application(macos_factory)
    app.create_ui()


if __name__ == "__main__":
    main()

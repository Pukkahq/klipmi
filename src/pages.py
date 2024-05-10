"""
Copyright 2024 Joe Maples <joe@maples.dev>

This file is part of OpenQ1Display.

OpenQ1Display is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

OpenQ1Display is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
OpenQ1Display. If not, see <https://www.gnu.org/licenses/>. 
"""

import logging

from collections.abc import Callable
from nextion import EventType
from state import State
from utils import SimpleDict

def registerPages() -> SimpleDict:
    pages = SimpleDict()

    # pages[BasePage.name] = BasePage
    pages[BootPage.name] = BootPage
    pages[MainPage.name] = MainPage

    return pages

class BasePage:
    name = ""
    id = -1

    def __init__(self, state: State, changePageCallback: Callable):
        self.state = state
        self.changePageCallback = changePageCallback

    async def init(self):
        """Implimented on a page-by-page basis"""

    async def onDisplayEvent(self, type: EventType, data):
        logging.info("Event %s data: %s", type, str(data))

    async def onPrinterStatusUpdate(self, data: dict):
        """Implimented on a page-by-page basis"""

    async def onFileListUpdate(self, data: dict):
        """NO-OP for non-files pages"""

    def changePage(self, page: str):
        self.changePageCallback(page)


class BootPage(BasePage):
    name = "boot"
    id = 0

    async def init(self):
        await self.state.display.set('version.val', 18)

class MainPage(BasePage):
    name = "main"
    id = 15
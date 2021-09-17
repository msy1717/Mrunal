# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from MrunalOP.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for search youtube quire Telegram Groups .\n\n✅ Send me /help for more info."
    HELP_MSG = [
        ".",
         f"""
**Hey 👋 Welcome back to {PROJECT_NAME}
⚪️ {PROJECT_NAME} can search music or video for you
""",
         f"""
**=>> Song Download 🎸**
- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer
**=>> Search Tools 📄**
- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",
       ]

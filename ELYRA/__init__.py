from ELYRA.core.bot import JARVIS
from ELYRA.core.dir import dirr
from ELYRA.core.git import git
from ELYRA.core.runtime_patches import apply_runtime_patches
from ELYRA.core.userbot import Userbot
from ELYRA.misc import dbb, heroku
from ELYRA.security import drop_sensitive_env_vars

from .logging import LOGGER

dirr()
git()
dbb()
heroku()
apply_runtime_patches()

app = JARVIS()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

_removed_sensitive_env = drop_sensitive_env_vars()
if _removed_sensitive_env:
    LOGGER(__name__).info(
        "Security hardening active: stripped %s sensitive env vars from process environment.",
        len(_removed_sensitive_env),
    )

import config
from ELYRA import app
from ELYRA.button_styles import primary_button, success_button


def hide_public_owner_info(text: str) -> str:
    markers = {
        "tg://openmessage?user_id=",
        "t.me/abouttorix",
        "t.me/iflexalgorithm",
    }
    if config.OWNER_USERNAME:
        markers.add(f"t.me/{str(config.OWNER_USERNAME).lstrip('@')}".casefold())

    blocks = text.split("\n\n")
    return "\n\n".join(
        block
        for block in blocks
        if not any(marker in block.casefold() for marker in markers)
    ).strip()


def start_panel(_):
    buttons = [
        [
            primary_button(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            success_button(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            primary_button(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            success_button(text=_["S_B_4"], url=config.SUPPORT_CHAT),
        ],
        [
            primary_button(text=_["S_B_3"], callback_data="open_help"),
        ],
    ]
    return buttons

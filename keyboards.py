import emoji
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callbackdata import CategoryInfo, RatingInfo


def get_start_keyboard():

    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text="русские", callback_data=CategoryInfo(category="russian")
    )
    keyboard_builder.button(
        text="теща", callback_data=CategoryInfo(category="mother_in_low")
    )
    keyboard_builder.button(
        text="отношения", callback_data=CategoryInfo(category="sex")
    )
    keyboard_builder.button(
        text="штирлиц", callback_data=CategoryInfo(category="pidors")
    )
    keyboard_builder.button(
        text="измена", callback_data=CategoryInfo(category="treason")
    )
    keyboard_builder.button(
        text="религия", callback_data=CategoryInfo(category="religion")
    )
    keyboard_builder.button(
        text="коммунизм", callback_data=CategoryInfo(category="komunism")
    )
    keyboard_builder.button(
        text="я победил!!!", callback_data=CategoryInfo(category="all")
    )

    keyboard_builder.adjust(4, 3, 1)

    return keyboard_builder.as_markup()


def get_jokes_keyboard(category, joke_id):

    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text=emoji.emojize(":thumbs_down:"),
        callback_data=RatingInfo(changes="-1", joke_id=joke_id),
    )
    keyboard_builder.button(
        text="следующий", callback_data=CategoryInfo(category=category)
    )
    keyboard_builder.button(
        text=emoji.emojize(":heart_with_arrow:"),
        callback_data=RatingInfo(changes="1", joke_id=joke_id),
    )
    keyboard_builder.button(text="вернуться в меню", callback_data="main_menu")

    keyboard_builder.adjust(3, 1)

    return keyboard_builder.as_markup()

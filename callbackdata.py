from aiogram.filters.callback_data import CallbackData


class CategoryInfo(CallbackData, prefix='category'):
    category: str


class RatingInfo(CallbackData, prefix='rating'):
    changes: int
    joke_id: int

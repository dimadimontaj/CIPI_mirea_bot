# import asyncio
#
# import config
# from db_api import quick_commands as commands
# from db_api.db_gino import db
#
#
# async def db_test():
#     await db.set_bind(config.POSTGRES_URI)
#     await db.gino.drop_all()
#     await db.gino.create_all()
#
#     await commands.add_joke(category='русские', jokes='шутка 1')
#     await commands.add_joke(category='теща', jokes='шутка 2')
#     await commands.add_joke(category='религия', jokes='шутка 3')
#
#     jokes = await commands.select_all_jokes()
#     print(jokes)
#     jokes = await commands.select_category_jokes('русские')
#     print(jokes)
#     jokes = await commands.select_joke(1)
#     print(jokes)
#     jokes = await commands.change_rating(2, 1)
#     print(jokes)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(db_test())
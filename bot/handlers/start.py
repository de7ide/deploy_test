from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router(name="start-router")


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    data = await state.get_data()
    occurrence = data.get("occurence", 0)
    if occurrence == 0:
        text = "Привет! Это Счетчик команнды /start"
    else:
        text = f"Уже нажмякал: {occurrence} раз"
    await message.answer(text)
    await state.update_data(occurrence=occurrence+1)

from src.app.utils.textes import *
import random


def get_emoji_by_streak(streak) -> tuple[int, int]:
    emotion_start, emotion_end = '', ''
    emotions_keys = list(emotions.keys())
    for i in range(len(emotions_keys) - 1):
        now = emotions_keys[i]
        next = emotions_keys[i + 1]
        if now < streak < next:
            emotion_start, emotion_end = emotions[emotions_keys[i]]
            break
        elif streak > next:
            emotion_start, emotion_end = emotions[emotions_keys[i + 1]]
    return emotion_start, emotion_end


def get_random_text() -> str:
    return random.choice(text_streak_increment)


def get_beauty_streak(streak: int) -> str:
    return f"\n**Серия {abs(streak)}**"


def text_constructor(streak) -> str:
    beauty_streak = get_beauty_streak(streak)
    text = ''
    if streak in ura_texts.keys():
        text = ura_texts[streak]
    else:
        congratulations = get_random_text()
        emoji_start, emoji_end = get_emoji_by_streak(streak)
        text = emoji_start + congratulations + emoji_end[::-1]
    text += beauty_streak
    return text


def get_text_by_streak(streak, lost=False):
    if lost:
        streak = -1
    text = text_constructor(streak)
    return text
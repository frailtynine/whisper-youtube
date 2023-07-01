import decode
import download


PROMPT = (
    'ЧВК Вагнера, '
    'Ходорковский, '
    'Пригожин, '
    'Пастухов, '
    'Газпром, '
    'Ростов-на-Дону, '
    'Рейтер, '
    'Шендерович, '
    'Малаховская, '
    'Воронеж, '
    'Липецк, '
    'Шойгу, '
    'Песков, '
    'Иноземцев, '
    'Лукашенко, '
    'преемник, '
    'мятежник, '
    'Крутихин, '
    'Ренат Давлетгильдеев, '
)

url = 'https://www.youtube.com/watch?v=Y2pu-3stIbI'
audio = download.download_audio(url)
decode.transcribe(audio, PROMPT)

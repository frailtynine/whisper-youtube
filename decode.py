import whisper
import datetime


def transcribe(file: str, initial_promt: str):
    '''
        Test and transcribe given audio with prompt.
        Use difficult words like names, brands
        and toponyms for prompt to clean the result.
    '''
    model = whisper.load_model('small')
    audio = whisper.load_audio(file)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions(
        language='ru',
        without_timestamps=False,
        fp16=False
    )

    result = whisper.decode(model, mel, options)
    print(result.text)
    result = model.transcribe(audio=file,
                              verbose=False,
                              word_timestamps=True,
                              initial_prompt=initial_promt)
    date = datetime.datetime.now().strftime('%d%m%y%H%M')
    with open(f'result{date}.txt', 'w') as text:
        text.write(result['text'])

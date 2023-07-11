import openai

KEY = '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'

file = open('audio_2023-06-27_21-37-5.mp3', 'rb')

result = openai.Audio.transcribe(
    api_key=KEY,
    model='whisper-1',
    file=file,
    response_format='text'

)

print(result)
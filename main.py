from openai import OpenAI
import os
from dotenv import load_dotenv
import whisper
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPEN_AI_KEY')
)

audio_files = [f for f in os.listdir('./audiofiles') if f.endswith('m4a')]

model = whisper.load_model("small")

#completions = []

with open('output.json', 'a') as file_obj,open('seen_files.txt', 'a') as seen_files:
    for audio_file in audio_files:
        base_name = os.path.splitext(audio_file)[0]
        with open(f"./audiofiles/{base_name}.info.json") as metadata:
            metadata_json = json.load(metadata)

            result = model.transcribe(f"./audiofiles/{audio_file}")

            info = {
                'text': result['text'],
                'description': metadata_json['description'] if 'description' in metadata_json else '',
                'title': metadata_json['title']  if 'title' in metadata_json else '',
                'url': metadata_json['webpage_url'] if 'webpage_url' in metadata_json else ''
            }

            print(f"Generated transcription: {info}")

            #gpt-4-1106-preview
            completion = client.chat.completions.create(
              model="gpt-4-1106-preview",
              response_format={"type": "json_object" },
              messages=[
                {"role": "system",
                 "content": """Take a json object that contains the fields "text" and "description". Combine the values of those fields to produce a single text value, then summarize this text value by generating a list of up to 5 keywords. You can generate less than 5, but you must generate at least one. The keywords you generate must be concrete and specific. The must be nouns or noun phrases. Words like "hammering", "saw", "lobbing", and "pencil" are concrete and specific, so include words like those in your list of keywords. Words like "skill" and "control" are too abstract so do not include words like that in your list of keywords. Proper names and brand names are ok to include. Take the keywords you generate and append them to the original json object under the field name "keywords". Give me back the new json object you create."""},
                {"role": "user", "content": f"Here is the json object: {json.dumps(info)}"},
                {"role": "user", "content": """Words like "skill" are too abstract. Don't include them in your list of keywords. And don't include "framing" ever. And remember that you are allowed to generate less than 5 keywords. 5 is the maximum number of keywords and 1 is the minumum."""},
                {"role": "user", "content": """Gerunds are good words to include in your list of keywords. Gerunds like "sawing", "measuring", etc."""}
              ]
            )
            print(f"Generated completion: {completion.choices[0].message.content}")
            file_obj.write(f"{json.dumps(completion.choices[0].message.content)}\n")
            seen_files.write(f"{audio_file}\n")

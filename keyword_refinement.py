import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# sample keywords
# [
#     "coil framing nailer",
#     "coil nailers",
#     "pasload nailer",
#     "chop saw",
#     "circular saw",
#     "makita saw",
#     "metabo hpt rear handle saw",
#     "steel nailer",
#     "concrete nailer",
#     "@martineztools",
#     "@strongtie",
#     "rafter",
#     "plate level",
#     "stabila level",
#     "ridge beam",
#     "rakewall",
#     "toenailing",
#     "snapping lines",
#     "wall lifting",
#     "wall sheathing",
#     "wall puller"
#     "bird blocks", 
#     "birdsmouth", 
#     "birdsmouth layout", 
#     "blade", 
#     "blade brake", 
#     "blades", 
#     "blocking", 
#     "blocking walls", 
#     "brace", 
#     "bracing"
# ]

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPEN_AI_KEY')
)

index = {}

keywords = []

with open('./output.json') as data_file:
    for line in data_file:
        try:
            first = json.loads(line)
            entry = json.loads(first)
            for keyword in entry["keywords"]:
                keywords.append(keyword.lower())
        except:
             print("decode error")


sorted_keywords = sorted(list(set(keywords)))

print(len(sorted_keywords))

def generate_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

chunks = generate_chunks(sorted_keywords, 100)

from openai import OpenAI
client = OpenAI()


messages = [
    {
        "role": "system",
        "content": "You are given a list of keywords. Group similar keywords and create a category name for each group.\n\nSome context: words begining with \"@\" are social media handles. Words begining with \"#\" are social media hashtags. \"birdsmouth\" relates to rafter cutting.\n\nIf you have trouble categorizing a word, just make it a standalone group by itself.\n\nPrefer specific categories with fewer members over more general categories with more members. Having a category with only one member is better than lumping together keywords that are only slightly related. \n\nCheck the output list against the original given list to make sure no keywords are missing from your output. Confirm that you have done this and tell me if any are missing.\n\nReturn your response as a json object with the category name as the key and the group of words as the object. Do not snake case the keys. Instead, keep normal spacing for the keys."
    },
    {
        "role": "user",
        "content": "Here are the keywords: [\n    \"coil framing nailer\",\n    \"coil nailers\",\n    \"pasload nailer\",\n    \"chop saw\",\n    \"circular saw\",\n    \"makita saw\",\n    \"metabo hpt rear handle saw\",\n    \"steel nailer\",\n    \"concrete nailer\",\n    \"@martineztools\",\n    \"@strongtie\",\n    \"rafter\",\n    \"plate level\",\n    \"stabila level\",\n    \"ridge beam\",\n    \"rakewall\",\n    \"toenailing\",\n    \"snapping lines\",\n    \"wall lifting\",\n    \"wall sheathing\",\n    \"wall puller\"\n    \"bird blocks\", \n    \"birdsmouth\", \n    \"birdsmouth layout\", \n    \"blade\", \n    \"blade brake\", \n    \"blades\", \n    \"blocking\", \n    \"blocking walls\", \n    \"brace\", \n    \"bracing\",\n\"lobbing\"\n]\n"
    },
    {
        "role": "assistant",
        "content": "```json\n{\n  \"Power Tools\": [\n    \"coil framing nailer\",\n    \"coil nailers\",\n    \"pasload nailer\",\n    \"chop saw\",\n    \"circular saw\",\n    \"makita saw\",\n    \"metabo hpt rear handle saw\",\n    \"steel nailer\",\n    \"concrete nailer\"\n  ],\n  \"Social Media Handles\": [\n    \"@martineztools\",\n    \"@strongtie\"\n  ],\n  \"Carpentry Framing Techniques\": [\n    \"rafter\",\n    \"toenailing\",\n    \"snapping lines\",\n    \"wall lifting\",\n    \"wall sheathing\",\n    \"bird blocks\",\n    \"birdsmouth\",\n    \"birdsmouth layout\",\n    \"blocking\",\n    \"blocking walls\",\n    \"brace\",\n    \"bracing\"\n  ],\n  \"Levels\": [\n    \"plate level\",\n    \"stabila level\"\n  ],\n  \"Carpentry Structural Components\": [\n    \"ridge beam\",\n    \"rakewall\"\n  ],\n  \"Saw Blade Items\": [\n    \"blade\",\n    \"blade brake\",\n    \"blades\"\n  ],\n  \"Standalone Keywords\": [\n    \"lobbing\",\n    \"wall puller\"\n  ]\n}\n```\n\nI"
    },
    {
        "role": "user",
        "content": "\"Power tools\" is too broad a category.  Break it up by type of power tool--e.g. saws, nailers, etc. \"Carpentry Framing Techniques\" is also too broad a category. It should be broken up into smaller categories--'nailing', 'walls', 'rafters', 'roofs', etc. Good job on preserving spacing in the object keys. Keep doing that. "
    },
    {
        "role": "assistant",
        "content": "```json\n{\n  \"Nailers\": [\n    \"coil framing nailer\",\n    \"coil nailers\",\n    \"pasload nailer\",\n    \"steel nailer\",\n    \"concrete nailer\"\n  ],\n  \"Saws\": [\n    \"chop saw\",\n    \"circular saw\",\n    \"makita saw\",\n    \"metabo hpt rear handle saw\"\n  ],\n  \"Saw Blades\": [\n    \"blade\",\n    \"blade brake\",\n    \"blades\"\n  ],\n  \"Social Media Handles\": [\n    \"@martineztools\",\n    \"@strongtie\"\n  ],\n  \"Rafters\": [\n    \"rafter\",\n    \"bird blocks\",\n    \"birdsmouth\",\n    \"birdsmouth layout\"\n  ],\n  \"Levels\": [\n    \"plate level\",\n    \"stabila level\"\n  ],\n  \"Roof Framing Techniques\": [\n    \"toenailing\",\n    \"brace\",\n    \"bracing\"\n  ],\n  \"Wall Construction\": [\n    \"rakewall\",\n    \"wall lifting\",\n    \"wall sheathing\",\n    \"blocking\",\n    \"blocking walls\",\n    \"wall puller\"\n  ],\n  \"Line Work\": [\n    \"snapping lines\"\n  ],\n  \"Standalone Keywords\": [\n    \"ridge beam\",\n    \"lobbing\"\n  ]\n}\n```\nI have reviewed the original list of keywords and can confirm that all are present in the categorized output. No keywords are missing."
    },
    {
        "role": "user",
        "content": "\"brace\", \"bracing\", and \"toenailing\" are more properly classified as \"Wall construction\". \"Roof construction\" would be stuff like \"rolling trusses\" or \"setting rafters\". The way you broke down power tools is great. Keep doing that but try again on the \"Roof Framing Techniques\" category."
    },
    {
        "role": "assistant",
        "content": "```json\n{\n  \"Nailers\": [\n    \"coil framing nailer\",\n    \"coil nailers\",\n    \"pasload nailer\",\n    \"steel nailer\",\n    \"concrete nailer\"\n  ],\n  \"Saws\": [\n    \"chop saw\",\n    \"circular saw\",\n    \"makita saw\",\n    \"metabo hpt rear handle saw\"\n  ],\n  \"Saw Blades\": [\n    \"blade\",\n    \"blade brake\",\n    \"blades\"\n  ],\n  \"Social Media Handles\": [\n    \"@martineztools\",\n    \"@strongtie\"\n  ],\n  \"Rafters\": [\n    \"rafter\",\n    \"bird blocks\",\n    \"birdsmouth\",\n    \"birdsmouth layout\"\n  ],\n  \"Levels\": [\n    \"plate level\",\n    \"stabila level\"\n  ],\n  \"Wall Construction\": [\n    \"brace\",\n    \"bracing\",\n    \"toenailing\",\n    \"rakewall\",\n    \"wall lifting\",\n    \"wall sheathing\",\n    \"blocking\",\n    \"blocking walls\",\n    \"wall puller\"\n  ],\n  \"Line Work\": [\n    \"snapping lines\"\n  ],\n  \"Standalone Keywords\": [\n    \"ridge beam\",\n    \"lobbing\"\n  ]\n}\n```\nI have reassigned \"brace,\" \"bracing,\" and \"toenailing\" to the \"Wall Construction\" category and eliminated the \"Roof Framing Techniques\" category, moving all keywords to more appropriate categories. The original keyword list has been re-checked and included correctly in this updated JSON structure. No keywords are missing."
    },
    {
        "role": "user",
        "content": "Excellent. One last thing: Make each standalone keyword it's one category. So for example the key should be \"Lobbing\" and the value should be \"['lobbing']\"."
    },
    {
        "role": "assistant",
        "content": "```json\n{\n  \"Nailers\": [\n    \"coil framing nailer\",\n    \"coil nailers\",\n    \"pasload nailer\",\n    \"steel nailer\",\n    \"concrete nailer\"\n  ],\n  \"Saws\": [\n    \"chop saw\",\n    \"circular saw\",\n    \"makita saw\",\n    \"metabo hpt rear handle saw\"\n  ],\n  \"Saw Blades\": [\n    \"blade\",\n    \"blade brake\",\n    \"blades\"\n  ],\n  \"Social Media Handles\": [\n    \"@martineztools\",\n    \"@strongtie\"\n  ],\n  \"Rafters\": [\n    \"rafter\",\n    \"bird blocks\",\n    \"birdsmouth\",\n    \"birdsmouth layout\"\n  ],\n  \"Levels\": [\n    \"plate level\",\n    \"stabila level\"\n  ],\n  \"Wall Construction\": [\n    \"brace\",\n    \"bracing\",\n    \"toenailing\",\n    \"rakewall\",\n    \"wall lifting\",\n    \"wall sheathing\",\n    \"blocking\",\n    \"blocking walls\",\n    \"wall puller\"\n  ],\n  \"Line Work\": [\n    \"snapping lines\"\n  ],\n  \"Ridge Beam\": [\n    \"ridge beam\"\n  ],\n  \"Lobbing\": [\n    \"lobbing\"\n  ]\n}\n```\nEach standalone keyword is now in its own category as requested."
    },
    {
        "role": "user",
        "content": "Good. \"Ridge beam\" has to do with \"roof construction\" so reclassify it."
    },
    {
        "role": "assistant",
        "content": "```json\n{\n  \"Nailers\": [\n    \"coil framing nailer\",\n    \"coil nailers\",\n    \"pasload nailer\",\n    \"steel nailer\",\n    \"concrete nailer\"\n  ],\n  \"Saws\": [\n    \"chop saw\",\n    \"circular saw\",\n    \"makita saw\",\n    \"metabo hpt rear handle saw\"\n  ],\n  \"Saw Blades\": [\n    \"blade\",\n    \"blade brake\",\n    \"blades\"\n  ],\n  \"Social Media Handles\": [\n    \"@martineztools\",\n    \"@strongtie\"\n  ],\n  \"Rafters\": [\n    \"rafter\",\n    \"bird blocks\",\n    \"birdsmouth\",\n    \"birdsmouth layout\"\n  ],\n  \"Levels\": [\n    \"plate level\",\n    \"stabila level\"\n  ],\n  \"Wall Construction\": [\n    \"brace\",\n    \"bracing\",\n    \"toenailing\",\n    \"rakewall\",\n    \"wall lifting\",\n    \"wall sheathing\",\n    \"blocking\",\n    \"blocking walls\",\n    \"wall puller\"\n  ],\n  \"Line Work\": [\n    \"snapping lines\"\n  ],\n  \"Roof Construction\": [\n    \"ridge beam\"\n  ],\n  \"Lobbing\": [\n    \"lobbing\"\n  ]\n}\n```\n\"Ridge beam\" has been recategorized under \"Roof Construction\". As before, the list has been checked and no keywords are missing from the output."
    }
]

with open('keyword_output.json', 'a') as keyword_file:
    for chunk in chunks:
        print(f"grouping chunk {chunk}")
        new_message = {
            "role": "user",
            "content": f"I am going to give you more keywords. Group them as you did the previous keywords. If they fit into a category you've already created, then put them there. If not, create a new category. Here are the keywrods: {chunk}"
        }
        messages.append(new_message)
        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            max_tokens=4095,
            response_format={"type": "json_object" },
            messages=messages
        )

        keyword_file.write(f"{completion.choices[0].message.content}\n")


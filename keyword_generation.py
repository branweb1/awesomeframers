import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPEN_AI_KEY')
)

keywords = ['Track Saw', 'Zip R6 Sheathing', 'Makita Tools', 'Chainsaw', 'Battery Cordless', 'Makita Tools', 'Exterior Wafer Head Screws', 'Simpson Strong Tie', 'Sliding Glass Door', 'Roof framing', 'Rafters', 'Zip R6 Sheathing', 'Cascadia railing', 'women in the trades', 'IBS2023', 'Siga Tape', 'Siga Blue', 'Building Science', 'KEENutility', 'basketball', 'LP ProStruct', 'stud heights', 'chalk line', 'top plates', 'nailer weight', 'High Pressure Coil Nailer', 'Max HN90FHigh Pressure Nailer', 'Paslode Cordless Nailer', 'Metal Connector Nailer', 'Positive Placement Nailer®', 'custom home', 'fireplace', 'Instagram', 'Max HN90FHigh Pressure Nailer', 'Zip R6 Sheathing', 'Siga Tape', 'Advantech Subfloor Adhesive', 'iJoyce', 'screw pulls', 'Stabila LA-180', 'concrete', 'remote control', 'powder actuated tool', 'PINWP nail', 'Halo Interra', 'telehandler', 'Zip R6 Sheathing', 'part107certified', 'birdsmouth', 'rafter length', 'MetaboHPT rear handle', 'jlconline', 'education', 'Building Science', 'router with a handle', '1/4" bit', 'MetaboHPT router', 'M79 head', 'M1 handle', 'form work', 'Benjamin Obdyke Slicker Classic', 'LP ProStruct', 'Temple Tape', 'cordless rear handle saws', 'MetaboHPT rear handle', 'Makita XGT', 'jig', 'MetaboHPT rear handle', 'bird blocks', 'Max HN90FHigh Pressure Nailer', 'concrete', 'Simpson Strong Tie', 'rake walls', "king's dud", 'wall sheathing', 'belt hook', 'Max HN90FHigh Pressure Nailer', 'coil framing nailer', 'truss', 'counterweight', '2x6', 'concrete', 'Advantech', 'Contraction Joints', 'Max HN90FHigh Pressure Nailer', 'concrete', 'Building Science', 'Building Science', 'finger joints', 'glulam', 'martinezhammer', 'framerlife', 'hammerchallenge', 'coffee', 'Dutch Bros', 'Instagram', 'Advantech', 'cleaning technique', 'foam application', 'roof framing', 'glulam', '2x12 rafters', 'top flange hangers', 'RidgidLam LVL', 'hanger load tables', 'postyourmistakes', 'pre-fab', 'wing wall', 'Interior walls', 'siding', 'part107certified', 'CompanyCam', 'documentation', 'geo tagged', 'roof framing', 'KEENutility', 'tape measure', '@panasoniciaq WhisperComfort 60', 'CFM control', 'IntelliBalance 100', 'roof', 'ardoise', 'renovation', 'Simpson Strong Tie', 'router with a handle', 'Dewalt', 'Huber', 'Stabila LA-180', 'concrete', 'plumb', 'bearing plates', 'Dude Tools socket', 'mudsill', 'fireplace', 'laser plumb bob', 'Instagram', 'Stabila LA-180', 'laser plumb bob', 'subfloor', 'glulam', 'engineered wood', 'concrete', 'Slope Shield Plus SA', 'Advantech', 'concrete', 'Halo Interra', 'powder actuated tool', 'Simpson Strong Tie', 'Max HN90FHigh Pressure Nailer', 'concrete', 'hearing protection', 'structural screws', 'Stabila LA-180', 'laser plumb bob', 'framerlife', 'Zip R6 Sheathing', 'Huber', 'anchor bolt', 'Dude Tools socket', 'hearing protection', 'vertical sheeting', 'insulation', 'labor', 'level', 'TheRationalBuilder', 'geometry', 'Paslode Cordless Nailer', 'hearing protection', 'telehandler', 'miniexcavator', 'kubota', 'stair landing', 'Advantech', 'hearing protection', 'porch rafters', 'Big Foot Tools', 'gang cutting', 'Roof framing', 'Stabila LA-180', 'California Jacks', 'tape test', 'adhesive', 'pull test', 'chalk line', 'concrete', 'hearing protection', 'chainsaw', 'manufacturing', 'ASMR', 'Big Foot Tools', 'beam saws', 'Diablo blade', 'recip blade', 'toenail', 'wall lift', 'tie down straps', 'Beck America Nailer', 'structural one zip sheathing panel', 'Milwaukee Tools', 'brushless lithium ion', 'jump cuts', 'Cascadia railing', 'deck building', 'IBS2023', 'ASMR', 'Rock Wool', 'insulation', 'World of Concrete', 'Martinez Tools', 'giveaway', 'dronevideo', 'whiteriverfalls', 'part107certified', '#TheRationalBuilder', '@truewerk', 'smartside', 'concrete', 'hearing protection', 'Diablo blade', 'iJoyce', 'cutting holes', 'Boise Cascade', 'Stabila LA-180', 'concrete', 'hearing protection', 'stair stringers', 'Makita XGT', 'Diablo blade', '#framersareadyingbreed', 'lift your legs', 'trace', 'jig', '#framersareadyingbreed', 'hearing protection', 'Advantech', 'end stud', 'Milwaukee Tools', 'stud layout', 'Advanced Framing', 'TheRationalBuilder', 'Martinez Tools', '12-inch square', 'geometry', '#framersareadyingbreed', 'framerlife', 'KEENutility', 'handmade boots', 'leather boots', 'ASMR', 'hearing protection', 'Zip System', '#framersareadyingbreed', 'Instagram', '#framer', 'sprinter', 'Makita XGT', 'tracksaw', 'Advanced Framing', '#framersareadyingbreed', '2x12', 'teamwork', 'Simpson Strong Tie', 'Makita XGT', 'Stabila LA-300G', 'Big Pee Vee wall puller', '2000 pound rake wall', 'no squeaks', 'Zip System', 'stretch tape', 'Building Science', 'Instagram', 'Cascadia railing', 'TheRationalBuilder', 'Las Vegas', 'Zip System', 'hearing protection', 'concrete', 'shear wall', 'Simpson Strong Tie', 'anchor bolts', 'tilt turn windows', '@crossfitgames', 'maintenance problem', 'hammer', 'Max HN90FHigh Pressure Nailer', 'toenail', '@strongtie Quick Stik', 'SDWC structural screw', '#acrobat', 'Novoform', 'foundation forming', 'QR code', 'ASMR', 'Advantech', 'hearing protection', 'iJoyce', 'fasteners', 'engineering', 'Beam Wrench', 'IsoTunes Hearing Protection', 'Concrete', 'Makita XGT', 'cordless beam saw', 'hearing protection', '#framersareadyingbreed', 'deadeye', '@jamesjeantrickshots', '#TheRationalBuilder', 'rake wall', 'telehandler', 'Makita XGT', 'beam saws', 'safety glasses', 'smartside', 'concrete', 'hearing protection', 'Advantech Subfloor Adhesive', 'Mavic 3', 'Huber', 'Huber', 'Concrete', 'Zip R6 Sheathing', 'Zip R6 Sheathing', 'seismic zone D2', '#framersareadyingbreed', 'iJoyce', 'rim installation', 'toenail', 'bowed stud', 'straightening a stud', '45 degree cut', 'Advantech', 'Max HN90FHigh Pressure Nailer', 'hearing protection', 'Makita XGT', 'cordless', 'rebar', 'jigsaw', 'Diablo blade', 'ISOtunes Hearing Protection', 'I Joists', '@drdecks', 'Stabila LA-180', 'concrete', 'Subaru symmetrical all wheel drive', 'RidgidLam LVL', 'Makita XGT', '#framersareadyingbreed', 'MetaboHPT Triple Hammer', 'Simpson Strong Tie', 'SDWS timber screws', 'IsoTunes Hearing Protection', 'chainsaw', 'acrylic tape', '#framersareadyingbreed', 'Zip System', 'telehandler', 'fall protection', 'Zip System', 'hearing protection', '#framersareadyingbreed', 'corded saw', 'Simpson Strong Tie', 'roof framing', 'glulam', 'giveaway', "Nick's Handmade Boots", 'YouTube', 'googleit', 'Advantech', 'chalk line', 'RidgidLam LVL', 'Advantech', 'Astrophotography', 'SonyA7IV', 'manual focus', 'martineztools', 'framer', 'Worcestershire sauce', 'Stiletto Tibone hammers', 'magnets', '#framersareadyingbreed', '#framer', 'graceful', 'viral', 'beam saws', 'wheelchair ramp', 'ASMR', 'Advantech', "Nick's Handmade Boots", 'Paslode Cordless Nailer', 'HVAC', 'I Joists', '#TheRationalBuilder', '#framersareadyingbreed', 'siding', 'smartside']

with open('output.json') as entries, open('generated_keywords.txt', 'a') as keyword_output_file:
    seek_complete = False
    for line in entries:
        try:
            entry = json.loads(json.loads(line))
            if 'url' not in entry:
                continue
            if entry['url'] == 'https://www.instagram.com/reel/CyrJyyky-Iz/':
                seek_complete=True
                continue
            if seek_complete:
                transcription = f"{entry['description']} {entry['text']}"
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo-1106",
                    response_format={"type": "json_object" },
                    messages=[
                        {
                            "role": "system",
                            "content": f"You are a librarian whose job it is to classify videos. You are provided with a video transcript, and you must summarize the transcript using keywords from the transcript. \n\nThe keywords must be concrete and specific. All these videos are about carpentry and framing, so the terms \"carpentry\", \"framing\", \"carpentry skills\", and the like are bad keywords that you must not use.\n\nYou can use a maximum of three keywords to summarize a video transcript. You can use fewer than three, but you must use at least one.\n\nCheck each of your keywords against this list of keywords: {keywords}. If there is a keyword in the list similar to yours, use the one from the list instead. If not, use yours.\n\nGive your response as a valid json object where the key is 'keywords' and the response is a json array of strings."
                        },
                        {
                            "role": "user",
                            "content": transcription
                        }
                    ]
                )
                generated_keywords = json.loads(completion.choices[0].message.content)['keywords']
                print(f"generated keywords {generated_keywords} for transcript {transcription}")
                keywords = keywords + generated_keywords
                obj = {}
                if 'url' in entry:
                    obj[entry['url']] = generated_keywords
                    print(f"writing {obj} to file")
                    keyword_output_file.write(json.dumps(obj))
                    keyword_output_file.write('\n')
        except json.decoder.JSONDecodeError:
            print("decode errror")

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import base64

with app.app_context():
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/goldenretriever.jpg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description = "Max is a 2-year-old Golden Retriever with boundless energy and a playful personality. He requires a lot of time and attention. He also loves to be active and play games."
            name = "Max"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/siberian_husky.jpg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description = "Saddie is a 3-year-old Siberian Husky with boundless energy and a playful spirit. Saddie needs plenty of exercise and mental stimulation to keep her happy and healthy."
            name = "Saddie"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/bordercollie.jpeg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description = "Collin is a 4-year-old Border Collie with a sleek black and white coat and an insatiable appetite for activity. He's highly intelligent and loves to play games like frisbee and fetch."
            name = "Collin"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/australianshepard.jpeg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Lucy is a 3-year-old Australian Shepherd that loves to stay active and play games with her humans. She's highly intelligent and always up for an adventure."
            name = "Lucy"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/beagle.jpeg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Charlie is a 2-year-old Beagle with a distinctive howl and an insatiable curiosity. He's always eager to follow his nose and explore his surroundings. He loves to play games like hide-and-seek with his humans."
            name = "Charlie"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/terrier.jpg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Bella is a 4-year-old Jack Russell Terrier with a spunky personality and an adventurous spirit. She's a high-energy dog that loves to play and explore."
            name = "Bella"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/dalmation.jpg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Milo is a 5-year-old Dalmatian with striking black spots on his white coat. He's a friendly and energetic dog that loves to play and run. He's always up for an adventure."
            name = "Milo"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/images/boxer.jpeg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Chloe is a 3-year-old Boxer with a playful personality and a contagious enthusiasm for life. She's a high-energy dog that is always up for a game of fetch or tug-of-war."
            name = "Chloe"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/irishsetter.jpeg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Lola is a 5-year-old Irish Setter that exudes elegance and playfulness. She's always eager to explore her surroundings and loves to play games like frisbee and fetch."
            name = "Lola"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
    filepath = '/Users/anijain/Documents/GitHub/TSACoding2023/australian cattle dog.jpeg'
    with open(filepath, 'rb') as f:
            file_data = f.read()
            encoded_data = base64.b64encode(file_data)
            base64image = encoded_data
            description =  "Rocky is a 4-year-old Australian Cattle Dog with a distinctive black and brown coat and a high-energy personality. He's a natural herder and loves to stay active."
            name = "Rocky"
            new_entry = Entry(base64Val=str(base64image), description=description, name=name)
            db.session.add(new_entry)
            db.session.commit()
import json

class database:
    def __init__(self):
        self.name = "database.db"
    def save(self):
        data = {}
        data['people'] = []
        data['people'].append({
            'name': 'Scott',
            'website': 'pythonist.ru',
            'from': 'Nebraska'
        })
        data['people'].append({
            'name': 'Larry',
            'website': 'pythonist.ru',
            'from': 'Michigan'
        })
        data['people'].append({
            'name': 'Tim',
            'website': 'pythonist.ru',
            'from': 'Alabama'
        })
        with open(self.name, 'w') as outfile:
            json.dump(data, outfile)

    def open():
        with open(self.name) as json_file:
            data = json.load(json_file)
            for p in data['people']:
                print('Name: ' + p['name'])
                print('Website: ' + p['website'])
                print('From: ' + p['from'])
                print('')

database.save
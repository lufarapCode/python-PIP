import requests 

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    
    #Que significa el status_code ->  https://realpython.com/python-requests/#:~:text=your%20GET%20request.-,Status%20Codes,looking%20for%20was%20not%20found.
    print(r.status_code)
    print(r.headers)
    # print(r.text)

    
    categories = r.json()
    print(type(categories))

    for category in categories:
        print(category['image'])


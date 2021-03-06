import json

def save_result_in_json_file(data, filename):
    """save result in a json file

    Keyword Arguments:
        filename {str} -- the filename (and path) that the data will be save in
        data {str} -- the data that I need to save

    Returns:
        Bool -- Wheter the data is save or not
    """
    #save the data in JSON file so that the Flask app can read it
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json_file(filename):
    """read a json file

    Keyword Arguments:
        filename {str} -- Reading a JSON file

    Returns:
        [dict] -- the contect of the file
    """
    try:
        #reading secrets.json to connect to db
        with open(filename) as json_file:
                data = json.load(json_file)
        return data
    except:
        raise FileNotFoundError("file not found")

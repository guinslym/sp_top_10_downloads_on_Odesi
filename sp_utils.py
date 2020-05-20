import json

def save_result_in_json_file(filename, data):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] 
        data {str} -- [description] 

    Returns:
        [type] -- [description]
    """
    try:
        #save the data in JSON file so that the Flask app can read it
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except:
        print("error on filename creation")
        return False

def read_json_file(filename):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description])

    Returns:
        [type] -- [description]
    """
    try:
        #reading secrets.json to connect to db
        with open('secrets.json') as json_file:
                data = json.load(json_file)
        return data
    except:
        print( "File {0} not found".format(file))
        return dict()
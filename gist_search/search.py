#from gist_search.utils import get_gists
from utils import get_gists
result_list=[]

def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    gists = get_gists(username)   
    for gist in gists:
        if description and file_name:
            pass
        elif description:
            if description.lower() in gist['description'.lower()]:
                result_list.append(result_list)
        elif file_name:
            pass
    return result_list   
                
gists = search_gists("santiagobasulto",file_name ="time")
for gist in gists:
    print("{:<40} | {}".format(gist['id'],gist['description']))
import requests_with_caching
import json
def get_movie_data(s): 
    baseurl = 'http://www.omdbapi.com/'     
    param_diction=dict()
    param_diction['t']=s
    param_diction['r']='json'
    resp = requests_with_caching.get(baseurl, params=param_diction)
    return resp.json()
di=get_movie_data('Black Panther')
#print(di)
def get_movie_rating(di):
    raw = (di['Ratings'])
    #print(raw)
    for i in raw:
        if i['Source'] == 'Rotten Tomatoes':
            string = i['Value']
            raw1=string[:-1]
            #print(raw1)
            fi=int(raw1)
            #print(fi)
            return fi
        else:
            return 0        

def get_sorted_recommendations(lm):
    rel = get_related_titles(lm)
    sorted_rel=sorted(rel, reverse=True)
    #print(sorted_rel)
    #rating = [(get_movie_rating(get_movie_data(x)) for x in sorted_rel)]
    order = sorted(sorted_rel, key=lambda y:(-get_movie_rating(get_movie_data(y)), y), reverse=True)
    print(order)    
    return order      

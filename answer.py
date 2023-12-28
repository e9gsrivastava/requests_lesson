import random
import re 
import requests
'''below code reads all the urls of a page and returns a dict '''
def answer():
    '''this func returns a a dict with key as status code and val as urls showing that status code'''
    r=requests.get('https://httpbin.org')
    data=r.text
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

    my_list=[i for i in urls]

    num=random.randint(1,len(my_list))

    random_urls=random.choices(my_list, k=num)
    
    final_urls=[i for i in random_urls]

    my_dict={}
    for i in final_urls:
        if requests.get(i).status_code in my_dict:
            my_dict[requests.get(i).status_code].append(i)
        else:
            my_dict[requests.get(i).status_code]=[i]


    return my_dict
if __name__=='__main__':
    print(answer('https://www.google.com/search?channel=fs&client=ubuntu&q=w3schools'))
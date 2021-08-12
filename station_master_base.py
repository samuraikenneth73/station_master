import requests, re
main_link = "https://erail.in/"
start = input()
stop = input()
get_trains = main_link+"/trains-between-stations/{}/{}".format(start,stop)

source = requests.get(get_trains).text
regex_dates = r'\d{2}-\w{3}-\d{4}_\d{2}:\d{2}'
new = re.findall(r'data-train=\'\d{5}.*_\d\d-\w{3}-\d{4}_\d{2}:\d{2}',source)

time_info = re.findall(regex_dates,str(new))
print("all trains departure times")
print(time_info[::2])
print("all trains arrival times")
print(time_info[1::2])
trains_info = re.sub(regex_dates,"",str(new))
# the variable trains lists all available trains with train id
trains = re.findall(r'[A-Z_0-9\s]+',str(trains_info))
print("train id's are")
train_id = re.findall(r'\d{5}',str(trains))
print(train_id)
ft = re.sub(r'\s',"_",str(trains))
almost_clean_trains = re.findall(r'([A-Za-z_]*)',ft)
trains_group = re.compile(r"(?P<trains>\w+[^_'])")
train_match = list(filter(trains_group.match,almost_clean_trains))
final_train_list = [c[1:-2] for c in train_match]
print("name of trains are")
print(final_train_list)
cleaner = re.sub(r"'.',|\s'',\s|\s''|'',\s|''","",str(almost_clean_trains))
print(cleaner)




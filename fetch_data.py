import os
import requests
from dotenv import load_dotenv
from table2ascii import table2ascii, PresetStyle

load_dotenv()
KEY = os.environ['DISCOURSE_API_KEY']


url = "https://forum.tecommons.org/admin/users/list/active.json"
res = requests.get(url, headers={'Api-Key': KEY, 'Api-username': 'system'})
data = [[
    u['username'],
    f"{u['time_read']/3600}h",
    str(u['posts_read_count']),
    str(u['post_count'])] for u in res.json()]

output = table2ascii(
    header=["Name", "Time Read", "Posts Read", "Posts Created"],
    body=data,
    style=PresetStyle.ascii_box
)
print(output)

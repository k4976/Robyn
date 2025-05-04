from robyn import Response


# rb = robyn.Robyn()


# d = robyn.Response(200, headers={'content-type':"application/json"}, description='{"hello": "world"}', response_type="json")
# d = Response(200, headers={'content-type':"application/json"}, description='{"hello": "world"}')
d = Response(200, headers={"content-type": "application/json"}, description='{"hello": "world"}', response_type=None)

# d.response_type = "json"
d.description = '{"heo": "world"}'

print(dir(d))
print(d)
print(repr(d))
print(str(d))
print(d.description)
print(d.response_type)

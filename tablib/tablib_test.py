import tablib

data = [
    {
        "a": "1",
        "b": "2",
        "c": "3"
    },
    {
        "a": "4",
        "b": "5",
        "c": "6"
    }
]

object_data = tablib.Dataset(*data)
print object_data.json
print object_data.yaml

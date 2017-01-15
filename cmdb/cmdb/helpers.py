# Todo: Remove this from the presented version

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


def test_deserialize(serializer_class, input_data, instance=None):

    print("Converting data to JSON")
    content = JSONRenderer().render(input_data)
    print("Converting to Byte stream")
    stream = BytesIO(content)
    print("Parsing stream")
    data = JSONParser().parse(stream)
    if instance:
        print("Instantiating Update serializer class with data")
        ser = serializer_class(instance, data=data)
    else:
        print("Instantiating Create serializer class with data")
        ser = serializer_class(data=data)

    print("Validating data")
    if ser.is_valid():
        print("Saving")
        ser.save()
    else:
        print("Data is invalid")

    return ser


def test_vdata(serializer_class, input_data, instance=None):

    print("Converting data to JSON")
    content = JSONRenderer().render(input_data)
    print("Converting to Byte stream")
    stream = BytesIO(content)
    print("Parsing stream")
    data = JSONParser().parse(stream)
    if instance:
        print("Instantiating Update serializer class with data")
        ser = serializer_class(instance, data=data)
    else:
        print("Instantiating Create serializer class with data")
        ser = serializer_class(data=data)

    return ser
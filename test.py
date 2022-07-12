import base64


def decode(uid):
    result = base64.b64decode(uid)
    print(result)


def decode_array(uid_array):

    for item in uid_array:
        result = base64.b64decode(item)
        print(result)


uid = 'dmlyYWctdmlyc2xpMUBnbWFpbC5jb20='

uid_array = (
    'dmlyYWctdmlyc2xpMUBnbWFpbC5jb20=',
    'YXJ0ZW0ta3Vob21leGFodWsuYWlAZ21haWwuY29t',
    'eW5vdGVrMjAxNi15bm90ZWsyMDE2QGdtYWlsLmNvbQ==',
)

#  one
# decode(uid)

# array list uid
decode_array(uid_array)
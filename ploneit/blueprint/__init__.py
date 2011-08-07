import urllib
from xmlrpclib import Binary


def get_file(item, base_field_name, url, auth=None):
    if auth:
        split_url = url.split('/')
        split_url[2] = '%s:%s@%s' % (auth[0], auth[1], split_url[2])
        url = '/'.join(split_url)
    response = urllib.urlopen(url)

    # 'file': 'image content',
    # 'file.filename': 'image.jpg',
    # 'file.mimetype': 'image/jpeg',},
    info = response.info()
    file_name = ''
    try:
        file_name = info.dict['content-disposition'].split('=')[1].replace('"','')
    except:
        file_name = url.split('/')[-1]

    mimetype = info.type

    item[base_field_name + '.filename'] = file_name
    item[base_field_name + '.mimetype'] = mimetype
    return Binary(response.read())


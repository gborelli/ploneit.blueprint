import urllib
# import cStringIO
# from OFS.Image import File
from xmlrpclib import Binary


def get_file(item, base_field_name, url):
    split_url = url.split('/')
    split_url[2] = 'giorgio:giorgio@' + split_url[2]
    url = '/'.join(split_url)
    response = urllib.urlopen(url)

    # 'file': 'image content',
    #  'file.filename': 'image.jpg',
    #  'file.mimetype': 'image/jpeg',},

    # file_name = 'immagine.jpg'
    # if url.endswith('leadImage'):
    #     file_name = url.split('/')[-2] + '.' + response.info().type.split('/')[-1]
    # else:

    file_name = url.split('/')[-1]
    item[base_field_name + '.filename'] = file_name
    item[base_field_name + '.mimetype'] = 'image/jpeg'
    return Binary(response.read())

    # return 
    # return Binary(File(file_name, file_name, cStringIO.StringIO(response.read()).getvalue(), response.info().type))


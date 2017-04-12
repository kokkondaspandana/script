import dropbox

flow = dropbox.client.DropboxOAuth2FlowNoRedirect('xary9q5nh6dhoqw', 'cdl3dod2vuj16im')


client = dropbox.client.DropboxClient('ZQ6BnaZjisAAAAAAAAAAC1ko4P9bfGZBn0j9HisOFIT3mu0PtEXEq0uP9PL90fCe')
print 'linked account: ', client.account_info()

f = open('sample.txt', 'rb')
response = client.put_file('/magnum-opus1.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus1.txt')
out = open('magnum-opus1.txt', 'wb')
out.write(f.read())
out.close()
print metadata

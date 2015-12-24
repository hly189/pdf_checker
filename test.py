import mechanize
br = mechanize.Browser()
response=br.open("http://www.example.com/")
target_url='http://www.rfc-editor.org/rfc/rfc2606.txt'
for link in br.links():
    print(link)
    # Link(base_url='http://www.example.com/', url='http://www.rfc-editor.org/rfc/rfc2606.txt', text='RFC 2606', tag='a', attrs=[('href', 'http://www.rfc-editor.org/rfc/rfc2606.txt')])
    print(link.url)
    # http://www.rfc-editor.org/rfc/rfc2606.txt
    if link.url == target_url:
        print('match found')
        # match found            
        break

br.follow_link(link)   # link still holds the last value it had in the loop
print(br.geturl())
# http://www.rfc-editor.org/rfc/rfc2606.txt
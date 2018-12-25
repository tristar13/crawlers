
def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html
    print(response)
    # Parse the rest of the page to extract structured data.

    if url = 'http://kg.akipress.org/':
        header = _gettext(page.xpath('//body/div[5]//a'))
    elif url = 'http://bilim.akipress.org/ru':
        header = _gettext(page.xpath('//body/div[@class]/div[3]/div/div[@class][2]//div[@class]/a'))
        
    #header = _gettext(page.xpath('//div[@class]/h1/text()'))
    #header2 = _gettext(page.xpath('//div[@class='news_body']/h1[@class='newsheadline_title']/text()'))
    #header3 = _gettext(page.xpath('//div[@class='area_block']/div[@class='news_body']/text()'))
    #foto = _gettext(page.xpath('//div[@class]/img/@src'))
    #foto2 = _gettext(page.xpath('//div[@class='area_block']/div[@class='news_body']/div[@class='photoin']/img/@src'))


    article_data = {
        "url": response.url,
        "header": header
        #"foto": foto
        #"foto2":  foto2
    }

    if article_data["header"] is not None:
        # If 'rule' is not set, it defaults to 'pass', which triggers the
        # final 'store' stage.
        context.emit(data=article_data)

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.


    header = _gettext(page.xpath('.//div/h2/text()'))
    foto = _gettext(page.xpath('//div[@class]/img[@class]/@src'))
    #date= _gettext(page.xpath('//div/div[3]/span[1]'))
    
    article_data = {
        "url": response.url,
        "header": header,
        "foto": foto,
        #"date": date
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
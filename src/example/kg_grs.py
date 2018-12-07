def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html
    
    
    # Parse the rest of the page to extract structured data.


    
    org_data = {
        "url": response.url,
        
    }

  
    
    

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
       
    
    for i in range(len('//tbody/tr')):
        result = {}
        id = _gettext((page.xpath('//tbody/tr/td[2]//p/text()')))
        street_kg = _gettext((page.xpath('//tbody/tr/td[3]//p/text()')))
        street_ru = _gettext((page.xpath('//tbody/tr/td[4]//p/text()')))
        old_street_kg = _gettext((page.xpath('//tbody/tr/td[5]//p/text()')))
        old_streetru = _gettext((page.xpath('//tbody/tr/td[6]//p/text()')))
        district = _gettext((page.xpath('//tbody/tr/td[7]//p/text()')))
        result['street'] = street
        #emit(data=org_data)
        #result['emit']  = emit
        print(result)
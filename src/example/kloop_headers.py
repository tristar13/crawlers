<<<<<<< HEAD
import re

=======
>>>>>>> ce447570fec0988c10acb7ca34eced58c5db1f51
def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

    header = _gettext(page.xpath('.//header/h1/text()'))
<<<<<<< HEAD

    article_data = {
        "url": response.url,
        "header": header
=======
    picture = _gettext(page.xpath('(.//div[@class="stk-mask"]/img/@src)[1]')) 

    article_data = {
        "url": response.url,
        "header": header,
		"picture": picture
>>>>>>> ce447570fec0988c10acb7ca34eced58c5db1f51
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
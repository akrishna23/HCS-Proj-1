try:
card = soup.find(id='ires').find_all(class_='g')[0]

label = card.h3.text + '\n' if card.h3 is not None else ''

overview = card.img.attrs['title'] + '\n' if card.img is not None and card.img.has_attr('title') else ''
restaurant = 'Restaurant: ' + card.find_all(text=re.compile(‘cui-merchant-name cui-truncate’))[0] + ‘\n’ if len(card.find_all(text=re.compile(‘cui-merchant-name cui-truncate’))) > 0 else ''
	coupon = ‘Coupon: ‘ + card.find_all(text=re.compile(‘cui-url should-truncate’))[0] + ‘\n’ if len(card.find_all(text=re.compile(‘cui-url should-truncate’))) > 0 else ''
	description = ‘Description: ‘ + card.find_all(text=re.compile(‘cui-description’))[0] + ‘\n’ if len(card.find_all(text=re.compile(‘cui-description’))) > 0 else ''
	image = card.img.attrs[‘c550x332q85.jpg’] + ‘\n’ if card.img is not None and
card.img.has_attr(‘c550x332q85.jpg’) else '' 

body = label
body += overview
body += restaurant	
body += coupon
body += description
body += image

    except Exception, e:
        print str(e)
        return "Could not find coupons. Are you sure you gave a proper type of food?"

    return body











###############################
#####Coupon Function Core######
###############################

def makeSpecial():
    s = 'To get the coupons for a particular city, use the format \'coupon city foodstyle\'.'
    return s

## return proper format to use for getting coupons
special = makeSpecial()

def eval(input):
    return getCoupons(input)



#pip install python-whois

import whois

sites = ["youtube.com", "spotify.com"]

companies = [whois.whois(s).org for s in sites]
creation_dates = [whois.whois(s).creation_date for s in sites]

print(companies)
print(creation_dates)

print(sites[creation_dates.index(min(creation_dates))])

emails = [whois.whois(s).emails for s in sites]
print(emails)

#simple
#res = whois.whois("youtube.com")
#print(res)
#print(res.org)
#print(res.creation_date)

#print(whois.whois("IP ADDRESS"))
#will show who own that domain,
#not always show the real owner of that domain
#usually show up the hosting provider
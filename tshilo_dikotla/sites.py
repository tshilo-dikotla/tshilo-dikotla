fqdn = 'td.bhp.org.bw'

td_site = (
    (40, 'gaborone'),
)


def get_site_id(name):
    return [site for site in td_site if site[1] == name][0][0]

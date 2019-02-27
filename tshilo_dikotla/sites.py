fqdn = 'td.bhp.org.bw'

td_site = (
    (40, 'gaborone', 'Gaborone'),
)


def get_site_id(name):
    print('>>>>>>>>>>>>>>>>>>>>.')
    return [site for site in td_site if site[1] == name][0][0]

from __future__ import print_function

import pytest

from rdap import RdapAsn
from rdap import RdapNotFoundError


def assert_parsed(data, parsed):
    # dump in json format for easily adding expected
    print("echo \\\n'{}'\\\n > {}/{}.expected".format(data.dumps(parsed), data.path, data.name))
    assert data.expected == parsed


def test_rdap_asn_lookup_not_found(rdapc):
    with pytest.raises(RdapNotFoundError):
        rdapc.get_asn(65535)


@pytest.RequestsData("rdap") # XXX , real_http=True)
def test_rdap_asn_lookup(rdapc, data_rdap_autnum):
    print(data_rdap_autnum.name)
    #asn = rdap.get_asn(205726)
    asn = rdapc.get_asn(data_rdap_autnum.name)
    assert_parsed(data_rdap_autnum, asn.parsed())

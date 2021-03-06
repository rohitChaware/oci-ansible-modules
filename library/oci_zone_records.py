#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: oci_zone_records
short_description: Update or Patch a collection of records in the specified zone in OCI DNS Service
description:
    - This module allows the user to update or patch a collection of records in the specified DNS zone in OCI DNS
      Service.
version_added: "2.5"
options:
    zone_id:
        description: The OCID of the target zone. Either I(name) or I(zone_id) must be specified to update or path
                     the collection of records in the specified zone.
        required: false
        aliases: ['id']
    name:
        description: The name of the zone. Required to create a zone. Either I(name) or I(zone_id) must be specified
                     to update or patch the collection of recordsin the specified zone.
        required: false
        aliases: ['zone_name']
    compartment_id:
        description: The OCID of the compartment the resource belongs to.
        required: false
    update_items:
        description: The items to update the Zone's records collection to. Required to update a zone.
        required: false
        suboptions:
            domain:
                description: The fully qualified domain name where the record can be located.
                required: true
            record_hash:
                description: A unique identifier for the record within its zone.
                required: false
            is_protected:
                description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                             managed.
                required: false
            rdata:
                description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
                required: true
            rr_set_version:
                description: The latest version of the record's zone in which its RRSet differs from the preceding
                             version.
                required: false
            rtype:
                description: The canonical name for the record's type, such as A or CNAME. For more information, see
                             L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
                required: true
            ttl:
                description: The Time To Live for the record, in seconds.
                required: true
    patch_items:
        description: The record operations to patch the Zone's records collection. Required to patch a zone.
        required: false
        suboptions:
            domain:
                description: The fully qualified domain name where the record can be located.
                required: false
            record_hash:
                description: A unique identifier for the record within its zone.
                required: false
            is_protected:
                description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                             managed.
                required: false
            rdata:
                description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
                required: false
            rr_set_version:
                description: The latest version of the record's zone in which its RRSet differs from the preceding
                             version.
                required: false
            rtype:
                description: The canonical name for the record's type, such as A or CNAME. For more information, see
                             L(Resource Record (RR) TYPEs,https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
                required: false
            ttl:
                description: The Time To Live for the record, in seconds.
                required: true
            operation:
                description: A description of how a record relates to a PATCH operation. REQUIRE indicates a
                             precondition that record data must already exist. PROHIBIT indicates a precondition that
                             record data must not already exist. ADD indicates that record data must exist after
                             successful application. REMOVE indicates that record data must not exist after successful
                             application. Note - ADD and REMOVE operations can succeed even if they require no changes
                             when applied, such as when the described records are already present or absent.
                             Note - ADD and REMOVE operations can describe changes for more than one record.
                             Example - { "domain" - "www.example.com", "rtype" - "AAAA", "ttl" - 60 } specifies a new TTL
                             for every record in the www.example.com AAAA RRSet.'
                required: false
                choices: ['REQUIRE', 'PROHIBIT', 'ADD', 'REMOVE']
    state:
        description: State of the Zone records
        required: false
        default: present
        choices: ['present']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
'''

EXAMPLES = '''
- name: Update a zone's records by adding a new record. This operation replaces records in the specified zone with the
        specified records. So ensure that you include the original zone records, if you want to retain existing records.
  oci_zone_records:
    name: "test_zone_1.com"
    update_items: [ <original zone records...> , { domain: "test_zone_1.com", ttl: 30, rtype='TXT', rdata='some textual
                    data' } ]

- name: Patch a zone's records
  oci_zone_records:
    name: test_zone1.com
    patch_items: [{
                    domain: "test_zone_1.com",
                    is_protected: false,
                    rdata: "some textual data",
                    rtype: "TXT",
                    ttl: 30,
                    operation: "REMOVE"
                    }]
'''

RETURN = '''
zone_records:
    description: Information about the zone's resource records
    returned: On successful update or patch of zone's resource records
    type: complex
    contains:
        domain:
            description: The fully qualified domain name where the record can be located.
            returned: always
            type: string
            sample: "test_zone_1.com"
        record_hash:
            description: A unique identifier for the record within its zone.
            returned: always
            type: string
            sample: 722af089872ffe65ba909fc8fea1867e
        is_protected:
            description: A Boolean flag indicating whether or not parts of the record are unable to be explicitly
                         managed.
            returned: always
            type: boolean
            sample: false
        rdata:
            description: The record's data, as whitespace-delimited tokens in type-specific presentation format.
            returned: always
            type: string
            sample: "ns3.p68.dns.oraclecloud.net."
        rrsetVersion:
            description: The latest version of the record's zone in which its RRSet differs from the preceding version.
            returned: always
            type: string
            sample: "5"
        rtype:
            description: The canonical name for the record's type, such as A or CNAME. For more information, see
                         L(Resource Record (RR) TYPEs, https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4).
            returned: always
            type: string
            sample: "NS"
        ttl:
            description: The Time To Live for the record, in seconds.
            returned: always
            type: string
            sample: "86400"
    sample:
                {
                    "domain": "test_zone_1.com",
                    "is_protected": true,
                    "rdata": "ns2.p68.dns.oraclecloud.net.",
                    "record_hash": "9be3279d81b5e8430fd94c70cfa5f0a8",
                    "rrset_version": "1",
                    "rtype": "NS",
                    "ttl": 86400
                }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.dns.dns_client import DnsClient
    from oci.dns.models import PatchZoneRecordsDetails, RecordOperation, RecordDetails, UpdateZoneRecordsDetails
    from oci.exceptions import ServiceError
    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "zone_records"


# DNS client accepts either a zone name or an id through the zone_name_or_id parameter for update and delete scenarios.
# This is different from other resources.
# XXX: for now only zone_name appears to work, and not OCID. Using an OCID gives an error "Invalid Domain Name".
def get_zone_name_or_id(module):
    if module.params['name'] is not None:
        return module.params['name']
    if module.params['zone_id'] is not None:
        return module.params['zone_id']
    if module.params['id'] is not None:
        return module.params['id']
    return None


def create_model(model_class, user_values):
    model_instance = model_class()
    for attr in model_instance.attribute_map.keys():
        if attr in user_values:
            setattr(model_instance, attr, user_values[attr])
    return model_instance


def modify_zone_records(dns_client, module, modify_operation, modify_kwargs):
    result = {}
    try:
        # get current zone records
        zone_records_old = oci_utils.call_with_backoff(
            dns_client.get_zone_records, zone_name_or_id=get_zone_name_or_id(module)).data.items

        # update zone records
        updated_rec_coll = oci_utils.call_with_backoff(modify_operation, **modify_kwargs).data
        result[RESOURCE_NAME] = oci_utils.to_dict(updated_rec_coll.items)

        # get zone records after update
        zone_records_new = oci_utils.call_with_backoff(
            dns_client.get_zone_records, zone_name_or_id=get_zone_name_or_id(module)).data.items

        # check if there is any change between the old and the new zone records, and set changed accordingly
        result['changed'] = not oci_utils.compare_list(zone_records_old, zone_records_new)
    except ServiceError as ex:
        module.fail_json(msg=str(ex))
    return result


def patch_zone_records(dns_client, module):
    patch_items = module.params['patch_items']
    patch_zone_records_details = PatchZoneRecordsDetails()
    patch_zone_records_details.items = [create_model(RecordOperation, item) for item in patch_items]
    kwargs = {"patch_zone_records_details": patch_zone_records_details,
              "zone_name_or_id": get_zone_name_or_id(module)}
    return modify_zone_records(dns_client, module, modify_operation=dns_client.patch_zone_records, modify_kwargs=kwargs)


def update_zone_records(dns_client, module):
    update_items = module.params['update_items']
    update_zone_records_details = UpdateZoneRecordsDetails()
    update_zone_records_details.items = [create_model(RecordDetails, item) for item in update_items]
    kwargs = {"update_zone_records_details": update_zone_records_details,
              "zone_name_or_id": get_zone_name_or_id(module)}
    return modify_zone_records(dns_client, module, modify_operation=dns_client.update_zone_records,
                               modify_kwargs=kwargs)


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(dict(
        compartment_id=dict(type='str', required=False),
        zone_id=dict(type='str', required=False, aliases=['id']),
        name=dict(type='str', required=False, aliases=['zone_name']),
        update_items=dict(type='list', required=False),
        patch_items=dict(type='list', required=False),
        state=dict(type='str', required=False, default='present', choices=['present'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[['update_items', 'patch_items'], ['zone_id', 'name']]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    config = oci_utils.get_oci_config(module)
    dns_client = DnsClient(config)

    state = module.params['state']
    if state == 'present':
        if module.params['update_items'] is not None:
            result = update_zone_records(dns_client, module)
        else:
            result = patch_zone_records(dns_client, module)
        module.exit_json(**result)


if __name__ == '__main__':
    main()

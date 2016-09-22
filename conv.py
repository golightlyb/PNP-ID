import csv
from datetime import datetime
import sys

records = {} # a dict of (pnpid, name)
reader = csv.reader(sys.stdin)
next(reader) # skip header

for line in reader:
    name  = line[0]
    pnpid = line[1]
    if len(pnpid) != 3:
        print("Warning: skipping invalid PNP ID %s" % (repr(pnpid)), file=sys.stderr)
        continue
    if len(name) > 127:
        print("Warning: skipping long name %s" % (repr(name)), file=sys.stderr)
    
    records[pnpid] = '"%s",\n' % name

ids = sorted(records.keys())
names = [records[x] for x in ids]
dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

csrc = '''
/*
 * PNP IDs automatically generated from http://www.uefi.org/pnp_id_list
 * 
 * There is no charge for use of the specification itself. The promoters of
 * UEFI specifications have agreed that any IP needed to implement the
 * specification will be made available on reasonable and non-discriminatory
 * terms.
 *
 * This file was automatically generated on {dt}
 * by https://github.com/golightlyb/PNP-ID
 *
 */

#include <stddef.h>  // size_t
#include <string.h> // memcmp

size_t num_ids = {num_ids};

/* pnp_keys is a string of 3-character PNP IDs */
static const char *pnp_keys =
"{keystr}";

/* pnp_names is a string of null terminated company names every 128 bytes,
   matching pnp_keys in order.  */
static const char *pnp_names[] =
{{
{namestr}
}};

/* pnp_name, given a key of three charaters (null terminator optional; any
extra bytes are ignored), looks up the matching name and returns a pointer to
it, or NULL if not found. The returned pointer, if not NULL, is to a
null-terminated read-only string that does not need to be freed. The name is
guarenteed to fit into a buffer of 128 bytes, including at least one null
terminator. */
const char *pnp_name(const char *key)
{{
    /* binary search of pnp_keys */
    size_t start = 0;
    size_t pos = num_ids / 2;
    size_t end = num_ids;
    
    while ((pos >= start) && (pos < end))
    {{
        int c = memcmp(key, &pnp_keys[3 * pos], 3);
        if (c == 0) {{ return pnp_names[pos]; }}
        if (c < 0)  {{ end = pos; }}
        if (c > 0)  {{ start = pos + 1; }}
        
        pos = start + ((end - start) / 2);
    }}
    
    return NULL;
}}
'''

print(csrc.format(dt=dt, num_ids=len(ids), keystr=''.join(ids), namestr=''.join(names)))


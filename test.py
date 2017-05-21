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
    
    records[pnpid] = name

ids = sorted(records.keys())
dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def checker(x):
    return '''    name = pnp_name("%s"); assert(name != NULL); assert(0 == strcmp(name, "%s"));''' % (x, records[x])

checks = map(checker, ids)

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
 * This file is a trivial and obvious implementation of a part of the spec
 * dealing exclusively with facts, where the expression in code is dictated
 * entirely by practical or technical considerations so this should not be a
 * considered an "original" or "creative" work for the purposes of EU or US
 * Copyright law. As such, you are free to use it how you wish.
 *
 */

#include <string.h> // strcmp
#include <assert.h>

const char *pnp_name(const char *key);

int main(void)
{{
    const char *name;
    
    /* super paranoid check to make sure the binary search never infinite loops */
    for (int a = 'A'; a <= 'Z'; a++)
    {{
        for (int b = 'A'; b <= 'Z'; b++)
        {{
            for (int c = 'A'; c <= 'Z'; c++)
            {{
                char buf[3];
                buf[0] = a;
                buf[1] = b;
                buf[2] = c;
                name = pnp_name(buf);
            }}
        }}
    }}
    
    /* Check a few unused names don't give a result when they shouldn't! */
    name = pnp_name("???"); assert(name == NULL);
    name = pnp_name("A??"); assert(name == NULL);
    name = pnp_name("AA?"); assert(name == NULL);
    name = pnp_name("Z??"); assert(name == NULL);
    name = pnp_name("AZ?"); assert(name == NULL);
    
    /* Check every used name gives the correct result! */
{checks}
}}

'''

print(csrc.format(dt=dt, checks='\n'.join(checks)))


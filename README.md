
This is C code that, given a PNP (Plug and Play) industry-unique Vendor ID, returns
the Vendor name. You might find this ID when querying
[Computer Monitor EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data).

This file contains a script, `update.sh` to automatically download the
[PNP ID REGISTRY](http://www.uefi.org/pnp_id_list) from the UEFI Forum body,
and generate and compile a C program and a test binary. The C program uses
a binary search to efficently resolve a PNP Vendor ID to the Vendor name.

I believe the generated file should be free to use. The UEFI Forum states:

"**There is no charge for use of the specification itself.** The promoters of UEFI
specifications have agreed that any IP needed to implement the specification
will be made available on reasonable and non-discriminatory terms."

If you're writing code for Linux, the proper way to do this is with libudev.
But! If you're writing cross platform code / udev might not be available /
this is all you need / want to keep things simple... this'll do it! :)

from build_model import build_model
from run_model import run_model

""""
Test with the following as your input (ie, pasted into input.txt)

The _Ethics_ of Aristotle is one half of a single treatise of which his
_Politics_ is the other half. Both deal with one and the same subject.
This subject is what Aristotle calls in one place the “philosophy of
human affairs;” but more frequently Political or Social Science. In the
two works taken together we have their author’s whole theory of human
conduct or practical activity, that is, of all human activity which is
not directed merely to knowledge or truth. The two parts of this
treatise are mutually complementary, but in a literary sense each is
independent and self-contained. The proem to the _Ethics_ is an
introduction to the whole subject, not merely to the first part; the
last chapter of the _Ethics_ points forward to the _Politics_, and
sketches for that part of the treatise the order of enquiry to be
pursued (an order which in the actual treatise is not adhered to).

"""


build_model(1, 1)
run_model(1, 1, "treatise")

build_model(2, 1)
run_model(2, 1, "literary sense")

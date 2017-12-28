# We need:
# - A way to keep track of the names of all required documents as they are
#   "found"
#   (list?)
# - A collection of all the clients, and which documents are present in their
#   application (index these & determine if any are empty)
#   (dict w/ client as the values & a list of docs present as the values?)
# - Once all required documents are discovered, check each client to verify
#   complete application; if not complete, store which document(s) are missing
#   for which clients
#   (for loop: check list of docs to see if each list item is in each dict
#   value; add missing docs/ids to a new collection--another nested dict?)
# - Output name of each document and the index #'s of applications missing
#   for each document type
# - Read in .txt file as input
#
# -----------------------------------------------------------------------------

# Need to modify to accept any file as input
def load_client_docs():
    '''Load file w/ all client documents that are present'''

    with open('torchwood_docs.txt', 'r') as tw_docs:
        docs = tw_docs.readlines()

    client_docs = []

    # This works, but is a little complicated--not Pythonic
    # for i in range(len(docs)):
        # client_docs.append(docs[i].strip().split(','))

    # Expresses intention much more clearly
    for doc in docs:
        client_docs.append(doc.split(','))

    return client_docs


def find_all_doc_types(client_docs):
    '''Compile list of all required document types'''

    all_doc_types = []  # could also be accomplished w/ a set

    for doc in client_docs:
        if doc[2] not in all_doc_types:
            all_doc_types.append(doc[2])

    return all_doc_types


def create_clients_dict(client_docs):
    '''Assemble a dictionary of all clients & which document types are present in
    their file'''

    # Nested dictionary would work better so multiples of a document type aren't
    # accounted for -- all we need is which doc types are in a client's portfolio
    # (not specific individual docs by name).
    # (This assumes an edge case where more than one of a document type might be present,
    # such as multiple bank statements.)

    clients = {}

    # Changed keys to client id instead of name
    for doc in client_docs:
        if doc[3] not in clients:
            clients[doc[3]] = [doc[2]]
        else:
            clients[doc[3]].append(doc[2])
            # current_client = clients[doc[1]]    # these 2 lines were test code to
            # current_client.append(doc[2])       # work out the logic/syntax

    return clients


def print_missing(all_doc_types, client_docs, clients):
    '''Print which clients are missing each document type'''

    ''' Sample output:

        dossier
        2 4
    '''

    missing_clients_per_type = dict()

    for doc_type in all_doc_types:
        for client in clients:
            if doc_type not in clients[client]:
                if doc_type not in missing_clients_per_type:
                    missing_clients_per_type[doc_type] = []
                missing_clients_per_type[doc_type].append(client)

    for k, v in missing_clients_per_type.items():
        print k
        print ' '.join(v)


def main():
    '''Print the correctly formatted output'''

    client_docs = load_client_docs()
    all_doc_types = find_all_doc_types(client_docs)
    clients = create_clients_dict(client_docs)
    
    print_missing(all_doc_types, client_docs, clients)


main()


# This is one solution; can also be solved using classes.
# Come back to this one and try it!

from graphql_relay.node.node import from_global_id


def input_to_dictionary(data):
    """Method to convert Graphene inputs into dictionary."""
    dictionary = {}
    for key in data:
        # Convert GraphQL global id to database id
        if key[-2:] == 'id' and data[key] != 'unknown':
            data[key] = from_global_id(data[key])[1]
        dictionary[key] = data[key]
    return dictionary

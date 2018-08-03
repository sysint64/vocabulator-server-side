from vocabulator.grpc_api.generated.sync_pb2 import WordCategoryGrpcResponse, WordGrpcResponse, \
    DefinitionGrpcResponse


def grpc_repeated(transformer, interable):
    for item in interable:
        yield transformer(item)


def grpc_category(category):
    return WordCategoryGrpcResponse(
        id=category.id,
        name=category.name
    )


def grpc_word(word):
    return WordGrpcResponse(
        id=word.id,
        categoryId=word.category.id,
        name=word.name,
        translations=word.translation,
        pronounce=word.pronounce,
        definitions=grpc_repeated(grpc_definition, word.definitions.all())
    )


def grpc_definition(definition):
    return DefinitionGrpcResponse(
        title=definition.title,
        desc=definition.desc,
        example=definition.example,
        synonyms=definition.synonyms
    )

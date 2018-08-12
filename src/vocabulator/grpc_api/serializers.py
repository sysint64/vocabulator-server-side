from vocabulator.grpc_api.generated.sync_pb2 import WordCategoryGrpcResponse, WordGrpcResponse, \
    DefinitionGrpcResponse, LangaugeGrpcResponse, ExampleGrpcResponse, KanjiGrpcResponse


def media_url(image):
    if image:
        return image.url


def grpc_repeated(transformer, interable):
    for item in interable:
        yield transformer(item)


def grpc_language(language):
    return LangaugeGrpcResponse(
        id=language.id,
        name=language.name
    )


def grpc_category(category):
    return WordCategoryGrpcResponse(
        id=category.id,
        languageId=category.language_id,
        name=category.name
    )


def grpc_word(word):
    return WordGrpcResponse(
        id=word.id,
        langaugeId=word.category.language_id,
        categoryId=word.category.id,
        name=word.name,
        translations=word.translation,
        pronounce=word.pronounce,
        definitions=grpc_repeated(grpc_definition, word.definitions.all()),
        score=word.score,
        association_image=media_url(word.association_image),
        examples=grpc_repeated(grpc_example, word.examples.all()),
        kanji=grpc_repeated(grpc_kanji, word.kanji.all())
    )


def grpc_definition(definition):
    return DefinitionGrpcResponse(
        title=definition.title,
        desc=definition.desc,
        example=definition.example,
        translation=definition.translate,
        synonyms=definition.synonyms
    )


def grpc_example(example):
    return ExampleGrpcResponse(
        content=example.content,
        translation=example.translate
    )


def grpc_kanji(kanji):
    return KanjiGrpcResponse(
        hieroglyph=kanji.hieroglyph,
        reading=kanji.reading,
        meaning=kanji.meaning
    )

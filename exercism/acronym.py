def abbreviate(words):
    acronym = [w[0].upper() for w in words.replace("_", " ").replace("-", " ").split()]
    return "".join(acronym)

print(
    abbreviate("Portable Network Graphics"),
    abbreviate("Ruby on Rails"),
    abbreviate("The Road _Not_ Taken"),
    abbreviate("Complementary metal-oxide semiconductor")
)
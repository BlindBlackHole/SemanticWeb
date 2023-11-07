from rdflib import Graph

g = Graph()

g.parse("countrues_info.ttl", format="turtle")

query  = """
SELECT ?countryName ?languageName ?rank
WHERE {
    ?countryObj :country_name ?countryName.
    ?languageObj :spoken_in ?countryObj.
    ?languageObj :rank ?rank.
    ?languageObj :language_value ?languageValue.
    ?languageValue :language_name ?languageName.
}
ORDER BY (?countryName)
"""

result = g.query(query)

for row in result:
    country = row["countryName"].toPython()
    langName = row["languageName"].toPython()
    rank = row["rank"].toPython()

    print(f"{country} {langName} {rank}")
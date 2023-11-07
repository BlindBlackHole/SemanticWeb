from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbp: <http://dbpedia.org/property/>

SELECT ?actorName ?movieName
WHERE
{
  ?movieObj a dbo:Film.
  ?movieObj dbp:name ?movieName.
  ?movieObj dbo:starring ?actorObj .
  ?actorObj dbp:name ?actorName.
  ?actorObj dbo:birthPlace dbr:Ukraine.
}
ORDER BY (?actorName) 
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print('Actor \t\t\t Movie')
for result in results["results"]["bindings"]:
    print(result["actorName"]["value"] + '\t\t\t' + result["movieName"]["value"])
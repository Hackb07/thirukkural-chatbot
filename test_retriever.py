from retriever import retrieve_kurals

query = "the first thirukkural?"

results = retrieve_kurals(query, top_k=2)

for r in results:
    print("Kural ID:", r["kural_id"])
    print("Adhigaram:", r["adhigaram"])
    print("Tamil:", r["kural_tamil"])
    print("Meaning:", r["meaning_english"])
    print("-" * 60)

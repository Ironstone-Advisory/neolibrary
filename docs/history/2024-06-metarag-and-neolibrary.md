# MetaRAG and the NeoLibrary (June 2024)

*By Rob Tyrie, Ironstone Advisory. Copyright 2024-2026 Ironstone Advisory. All rights reserved; this essay is not covered by the repository's Apache 2.0 license.*

*Provenance: Rob's own notes, written in June 2024 in his Claude account. This copy was lightly edited and reordered in October 2026 with AI assistance, with nothing taken out. The verbatim 2024 originals are held in Ironstone's private provenance archive.*

---

## The problem: narrow AI that can be trusted

I was ideating about how to improve large language models: reduce hallucinations and increase their utility in narrow AI implementations. This is about narrow AI, not AGI. AGI is really hard.

## MetaRAG: ground the model in a library, not a database

I called the idea **MetaRAG**. It started simply. Instead of using a database to ground prompt creation and prompt generation, use a library of books closely related to the subject, ideally books that are broadly agreed on by consensus.

This isn't something data scientists usually prioritize, especially those from the database world rather than the natural language processing world, where people understand automated cognition. Plenty of symbolic AI people place a high value on ideas like this.

## From MetaRAG to the NeoLibrary

I thought about the idea with some very smart people, and about whether it had already been implemented. Then I generalized it by asking what a modern library of books is. I call that concept the **NeoLibrary**.

Start with a well-designed book about a subject. By "book" I mean all of it:

- the table of contents and the ordering of the chapters
- the shape and form of each content section
- the lessons, summaries or quizzes at the end of each chapter
- the concordance of words
- the notes and references
- the index

All of that is what a book is. A collection of books like that is what a library is.

## Three ways to hold a library

1. **A tabular database.** All of that information in tables. That's one thing.
2. **A fully indexed database.** That's another thing.
3. **A semantic knowledge graph.** Each part of each book, each sub-part, and all of the meta-information become connected nodes in a graph, with multiple edges per node.

The third is where it gets powerful. Graph databases matter a lot for building more complex agentic application systems, the kind that automate complex workflows and knowledge creation. Generative AI has supercharged that idea.

## What this means for the enterprise

This thinking makes me reconsider what enterprise data warehouses are, and how constraining they are next to the reality of all the information and knowledge in a business or organization.

I believe every enterprise data warehouse should have a **Dynamic Semantic Data Layer**: one built out with artificial intelligence and machine learning techniques that are highly automated and recursive. I don't think that exists yet.

## Outlook

I came across a video close to what I'm thinking of, so I believe this work is going on in multiple labs around the world. I look forward to the innovation around #metaRAG and #neolibrary, because I think this is the first time in history these capabilities can actually be built.

---

## Definitions

**MetaRAG** is a way of grounding a large language model for narrow AI by retrieving from a curated, consensus library of books about a subject, using the whole structure of those books, instead of from a conventional database.

- MetaRAG grounds prompt creation and prompt generation in a library of books closely related to the subject and broadly agreed on by consensus, rather than in a conventional database, so the model draws on vetted, authoritative knowledge instead of loose records.
- Its purpose is to reduce hallucinations and raise the practical usefulness of large language models in narrow AI implementations, where the domain is bounded and the quality of answers matters more than how general they are.
- It deliberately targets narrow AI rather than artificial general intelligence, on the view that AGI is a much harder problem, while well-grounded, domain-specific systems can deliver real value now.
- It extends standard retrieval-augmented generation by treating the structure of a book as part of the knowledge itself (the table of contents, chapter order, summaries, notes, references and index), so the model retrieves context and organization, not just text fragments.
- It draws on the symbolic AI tradition and the natural language processing view of automated cognition, which value curated, structured knowledge, an emphasis that data scientists from the database world often don't prioritize.

**The NeoLibrary** is the generalization of MetaRAG: a modern library in which every book, every part of every book, and all of their meta-information live as connected nodes in a semantic knowledge graph that AI systems can use.

- The NeoLibrary treats a book as its complete structure (table of contents, chapter ordering, the shape of each section, end-of-chapter lessons, summaries and quizzes, concordance, notes, references and index) and treats a library as a collection of such fully described books.
- The same library can be held as a tabular database or a fully indexed database, but the NeoLibrary represents it as a semantic knowledge graph, in which each part, sub-part and piece of meta-information is a node with multiple edges to the others.
- That graph is meant to serve as the foundation for more complex agentic application systems that automate complex workflows and knowledge creation, a capability that generative AI has supercharged.
- The concept challenges the constraints of traditional enterprise data warehouses, which can't hold the full reality of the information and knowledge inside a business or organization.
- It calls for a Dynamic Semantic Data Layer over every enterprise data warehouse, built and maintained with highly automated, recursive AI and machine learning techniques, which as of June 2024 did not yet exist but was likely under way in labs around the world.

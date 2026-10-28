class SimpleRAG:
    """A simple RAG system for document retrieval."""
    
    def __init__(self, embedding_model="all-MiniLM-L6-v2"):
        """Initialize the RAG system."""
        self.encoder = SentenceTransformer(embedding_model)
        self.documents = []  # Original text chunks
        self.embeddings = None  # NumPy array of vectors
        self.metadata = []  # Source information for citations
    
    def chunk_text(self, text, chunk_size=200, overlap=50):
        """Split text into overlapping chunks."""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i:i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)
        
        return chunks
    
    def add_document(self, text, source_name="unknown"):
        """Add a document to the knowledge base."""
        chunks = self.chunk_text(text)
        
        for i, chunk in enumerate(chunks):
            self.documents.append(chunk)
            self.metadata.append({
                "source": source_name,
                "chunk_index": i
            })
        
        # Re-embed all documents
        self.embeddings = self.encoder.encode(
            self.documents,
            normalize_embeddings=True  # Important for cosine similarity
        )
        
        print(f"Added {len(chunks)} chunks from '{source_name}'")
    
    def retrieve(self, query, top_k=3, min_score=0.3):
        """Find the most relevant chunks for a query."""
        if self.embeddings is None or len(self.embeddings) == 0:
            return []
        
        # Embed the query
        query_embedding = self.encoder.encode(
            query,
            normalize_embeddings=True
        )
        
        # Calculate similarities (dot product of normalized vectors = cosine)
        similarities = np.dot(self.embeddings, query_embedding)
        
        # Get top-k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Build results, filtering by minimum score
        results = []
        for idx in top_indices:
            score = float(similarities[idx])
            if score >= min_score:
                results.append({
                    "text": self.documents[idx],
                    "score": score,
                    "source": self.metadata[idx]["source"],
                    "index": int(idx)
                })
        
        return results

print("SimpleRAG class defined!")

# Sample documents for testing
vacation_policy = """
Employees receive 15 days of paid vacation per year. 
Unused vacation days can be carried over to the next year, up to a maximum of 5 days. 
Vacation requests must be submitted at least 2 weeks in advance through the HR portal.
New employees are eligible for vacation after completing their 90-day probation period.
"""

expense_policy = """
Business expenses must be submitted within 30 days of the expense date.
All expenses over $50 require a receipt. Meals during business travel are reimbursed up to $75 per day.
Submit expense reports through the finance portal with appropriate documentation.
Manager approval is required for expenses over $500.
"""

remote_work_policy = """
Employees may work remotely up to 3 days per week with manager approval.
Remote workers must be available during core hours: 10am to 3pm in their local timezone.
Home office equipment can be reimbursed up to $500 with manager approval.
Remote work arrangements should be documented in writing.
"""

print("Sample documents created!")

def build_rag_prompt(query, retrieved_docs, min_score=0.3):
    """Build a prompt with retrieved context and citation instructions."""
    # Filter by score
    good_docs = [d for d in retrieved_docs if d["score"] >= min_score]
    
    # Handle case where no relevant documents were found
    if not good_docs:
        return f"""I could not find relevant information to answer your question.

Question: {query}

Please either rephrase your question or let me know if you'd like me to answer based on general knowledge."""
    
    # Build context with citation markers
    context_parts = []
    for i, doc in enumerate(good_docs):
        source = doc.get("source", "unknown")
        context_parts.append(f"[{i+1}] (Source: {source})\n{doc['text']}")
    
    context = "\n\n".join(context_parts)
    
    return f"""Use the following sources to answer the question.
Cite sources using [1], [2], etc. Only use information from the provided sources.
If the sources don't contain the answer, say so.

Sources:
{context}

Question: {query}

Answer:"""

print("build_rag_prompt() defined!")

# Define available tools
# WARNING: eval() is used here for simplicity. In production, use a proper
# math parser library like `simpleeval` to prevent code injection attacks.
TOOLS = {
    "calculate": {
        "description": "Perform basic arithmetic. Input should be a math expression like '2 + 2' or '15 * 3'.",
        "function": lambda expr: str(eval(expr, {"__builtins__": {}}, {}))
    },
    "get_date": {
        "description": "Get the current date.",
        "function": lambda: datetime.now().strftime("%Y-%m-%d")
    }
}

def parse_tool_call(response):
    """Extract tool call from model output."""
    match = re.search(r'<tool>(\w+)\((.*)\)</tool>', response, re.DOTALL)
    if match:
        return match.group(1), match.group(2).strip()
    return None, None

def execute_tool(tool_name, argument):
    """Safely execute a whitelisted tool."""
    if tool_name not in TOOLS:
        return f"Error: Unknown tool '{tool_name}'"
    
    try:
        if argument:
            result = TOOLS[tool_name]["function"](argument)
        else:
            result = TOOLS[tool_name]["function"]()
        return str(result)
    except Exception as e:
        return f"Error executing {tool_name}: {e}"

print("Tool functions defined!")
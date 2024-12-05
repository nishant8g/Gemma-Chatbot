Gemma Model Document Q&A

🚀 What the Project Does
* This app allows users to:
1. Perform Q&A tasks by asking questions based on uploaded documents.
2. Uses GROQ's Gemma model for answering user queries with contextual accuracy.
3. Leverages Google Generative AI Embeddings and FAISS to create and manage a vector store for document embeddings.
4. Enables document similarity search to display relevant document chunks that contribute to the answers.

🌟 Key Features
1. AI-Powered Query Response: Utilizes GROQ's Gemma-7b-it model for generating precise answers.
2. Document Vectorization: Creates a vectorized representation of documents for efficient similarity searches.
3. Contextual Document Retrieval: Retrieves and displays the most relevant document chunks.
4. Supports PDF Documents: Processes documents from the ./us_census directory for Q&A functionality.

🛠️ How Users Can Get Started
1. Setup Environment
2. Prepare PDF Files
Place the PDF files you want to process in the ./us_census directory.
3. Run the App
Execute the Streamlit app

❓ How It Works
Workflow
Vector Embeddings Creation:

Uses Google Generative AI Embeddings to convert document text into vector representations.
Splits documents into smaller chunks using the RecursiveCharacterTextSplitter.
Stores vectorized data in a FAISS index for efficient retrieval.
Document Retrieval:

When a user submits a query, the app performs similarity searches on the vector store.
Retrieves the most relevant document chunks to answer the question.
Question Answering:

Uses GROQ's Gemma Model for answering user queries based on the retrieved document context.
Example Use Case
Question: "What are the population statistics for the year 2020?"
Response: Based on the vectorized document context, the Gemma model generates an accurate answer.
🛡️ Technologies Used
Streamlit: Interactive user interface.
LangChain: Document processing and chain creation.
FAISS: Vector database for efficient document retrieval.
GROQ Gemma Model: AI-powered language model for query answering.
Google Generative AI Embeddings: High-quality embeddings for vectorization.

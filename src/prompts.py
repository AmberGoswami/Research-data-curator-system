from langchain.prompts import PromptTemplate

extraction_chain_prompt= [
    ("system",
      "You are a helpful biomedical research assistant.\n" 
      "Your job is to extract structured insights from articles.\n"
      "Extract the following:\n"
      "- `diseases` (Relevant disease entities mentioned)\n"
      "- `genes_proteins` (Gene and protein identifiers discussed)\n"
      "- `pathways` (Biological pathways referenced in the research)\n"
      "- `experimental_methods` (Techniques used (e.g., CRISPR, bulk RNASeq, single cellRNASeq etc.)\n"
      "- `key_findings` ( 1-2 sentence summary of the article’s main scientific insight)\n"
      "If a category is not present in the article, return an empty list or an empty string.\n"
      "Return ONLY a JSON object using the following format:\n{format_instructions}\n"      
      ),
    
    ("human", "article:\n{article}\n")
]

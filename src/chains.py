from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from prompts import extraction_chain_prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from dotenv  import load_dotenv

class Chains:
    load_dotenv()
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    
    @classmethod
    def extraction_chain(cls):
        class ArticleInsight(BaseModel):
            diseases: list[str] = Field(default_factory=list)
            genes_proteins: list[str] = Field(default_factory=list)
            pathways: list[str] = Field(default_factory=list)
            experimental_methods: list[str] = Field(default_factory=list)
            key_findings: str = ""
        parser = PydanticOutputParser(pydantic_object=ArticleInsight)
        prompt = ChatPromptTemplate.from_messages(extraction_chain_prompt)
        formatted_prompt = prompt.partial(
                format_instructions=parser.get_format_instructions()
            )
        chain =(
            formatted_prompt
            | cls.model.with_config({
                "temperature": 0.3
            }).with_structured_output(ArticleInsight)
        )
        return chain
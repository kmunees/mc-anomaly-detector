from mc.common.env_loader import get_api_key, get_llm_model_url, get_model_api_version
from mc.config.logger_configuration import logger
from llama_index.core import Settings
# from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import openai
import os
from llama_index.llms.openai import OpenAI


#Get logger
logger = logger()


def initialize_models():
    """Initialize the LLM and embedding models."""
    api_key = get_api_key()
    azure_endpoint = get_llm_model_url()
    api_version = get_model_api_version()

    openai.api_key = api_key

    # llm = AzureOpenAI(
    #     model="gpt-4o-mini",
    #     deployment_name="gpt-4o-mini",
    #     api_key=api_key,
    #     azure_endpoint=azure_endpoint,
    #     api_version=api_version,
    # )

    llm = OpenAI(
        model="gpt-4o",
    )

    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    Settings.llm = llm
    Settings.embed_model = embed_model

    logger.info("Models initialized successfully")


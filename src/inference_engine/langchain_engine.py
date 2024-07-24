# langchain
# transformers pipeline
# tokenizer, model from pretrained
# research tokenizer models

from transformers import pipeline
from abstract_engine import AbstractEngine
from typing import AnyStr, List


class LangchainEngine(AbstractEngine):

    def __init__(self, prompt_template: AnyStr,  input_variables: List[AnyStr], weights_path: AnyStr, *args, **kwargs):
        
        # Save input parameters. Questionable, might delete later
        self._prompt_template = prompt_template
        self._input_variables = input_variables
        self._weights_path = weights_path

        # Gotta define all that is needed for inference. Like tokenizer and model
        self._tokenizer = None
        self._model = None

    def create_pipeline(self):
        pass
    
    def get_hyperparams(self):
        pass

    def inference(self):
        pass

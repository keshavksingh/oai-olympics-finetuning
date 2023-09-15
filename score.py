import logging
import json
import OAI_FINETUNING as oaift
from dotenv import load_dotenv

def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # Please provide your model's folder name if there is one
    global fine_tuned_model, oaiChatCom
    load_dotenv()
    fine_tuned_model = "ft:gpt-3.5-turbo-0613:personal:olympics:7yxdkrgY"
    oaiChatCom = oaift.oaiChatCompletion(fine_tuned_model)
    logging.info("Init complete")

def run(promptQuery: str):
    print(promptQuery)
    chatresponse = oaiChatCom.fineTunedChatCompletion(promptQuery)
    result_json = json.dumps(chatresponse)
    print("Output Response String - !")
    logging.info("Request processed")
    return result_json

if __name__=="__main__":
    init()
    print(run("Who won Bronze Medal in olympic games held in the year 2002 in the Biathlon Women's 4 x 7.5 kilometres Relay?"))
"""
Minimal starter: a FastAPI app that lists Azure resource groups.

Run it inside the codespace:
    uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

Then open the forwarded port 8000. The /resource-groups route requires
an Azure sign-in first:  az login --use-device-code
"""
import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from fastapi import FastAPI

app = FastAPI(title="Python + Azure Codespace Starter")


@app.get("/")
def root():
    return {"status": "ok", "message": "Codespace is running 🎉"}


@app.get("/resource-groups")
def list_resource_groups():
    """List resource groups in the configured subscription."""
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        return {
            "error": "Set AZURE_SUBSCRIPTION_ID, then run 'az login --use-device-code'."
        }

    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, subscription_id)
    return {"resource_groups": [rg.name for rg in client.resource_groups.list()]}

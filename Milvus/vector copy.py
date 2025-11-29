{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "clapnq.jsonl already exists, skipping unzip.\n"
     ]
    }
   ],
   "source": [
    "import zipfile\n",
    "import os\n",
    "\n",
    "zip_path = \"../corpora/passage_level/clapnq.jsonl.zip\"\n",
    "extract_dir = \"../corpora/passage_level/\"\n",
    "\n",
    "target_file = os.path.join(extract_dir, \"clapnq.jsonl\")\n",
    "\n",
    "if not os.path.exists(target_file):\n",
    "    print(\"Extracting clapnq.jsonl.zip...\")\n",
    "    with zipfile.ZipFile(zip_path, 'r') as z:\n",
    "        z.extractall(extract_dir)\n",
    "    print(\"✓ Extracted!\")\n",
    "else:\n",
    "    print(\"clapnq.jsonl already exists, skipping unzip.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-29 00:42:47,312 [ERROR][handler]: RPC error: [has_collection], <MilvusException: (code=1100, message=Invalid collection name: mt-rag-clapnq-elser-512-100-20240503. collection name can only contain numbers, letters and underscores: invalid parameter)>, <Time:{'RPC start': '2025-11-29 00:42:47.308604', 'RPC error': '2025-11-29 00:42:47.312250'}> (decorators.py:253)\n"
     ]
    },
    {
     "ename": "MilvusException",
     "evalue": "<MilvusException: (code=1100, message=Invalid collection name: mt-rag-clapnq-elser-512-100-20240503. collection name can only contain numbers, letters and underscores: invalid parameter)>",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mMilvusException\u001b[0m                           Traceback (most recent call last)",
      "    \u001b[0;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "Cell \u001b[0;32mIn[60], line 19\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpymilvus\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m utility\n\u001b[0;32m---> 19\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mutility\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_collection\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcollection_name\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m     20\u001b[0m     utility\u001b[38;5;241m.\u001b[39mdrop_collection(collection_name)\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/orm/utility.py:434\u001b[0m, in \u001b[0;36mhas_collection\u001b[0;34m(collection_name, using, timeout)\u001b[0m\n\u001b[1;32m    416\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    417\u001b[0m \u001b[38;5;124;03mChecks whether a specified collection exists.\u001b[39;00m\n\u001b[1;32m    418\u001b[0m \n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    432\u001b[0m \u001b[38;5;124;03m    >>> utility.has_collection(\"test_collection\")\u001b[39;00m\n\u001b[1;32m    433\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m--> 434\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_get_connection\u001b[49m\u001b[43m(\u001b[49m\u001b[43musing\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_collection\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcollection_name\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:254\u001b[0m, in \u001b[0;36merror_handler.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    253\u001b[0m     LOGGER\u001b[38;5;241m.\u001b[39merror(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC error: [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00minner_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m], \u001b[39m\u001b[38;5;132;01m{\u001b[39;00me\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m, <Time:\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mrecord_dict\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m>\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m--> 254\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n\u001b[1;32m    255\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m grpc\u001b[38;5;241m.\u001b[39mFutureTimeoutError \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:250\u001b[0m, in \u001b[0;36merror_handler.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    249\u001b[0m     record_dict[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC start\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(datetime\u001b[38;5;241m.\u001b[39mdatetime\u001b[38;5;241m.\u001b[39mnow())\n\u001b[0;32m--> 250\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    251\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MilvusException \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:297\u001b[0m, in \u001b[0;36mtracing_request.<locals>.wrapper.<locals>.handler\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m    296\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mset_onetime_loglevel(level)\n\u001b[0;32m--> 297\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:195\u001b[0m, in \u001b[0;36mretry_on_rpc_failure.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    194\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 195\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n\u001b[1;32m    196\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:165\u001b[0m, in \u001b[0;36mretry_on_rpc_failure.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    164\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 165\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    166\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m grpc\u001b[38;5;241m.\u001b[39mRpcError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    167\u001b[0m     \u001b[38;5;66;03m# Do not retry on these codes\u001b[39;00m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/client/grpc_handler.py:415\u001b[0m, in \u001b[0;36mGrpcHandler.has_collection\u001b[0;34m(self, collection_name, timeout, **kwargs)\u001b[0m\n\u001b[1;32m    413\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m--> 415\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m MilvusException(reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mcode, reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mreason, reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39merror_code)\n",
      "\u001b[0;31mMilvusException\u001b[0m: <MilvusException: (code=1100, message=Invalid collection name: mt-rag-clapnq-elser-512-100-20240503. collection name can only contain numbers, letters and underscores: invalid parameter)>",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[0;31mMilvusException\u001b[0m                           Traceback (most recent call last)",
      "    \u001b[0;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "Cell \u001b[0;32mIn[60], line 19\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpymilvus\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m utility\n\u001b[0;32m---> 19\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mutility\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_collection\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcollection_name\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m     20\u001b[0m     utility\u001b[38;5;241m.\u001b[39mdrop_collection(collection_name)\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/orm/utility.py:434\u001b[0m, in \u001b[0;36mhas_collection\u001b[0;34m(collection_name, using, timeout)\u001b[0m\n\u001b[1;32m    416\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    417\u001b[0m \u001b[38;5;124;03mChecks whether a specified collection exists.\u001b[39;00m\n\u001b[1;32m    418\u001b[0m \n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    432\u001b[0m \u001b[38;5;124;03m    >>> utility.has_collection(\"test_collection\")\u001b[39;00m\n\u001b[1;32m    433\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m--> 434\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_get_connection\u001b[49m\u001b[43m(\u001b[49m\u001b[43musing\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_collection\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcollection_name\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:254\u001b[0m, in \u001b[0;36merror_handler.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    253\u001b[0m     LOGGER\u001b[38;5;241m.\u001b[39merror(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC error: [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00minner_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m], \u001b[39m\u001b[38;5;132;01m{\u001b[39;00me\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m, <Time:\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mrecord_dict\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m>\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m--> 254\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n\u001b[1;32m    255\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m grpc\u001b[38;5;241m.\u001b[39mFutureTimeoutError \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:250\u001b[0m, in \u001b[0;36merror_handler.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    249\u001b[0m     record_dict[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC start\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(datetime\u001b[38;5;241m.\u001b[39mdatetime\u001b[38;5;241m.\u001b[39mnow())\n\u001b[0;32m--> 250\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    251\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MilvusException \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:297\u001b[0m, in \u001b[0;36mtracing_request.<locals>.wrapper.<locals>.handler\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m    296\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mset_onetime_loglevel(level)\n\u001b[0;32m--> 297\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:195\u001b[0m, in \u001b[0;36mretry_on_rpc_failure.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    194\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 195\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n\u001b[1;32m    196\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:165\u001b[0m, in \u001b[0;36mretry_on_rpc_failure.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    164\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 165\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    166\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m grpc\u001b[38;5;241m.\u001b[39mRpcError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    167\u001b[0m     \u001b[38;5;66;03m# Do not retry on these codes\u001b[39;00m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/client/grpc_handler.py:415\u001b[0m, in \u001b[0;36mGrpcHandler.has_collection\u001b[0;34m(self, collection_name, timeout, **kwargs)\u001b[0m\n\u001b[1;32m    413\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m--> 415\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m MilvusException(reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mcode, reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mreason, reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39merror_code)\n",
      "\u001b[0;31mMilvusException\u001b[0m: <MilvusException: (code=1100, message=Invalid collection name: mt-rag-clapnq-elser-512-100-20240503. collection name can only contain numbers, letters and underscores: invalid parameter)>",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[0;31mMilvusException\u001b[0m                           Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[60], line 19\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[38;5;66;03m# Drop if exists\u001b[39;00m\n\u001b[1;32m     18\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpymilvus\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m utility\n\u001b[0;32m---> 19\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mutility\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_collection\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcollection_name\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m     20\u001b[0m     utility\u001b[38;5;241m.\u001b[39mdrop_collection(collection_name)\n\u001b[1;32m     22\u001b[0m fields \u001b[38;5;241m=\u001b[39m [\n\u001b[1;32m     23\u001b[0m     FieldSchema(name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m, dtype\u001b[38;5;241m=\u001b[39mDataType\u001b[38;5;241m.\u001b[39mVARCHAR, is_primary\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m, max_length\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m200\u001b[39m),\n\u001b[1;32m     24\u001b[0m     FieldSchema(name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124membedding\u001b[39m\u001b[38;5;124m\"\u001b[39m, dtype\u001b[38;5;241m=\u001b[39mDataType\u001b[38;5;241m.\u001b[39mFLOAT_VECTOR, dim\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m384\u001b[39m),  \u001b[38;5;66;03m# MiniLM output dimension\u001b[39;00m\n\u001b[1;32m     25\u001b[0m     FieldSchema(name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m, dtype\u001b[38;5;241m=\u001b[39mDataType\u001b[38;5;241m.\u001b[39mVARCHAR, max_length\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m65535\u001b[39m),\n\u001b[1;32m     26\u001b[0m ]\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/orm/utility.py:434\u001b[0m, in \u001b[0;36mhas_collection\u001b[0;34m(collection_name, using, timeout)\u001b[0m\n\u001b[1;32m    415\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mhas_collection\u001b[39m(collection_name: \u001b[38;5;28mstr\u001b[39m, using: \u001b[38;5;28mstr\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdefault\u001b[39m\u001b[38;5;124m\"\u001b[39m, timeout: Optional[\u001b[38;5;28mfloat\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m):\n\u001b[1;32m    416\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    417\u001b[0m \u001b[38;5;124;03m    Checks whether a specified collection exists.\u001b[39;00m\n\u001b[1;32m    418\u001b[0m \n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    432\u001b[0m \u001b[38;5;124;03m        >>> utility.has_collection(\"test_collection\")\u001b[39;00m\n\u001b[1;32m    433\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 434\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_get_connection\u001b[49m\u001b[43m(\u001b[49m\u001b[43musing\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhas_collection\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcollection_name\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:254\u001b[0m, in \u001b[0;36merror_handler.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    252\u001b[0m     record_dict[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC error\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(datetime\u001b[38;5;241m.\u001b[39mdatetime\u001b[38;5;241m.\u001b[39mnow())\n\u001b[1;32m    253\u001b[0m     LOGGER\u001b[38;5;241m.\u001b[39merror(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC error: [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00minner_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m], \u001b[39m\u001b[38;5;132;01m{\u001b[39;00me\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m, <Time:\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mrecord_dict\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m>\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m--> 254\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n\u001b[1;32m    255\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m grpc\u001b[38;5;241m.\u001b[39mFutureTimeoutError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    256\u001b[0m     record_dict[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgRPC timeout\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(datetime\u001b[38;5;241m.\u001b[39mdatetime\u001b[38;5;241m.\u001b[39mnow())\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:250\u001b[0m, in \u001b[0;36merror_handler.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    248\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    249\u001b[0m     record_dict[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC start\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(datetime\u001b[38;5;241m.\u001b[39mdatetime\u001b[38;5;241m.\u001b[39mnow())\n\u001b[0;32m--> 250\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    251\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MilvusException \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    252\u001b[0m     record_dict[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRPC error\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(datetime\u001b[38;5;241m.\u001b[39mdatetime\u001b[38;5;241m.\u001b[39mnow())\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:297\u001b[0m, in \u001b[0;36mtracing_request.<locals>.wrapper.<locals>.handler\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m    295\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m level:\n\u001b[1;32m    296\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mset_onetime_loglevel(level)\n\u001b[0;32m--> 297\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:195\u001b[0m, in \u001b[0;36mretry_on_rpc_failure.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    193\u001b[0m         back_off \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mmin\u001b[39m(back_off \u001b[38;5;241m*\u001b[39m back_off_multiplier, max_back_off)\n\u001b[1;32m    194\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 195\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n\u001b[1;32m    196\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    197\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01me\u001b[39;00m\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/decorators.py:165\u001b[0m, in \u001b[0;36mretry_on_rpc_failure.<locals>.wrapper.<locals>.handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    163\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[1;32m    164\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 165\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    166\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m grpc\u001b[38;5;241m.\u001b[39mRpcError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    167\u001b[0m         \u001b[38;5;66;03m# Do not retry on these codes\u001b[39;00m\n\u001b[1;32m    168\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m e\u001b[38;5;241m.\u001b[39mcode() \u001b[38;5;129;01min\u001b[39;00m IGNORE_RETRY_CODES:\n",
      "File \u001b[0;32m~/Library/Python/3.9/lib/python/site-packages/pymilvus/client/grpc_handler.py:415\u001b[0m, in \u001b[0;36mGrpcHandler.has_collection\u001b[0;34m(self, collection_name, timeout, **kwargs)\u001b[0m\n\u001b[1;32m    412\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mcode \u001b[38;5;241m==\u001b[39m ErrorCode\u001b[38;5;241m.\u001b[39mCOLLECTION_NOT_FOUND:\n\u001b[1;32m    413\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m--> 415\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m MilvusException(reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mcode, reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39mreason, reply\u001b[38;5;241m.\u001b[39mstatus\u001b[38;5;241m.\u001b[39merror_code)\n",
      "\u001b[0;31mMilvusException\u001b[0m: <MilvusException: (code=1100, message=Invalid collection name: mt-rag-clapnq-elser-512-100-20240503. collection name can only contain numbers, letters and underscores: invalid parameter)>"
     ]
    }
   ],
   "source": [
    "from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection\n",
    "from sentence_transformers import SentenceTransformer\n",
    "from tqdm import tqdm\n",
    "import json\n",
    "\n",
    "# 1. Connect to Milvus\n",
    "\n",
    "connections.connect(\n",
    "    alias=\"default\",\n",
    "    host=\"127.0.0.1\",   # works in your setup\n",
    "    port=\"19530\"\n",
    ")\n",
    "\n",
    "# 2. Create Collection Schema\n",
    "collection_name = \"clapnq_passages\"\n",
    "\n",
    "# Drop if exists\n",
    "from pymilvus import utility\n",
    "if utility.has_collection(collection_name):\n",
    "    utility.drop_collection(collection_name)\n",
    "\n",
    "fields = [\n",
    "    FieldSchema(name=\"id\", dtype=DataType.VARCHAR, is_primary=True, max_length=200),\n",
    "    FieldSchema(name=\"embedding\", dtype=DataType.FLOAT_VECTOR, dim=384),  # MiniLM output dimension\n",
    "    FieldSchema(name=\"text\", dtype=DataType.VARCHAR, max_length=65535),\n",
    "]\n",
    "\n",
    "schema = CollectionSchema(fields, description=\"ClapNQ passage-level corpus\")\n",
    "collection = Collection(name=collection_name, schema=schema)\n",
    "print(\"✓ Collection created\")\n",
    "\n",
    "# 3. Load MiniLM Model\n",
    "print(\"Loading MiniLM embeddings model...\")\n",
    "model = SentenceTransformer(\"sentence-transformers/all-MiniLM-L6-v2\")\n",
    "print(\"✓ Model loaded\")\n",
    "\n",
    "# 4. Load ClapNQ Passages\n",
    "path = \"/Users/mohit/Desktop/NLP-Project-SemEval-Task8/corpora/passage_level/clapnq.jsonl\"\n",
    "\n",
    "passage_ids = []\n",
    "passage_texts = []\n",
    "\n",
    "print(\"Reading passages...\")\n",
    "with open(path) as f:\n",
    "    for line in f:\n",
    "        obj = json.loads(line)\n",
    "        passage_ids.append(obj[\"_id\"])\n",
    "        passage_texts.append(obj[\"text\"])\n",
    "\n",
    "print(f\"✓ Loaded {len(passage_ids)} passages\")\n",
    "\n",
    "# 5. Insert in Batches with Embeddings\n",
    "BATCH = 256\n",
    "print(\"Starting embedding + insertion...\")\n",
    "\n",
    "for i in tqdm(range(0, len(passage_texts), BATCH)):\n",
    "    batch_ids = passage_ids[i:i+BATCH]\n",
    "    batch_texts = passage_texts[i:i+BATCH]\n",
    "\n",
    "    # Generate embeddings (MiniLM -> 384-dim)\n",
    "    batch_embeddings = model.encode(batch_texts, convert_to_numpy=True).tolist()\n",
    "\n",
    "    # Insert into Milvus\n",
    "    collection.insert([batch_ids, batch_embeddings, batch_texts])\n",
    "\n",
    "print(\"✓ Finished inserting all passages\")\n",
    "\n",
    "# 6. Create Index\n",
    "index_params = {\n",
    "    \"index_type\": \"IVF_FLAT\",\n",
    "    \"metric_type\": \"COSINE\",\n",
    "    \"params\": {\"nlist\": 2048}\n",
    "}\n",
    "\n",
    "print(\"Building vector index...\")\n",
    "collection.create_index(field_name=\"embedding\", index_params=index_params)\n",
    "print(\"✓ Index built\")\n",
    "\n",
    "# 7. Load Collection for Searching\n",
    "collection.load()\n",
    "print(\"✓ Collection loaded & ready for search!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Embedding 0: [-0.11855029 -0.02213986  0.01778213 -0.02428699 -0.00693649  0.00115193\n",
      " -0.0012625   0.04398824 -0.00718389  0.05651155]... (dim=384)\n",
      "Embedding 1: [-0.02696555 -0.01277182  0.02977032 -0.08650455  0.06651282  0.03194625\n",
      " -0.03068677  0.01504944 -0.00052012 -0.0320821 ]... (dim=384)\n",
      "Embedding 2: [-0.021848    0.07122426  0.00184692 -0.11089488  0.02228159  0.01925579\n",
      " -0.02854635 -0.02844507  0.01250403 -0.02986964]... (dim=384)\n",
      "Embedding 3: [ 0.00701434  0.00355477 -0.01642065 -0.08840613  0.10574561  0.03929438\n",
      "  0.01180612 -0.02926991 -0.04262488  0.03408423]... (dim=384)\n",
      "Embedding 4: [-0.03925532 -0.00158098  0.02350306 -0.01048431  0.04540617  0.03902591\n",
      " -0.04975101  0.0625867  -0.0528319  -0.01387044]... (dim=384)\n",
      "Embedding 5: [ 0.09981296  0.03689335 -0.0677207  -0.06775098  0.08487421  0.00608058\n",
      "  0.02794629 -0.04413663  0.03554465  0.00873239]... (dim=384)\n",
      "Embedding 6: [-0.06892251 -0.0256021   0.00053463 -0.0173679  -0.01588602  0.01997466\n",
      "  0.03531457  0.04136641 -0.05784315  0.03201466]... (dim=384)\n",
      "Embedding 7: [-0.00037037  0.03268924 -0.02159727  0.03846634  0.09203841  0.03542484\n",
      "  0.0198022   0.07921433 -0.00918095  0.01825479]... (dim=384)\n",
      "Embedding 8: [-0.00757764  0.03249165  0.00057352 -0.00263553  0.06974159  0.02002492\n",
      "  0.03079503  0.10025892  0.02962441 -0.02762082]... (dim=384)\n",
      "Embedding 9: [ 0.03115204  0.04824591 -0.02545237 -0.08894457  0.08326529  0.01471463\n",
      " -0.04178195 -0.02867009 -0.02207232  0.01838059]... (dim=384)\n"
     ]
    }
   ],
   "source": [
    "# Print first 3 embeddings after encoding\n",
    "emb = model.encode(passage_texts[:10])\n",
    "for i, e in enumerate(emb):\n",
    "    print(f\"Embedding {i}: {e[:10]}... (dim={len(e)})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "837799097_6931-7548-0-617 0.627049446105957\n",
      "French Revolution\n",
      "After the Thermidorian Reaction , an executive council known as the Directory assumed control of the French state in 1795 . They suspended elections , repudiated debt - resulting in financial instability , persecuted the Catholic clergy , and made significant military conquests abroad . Dogged by charges of corruption , the Directory collapsed in a coup led by Napoleon Bonaparte in 1799 . Napoleon , who became the hero of the Revolution through his popular military campaigns , established the Consulate and later the First Empire , setting the stage for a wider array of global conflicts in the Napoleonic Wars .\n",
      "----\n",
      "833122377_27347-27845-0-498 0.6186552047729492\n",
      "Napoleon\n",
      "Unknown to Bonaparte , the Directory had sent him orders to return to ward off possible invasions of French soil , but poor lines of communication prevented the delivery of these messages . By the time that he reached Paris in October , France 's situation had been improved by a series of victories . The Republic , however , was bankrupt and the ineffective Directory was unpopular with the French population . The Directory discussed Bonaparte 's `` desertion '' but was too weak to punish him .\n",
      "----\n",
      "837799097_88359-88956-0-597 0.6068961024284363\n",
      "French Revolution\n",
      "Although committed to Republicanism , the Directory distrusted democracy . Historians have seldom praised the Directory ; it was a government of self - interest rather than virtue , thus losing any claim on idealism . It never had a strong base of popular support ; when elections were held , most of its candidates were defeated . Its achievements were minor . Brown stresses the turn towards dictatorship and the failure of liberal democracy under the Directory , blaming it on , `` chronic violence , ambivalent forms of justice , and repeated recourse to heavy - handed repression . '' General\n",
      "----\n",
      "807203428_28578-29018-0-440 0.5658490657806396\n",
      "Modern history\n",
      "The Executive Directory was a body of five Directors that held executive power in France following the Convention and preceding the Consulate . The period of this regime ( 2 November 1795 until 10 November 1799 ) , commonly known as the Directory ( or Directoire ) era , constitutes the second to last stage of the French Revolution . Napoleon , before seizing the title of Emperor , was elected as First Consul of the Consulate of France .\n",
      "----\n",
      "837799097_87714-88358-0-640 0.5614560842514038\n",
      "French Revolution\n",
      "The constitutional party in the legislature desired toleration of the nonjuring clergy , the repeal of the laws against the relatives of the émigrés , and some merciful discrimination towards the émigrés themselves . The directors baffled all such endeavours . On the other hand , the socialist conspiracy of Babeuf was easily quelled . Little was done to improve the finances , and the assignats continued to fall in value until each note was worth less than the paper it was printed on ; debtors easily paid off their debts . A series of financial reforms started by the Directory finally took effect after it fell from power . Evaluation\n",
      "----\n"
     ]
    }
   ],
   "source": [
    "query = \"What caused the fall of the French Directory?\"\n",
    "\n",
    "embedding = model.encode([query]).tolist()\n",
    "\n",
    "results = collection.search(\n",
    "    data=embedding,\n",
    "    anns_field=\"embedding\",\n",
    "    param={\"metric_type\": \"COSINE\", \"params\": {\"nprobe\": 10}},\n",
    "    limit=5,\n",
    "    output_fields=[\"text\"]\n",
    ")\n",
    "\n",
    "for hit in results[0]:\n",
    "    print(hit.id, hit.distance)\n",
    "    print(hit.entity.get(\"text\"))\n",
    "    print(\"----\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loaded 208 queries\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "def load_queries(jsonl_path):\n",
    "    queries = {}\n",
    "    with open(jsonl_path, \"r\", encoding=\"utf-8\") as f:\n",
    "        for line in f:\n",
    "            obj = json.loads(line)\n",
    "            qid = obj.get(\"_id\")\n",
    "            text = obj.get(\"text\")\n",
    "            queries[qid] = text\n",
    "    return queries\n",
    "\n",
    "CLAPNQ_QUERY_PATH = \"../human/clapnq_questions.jsonl\"\n",
    "queries = load_queries(CLAPNQ_QUERY_PATH)\n",
    "print(f\"Loaded {len(queries)} queries\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymilvus import Collection\n",
    "\n",
    "def retrieve_top_k(query_texts, top_k=100):\n",
    "    results = {}\n",
    "    for qid, text in query_texts.items():\n",
    "        q_emb = model.encode([text], convert_to_numpy=True)\n",
    "\n",
    "        search_params = {\"metric_type\": \"COSINE\", \"params\": {\"nprobe\": 16}}\n",
    "\n",
    "        raw = collection.search(\n",
    "            data=q_emb,\n",
    "            anns_field=\"embedding\",\n",
    "            param=search_params,\n",
    "            limit=top_k,\n",
    "            output_fields=[\"text\"]\n",
    "        )[0]\n",
    "\n",
    "        results[qid] = [\n",
    "            (hit.id, float(hit.score)) for hit in raw\n",
    "        ]\n",
    "    return results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_evaluation_format(results_with_scores, collection_name=\"clapnq_passages\"):\n",
    "    output = []\n",
    "    for qid, docs in results_with_scores.items():\n",
    "        contexts = []\n",
    "        for doc_id, sim_score in docs:\n",
    "            contexts.append({\n",
    "                \"document_id\": doc_id,\n",
    "                \"score\": sim_score\n",
    "            })\n",
    "        output.append({\n",
    "            \"task_id\": qid,\n",
    "            \"Collection\": collection_name,\n",
    "            \"contexts\": contexts\n",
    "        })\n",
    "    return output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "def save_predictions(evaluation_data, filename):\n",
    "    with open(filename, \"w\") as f:\n",
    "        for item in evaluation_data:\n",
    "            f.write(json.dumps(item) + \"\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running retrieval over CLAPNQ queries...\n",
      "Formatting retrieval results...\n",
      "Saving predictions...\n",
      "Done! File saved: clapnq_retrieval_predictions.jsonl\n"
     ]
    }
   ],
   "source": [
    "# 1. Run retrieval\n",
    "print(\"Running retrieval over CLAPNQ queries...\")\n",
    "retrieval_results = retrieve_top_k(queries, top_k=100)\n",
    "\n",
    "# 2. Convert to SemEval evaluation format\n",
    "print(\"Formatting retrieval results...\")\n",
    "evaluation_data = create_evaluation_format(retrieval_results)\n",
    "\n",
    "# 3. Save as jsonl\n",
    "print(\"Saving predictions...\")\n",
    "save_predictions(evaluation_data, \"clapnq_retrieval_predictions.jsonl\")\n",
    "\n",
    "print(\"Done! File saved: clapnq_retrieval_predictions.jsonl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...\n",
      "To disable this warning, you can either:\n",
      "\t- Avoid using `tokenizers` before the fork if possible\n",
      "\t- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)\n",
      "usage: run_retrieval_eval.py [-h] --input_file INPUT_FILE --output_file\n",
      "                             OUTPUT_FILE\n",
      "run_retrieval_eval.py: error: unrecognized arguments: --qrels_file ../human/retrieval_tasks_convid/cloud/qrels/dev.tsv\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "CompletedProcess(args=['python3', '../scripts/evaluation/run_retrieval_eval.py', '--input_file', 'clapnq_retrieval_predictions.jsonl', '--qrels_file', '../human/retrieval_tasks_convid/cloud/qrels/dev.tsv', '--output_file', 'clapnq_retrieval_eval.jsonl'], returncode=2)"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import subprocess\n",
    "\n",
    "subprocess.run([\n",
    "    \"python3\",\n",
    "    \"../scripts/evaluation/run_retrieval_eval.py\",\n",
    "    \"--input_file\", \"clapnq_retrieval_predictions.jsonl\",\n",
    "    \"--qrels_file\", \"../human/retrieval_tasks_convid/cloud/qrels/dev.tsv\",\n",
    "    \"--output_file\", \"clapnq_retrieval_eval.jsonl\"\n",
    "])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loaded: 208 full queries, 208 rewrite queries, 188 qrels entries\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "\n",
    "def load_queries(jsonl_path):\n",
    "    queries = {}\n",
    "    with open(jsonl_path, \"r\", encoding=\"utf-8\") as fh:\n",
    "        for line in fh:\n",
    "            obj = json.loads(line)\n",
    "            qid = obj.get(\"_id\")\n",
    "            text = obj.get(\"text\",\"\").strip()\n",
    "            queries[qid] = text\n",
    "    return queries\n",
    "\n",
    "def load_qrels(tsv_path):\n",
    "    df = pd.read_csv(tsv_path, sep=\"\\t\")\n",
    "    qrels = {}\n",
    "    for _, row in df.iterrows():\n",
    "        qid = row[\"query-id\"]\n",
    "        docid = row[\"corpus-id\"]\n",
    "        score = int(row[\"score\"])\n",
    "        qrels.setdefault(qid, {})[docid] = score\n",
    "    return qrels\n",
    "\n",
    "full_queries = load_queries(\"../human/clapnq_questions.jsonl\")\n",
    "rewrite_queries = load_queries(\"../human/clapnq_rewrite.jsonl\")\n",
    "qrels = load_qrels(\"../human/retrieval_tasks_convid/cloud/qrels/dev.tsv\")\n",
    "\n",
    "print(\"Loaded:\",\n",
    "      len(full_queries), \"full queries,\",\n",
    "      len(rewrite_queries), \"rewrite queries,\",\n",
    "      len(qrels), \"qrels entries\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymilvus import Collection\n",
    "\n",
    "def retrieve_clapnq_with_scores(query_texts, top_k=100):\n",
    "    results = {}\n",
    "    for qid, qtext in query_texts.items():\n",
    "        q_emb = model.encode([qtext], convert_to_numpy=True)\n",
    "        raw = collection.search(\n",
    "            data=q_emb,\n",
    "            anns_field=\"embedding\",\n",
    "            param={\"metric_type\": \"COSINE\", \"params\": {\"nprobe\": 16}},\n",
    "            limit=top_k,\n",
    "            output_fields=[\"text\"]\n",
    "        )[0]\n",
    "\n",
    "        retrieved = []\n",
    "        for hit in raw:\n",
    "            # Milvus COSINE → higher is better (Milvus returns distance)\n",
    "            sim = 1 - hit.distance\n",
    "            retrieved.append((str(hit.id), float(sim)))\n",
    "        retrieved.sort(key=lambda x: x[1], reverse=True)\n",
    "\n",
    "        results[qid] = retrieved\n",
    "    return results\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_clapnq_eval_format(results_with_scores, queries):\n",
    "    output = []\n",
    "    for qid, docs in results_with_scores.items():\n",
    "        if qid not in queries:\n",
    "            continue\n",
    "\n",
    "        contexts = [{\"document_id\": doc_id, \"score\": sim_score}\n",
    "                    for doc_id, sim_score in docs]\n",
    "\n",
    "        output.append({\n",
    "            \"task_id\": qid,\n",
    "\n",
    "            # ⭐ MUST match evaluator's CLAPNQ collection name\n",
    "            \"Collection\": \"mt-rag-clapnq-elser-512-100-20240503\",\n",
    "\n",
    "            \"contexts\": contexts\n",
    "        })\n",
    "    return output\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pathlib import Path\n",
    "import json\n",
    "\n",
    "QRELS_PATH = Path(\"../human/retrieval_tasks_convid/cloud/qrels/dev.tsv\")\n",
    "\n",
    "def run_clapnq_eval(queries, out_pred_name, out_eval_name):\n",
    "\n",
    "    # Load qrels and extract cloud query IDs\n",
    "    qrels = load_qrels(QRELS_PATH)\n",
    "    cloud_qids = set(qrels.keys())\n",
    "\n",
    "    # restrict queries to cloud qrels\n",
    "    filtered_queries = {qid: queries[qid] for qid in cloud_qids if qid in queries}\n",
    "\n",
    "    print(\"Running retrieval with proper similarity scores...\")\n",
    "    results = retrieve_clapnq_with_scores(filtered_queries)\n",
    "\n",
    "    print(\"Formatting...\")\n",
    "    eval_data = create_clapnq_eval_format(results, filtered_queries)\n",
    "\n",
    "    out_dir = Path(\"outputs_clapnq\")\n",
    "    out_dir.mkdir(parents=True, exist_ok=True)\n",
    "\n",
    "    pred_path = out_dir / (out_pred_name + \".jsonl\")\n",
    "\n",
    "    with open(pred_path, \"w\") as f:\n",
    "        for item in eval_data:\n",
    "            f.write(json.dumps(item) + \"\\n\")\n",
    "\n",
    "    print(f\"Saved predictions to: {pred_path}\")\n",
    "\n",
    "    eval_script = \"../scripts/evaluation/run_retrieval_eval.py\"\n",
    "\n",
    "    print(\"Running Evaluator...\")\n",
    "    result = subprocess.run([\n",
    "        \"python3\",\n",
    "        str(eval_script),\n",
    "        \"--input_file\", str(pred_path),\n",
    "        \"--output_file\", str(out_dir / (out_eval_name + \".jsonl\"))\n",
    "    ], capture_output=True, text=True)\n",
    "\n",
    "    print(\"Evaluation script output:\")\n",
    "    print(result.stdout)\n",
    "    if result.stderr:\n",
    "        print(\"Errors:\")\n",
    "        print(result.stderr)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running retrieval with proper similarity scores...\n",
      "Formatting...\n",
      "Saved predictions to: outputs_clapnq/clapnq_full_predictions.jsonl\n",
      "Running Evaluator...\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...\n",
      "To disable this warning, you can either:\n",
      "\t- Avoid using `tokenizers` before the fork if possible\n",
      "\t- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Evaluation script output:\n",
      "\n",
      "Errors:\n",
      "Traceback (most recent call last):\n",
      "  File \"/Users/mohit/Desktop/NLP-Project-SemEval-Task8/Milvus/../scripts/evaluation/run_retrieval_eval.py\", line 190, in <module>\n",
      "    main()\n",
      "  File \"/Users/mohit/Desktop/NLP-Project-SemEval-Task8/Milvus/../scripts/evaluation/run_retrieval_eval.py\", line 161, in main\n",
      "    n = len(scores_global_lst[0]['Recall'])\n",
      "IndexError: list index out of range\n",
      "\n"
     ]
    }
   ],
   "source": [
    "run_clapnq_eval(full_queries, \"clapnq_full_predictions\", \"clapnq_full_eval\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CLAPNQ query IDs: ['dd6b6ffd177f2b311abe676261279d2f<::>2', 'dd6b6ffd177f2b311abe676261279d2f<::>3', 'dd6b6ffd177f2b311abe676261279d2f<::>4', 'dd6b6ffd177f2b311abe676261279d2f<::>5', 'dd6b6ffd177f2b311abe676261279d2f<::>6', 'dd6b6ffd177f2b311abe676261279d2f<::>7', 'dd6b6ffd177f2b311abe676261279d2f<::>8', '3f5fa378239f7475baac89fa40288aaa<::>1', '3f5fa378239f7475baac89fa40288aaa<::>2', '3f5fa378239f7475baac89fa40288aaa<::>3']\n",
      "CLAPNQ qrels IDs: ['d5b1e735a040853ed361a3dfde1b8ef0<::>1', 'd5b1e735a040853ed361a3dfde1b8ef0<::>2', 'd5b1e735a040853ed361a3dfde1b8ef0<::>3', 'd5b1e735a040853ed361a3dfde1b8ef0<::>4', 'd5b1e735a040853ed361a3dfde1b8ef0<::>5', 'd5b1e735a040853ed361a3dfde1b8ef0<::>6', 'd5b1e735a040853ed361a3dfde1b8ef0<::>7', 'd5b1e735a040853ed361a3dfde1b8ef0<::>8', 'd5b1e735a040853ed361a3dfde1b8ef0<::>9', 'fdee20f7fd677e420742b09989623d68<::>1']\n"
     ]
    }
   ],
   "source": [
    "# Paste output here\n",
    "print(\"CLAPNQ query IDs:\", list(full_queries.keys())[:10])\n",
    "\n",
    "qrels = load_qrels(QRELS_PATH)\n",
    "print(\"CLAPNQ qrels IDs:\", list(qrels.keys())[:10])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter()\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "from collections import Counter\n",
    "\n",
    "collections = Counter()\n",
    "\n",
    "with open(\"outputs_clapnq/clapnq_full_predictions.jsonl\") as f:\n",
    "    for line in f:\n",
    "        obj = json.loads(line)\n",
    "        collections[obj[\"Collection\"]] += 1\n",
    "\n",
    "print(collections)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

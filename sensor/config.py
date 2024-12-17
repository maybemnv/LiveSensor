from dataclasses import dataclass
import os
import pymongo
@dataclass

class EnviromentVaiable:
    mongo_db_url:str="mongodb+srv://manavkauahal99:Manav%407410@apscluster0.h6w0y.mongodb.net/?retryWrites=true&w=majority&appName=ApsCluster0"

    

env=EnviromentVaiable()
mongo_client=pymongo.MongoClient(env.mongo_db_url)
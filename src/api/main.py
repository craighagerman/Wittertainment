from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fetch import Fetch

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------------------------------------------------------------------
# Endpoints
# ----------------------------------------------------------------------------------------

@app.get("/query")
def query(q: Union[str, None] = None):
    """
    Return results for a given query
    """
    if q:
        return Fetch().query_vespa(q)


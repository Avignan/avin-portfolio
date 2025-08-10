#!/bin/bash

echo "Starting FastAPI server..."
if [ "$FASTAPI_ENV" = "production" ]; then
    uvicorn getInformation:app --host 0.0.0.0 --port 8001 --workers 2
else
    uvicorn getInformation:app --host 0.0.0.0 --port 8001 --reload
fi
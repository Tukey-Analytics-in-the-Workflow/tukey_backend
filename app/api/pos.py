from fastapi import APIRouter, UploadFile
import pandas as pd

router = APIRouter()

@router.post("/upload")
async def upload_pos(file: UploadFile):
    df = pd.read_csv(file.file)
    
    # MVP: just validate & preview
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "sample": df.head(5).to_dict()
    }

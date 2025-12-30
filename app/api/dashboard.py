from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_dashboards():
    return [
        {
            "id": "sales-overview",
            "name": "Sales Overview",
            "embed_url": "https://tableau.com/views/sales"
        }
    ]

@router.get("/{dashboard_id}/embed-token")
def get_embed_token(dashboard_id: str):
    # MVP stub – later JWT → Tableau Connected App
    return {"token": "tableau-embed-token"}

from pydantic import BaseModel

class AIQuery(BaseModel):
    time_period: str
    region: str
    top_products: list[str]
    sales_trend: str

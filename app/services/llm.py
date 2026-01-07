from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
import logging

logger = logging.getLogger(__name__)

# Initialize OpenAI client (will be None if API key not set)
client = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(context: dict):
    """
    Generate business decision recommendations using OpenAI API based on POS data context.
    
    Args:
        context: Dictionary containing:
            - time_period: str (e.g., "Winter", "Q1 2024")
            - region: str (e.g., "Delhi", "Mumbai")
            - top_products: list[str] (e.g., ["Jackets", "Sweaters"])
            - sales_trend: str (e.g., "Increasing", "Decreasing", "Stable")
    
    Returns:
        dict: Contains decision, confidence, and reason
    """
    # Check if OpenAI is configured
    if not client or not OPENAI_API_KEY:
        logger.warning("OpenAI API key not configured. Using fallback response.")
        return {
            "decision": f"Stock more {context.get('top_products', ['products'])[0] if context.get('top_products') else 'products'}",
            "confidence": "Low",
            "reason": f"Sales trend is {context.get('sales_trend', 'unknown')} in {context.get('time_period', 'current period')}. Note: OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file."
        }
    
    try:
        # Construct a detailed prompt for business decision making
        prompt = f"""You are an expert retail business analyst. Based on the following POS (Point of Sale) data, provide a strategic business decision recommendation.

Context:
- Time Period: {context.get('time_period', 'N/A')}
- Region: {context.get('region', 'N/A')}
- Top Products: {', '.join(context.get('top_products', []))}
- Sales Trend: {context.get('sales_trend', 'N/A')}

Please provide a business decision recommendation in the following JSON format:
{{
    "decision": "Your specific recommendation (e.g., 'Stock more winter jackets' or 'Reduce inventory of summer items')",
    "confidence": "High/Medium/Low",
    "reason": "Detailed explanation of why this decision makes sense based on the data provided"
}}

Focus on actionable insights that would help a retail business owner make inventory and sales decisions."""

        # Call OpenAI API
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert retail business analyst specializing in inventory management and sales optimization. Provide clear, actionable business recommendations based on POS data."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,  # Balance between creativity and consistency
            max_tokens=500
        )
        
        # Extract the response content
        ai_response = response.choices[0].message.content.strip()
        
        # Try to parse JSON from the response, fallback to structured response
        import json
        try:
            # Try to extract JSON from the response
            if "{" in ai_response and "}" in ai_response:
                # Extract JSON portion
                start = ai_response.find("{")
                end = ai_response.rfind("}") + 1
                json_str = ai_response[start:end]
                parsed_response = json.loads(json_str)
                
                return {
                    "decision": parsed_response.get("decision", ai_response),
                    "confidence": parsed_response.get("confidence", "Medium"),
                    "reason": parsed_response.get("reason", ai_response)
                }
            else:
                # If no JSON found, structure the response
                return {
                    "decision": ai_response.split("\n")[0] if "\n" in ai_response else ai_response[:100],
                    "confidence": "Medium",
                    "reason": ai_response
                }
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "decision": ai_response.split("\n")[0] if "\n" in ai_response else ai_response[:100],
                "confidence": "Medium",
                "reason": ai_response
            }
            
    except Exception as e:
        logger.error(f"Error calling OpenAI API: {str(e)}")
        # Fallback response in case of API error
        return {
            "decision": f"Stock more {context.get('top_products', ['products'])[0] if context.get('top_products') else 'products'}",
            "confidence": "Low",
            "reason": f"Sales trend is {context.get('sales_trend', 'unknown')} in {context.get('time_period', 'current period')}. Note: AI service temporarily unavailable, using fallback logic."
        }

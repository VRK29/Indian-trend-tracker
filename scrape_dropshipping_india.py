import os
from supabase import create_client, Client

# Get secrets from GitHub environment variables
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in environment variables.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Sample trending products data for Indian e-commerce & dropshipping
trending_products = [
    {
        "name": "Crystal Water Bottle",
        "platform": "Shopify / Dropship",
        "category": "Lifestyle",
        "price": 899,
        "trend_score": 94,
        "supplier_source": "Roposo Clik",
        "target_city": "Mumbai, Delhi, Bangalore"
    },
    {
        "name": "Wireless Car Air Purifier",
        "platform": "Amazon.in",
        "category": "Automotive",
        "price": 1499,
        "trend_score": 88,
        "supplier_source": "Shiprocket 360",
        "target_city": "Delhi NCR, Pune"
    },
    {
        "name": "Orthopedic Neck Pillow",
        "platform": "Flipkart",
        "category": "Health & Care",
        "price": 699,
        "trend_score": 91,
        "supplier_source": "GlowRoad",
        "target_city": "Hyderabad, Chennai"
    },
    {
        "name": "LED Flame Diffuser",
        "platform": "Shopify / Dropship",
        "category": "Home Decor",
        "price": 1199,
        "trend_score": 96,
        "supplier_source": "CJ Dropshipping",
        "target_city": "Bangalore, Ahmedabad"
    }
]

def update_database():
    print("Connecting to Supabase and updating trending products...")
    for product in trending_products:
        response = supabase.table("trending_products").insert(product).execute()
    print("Successfully updated trending products!")

if __name__ == "__main__":
    update_database()

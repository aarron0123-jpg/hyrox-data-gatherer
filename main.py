from fastapi import FastAPI
import pyrox
import pandas as pd

app = FastAPI()

@app.get("/events")
def get_hyrox_events():
    # Use the unofficial pyrox-client to list races
    # You can specify seasons (e.g., season 8) or leave blank for all available
    client = pyrox.PyroxClient()
    
    try:
        # Fetching a list of available races
        all_races = client.list_races()
        
        # Convert to a list of dictionaries for the app to read
        # Adjust fields based on what your app needs
        events = []
        for index, row in all_races.iterrows():
            events.append({
                "name": f"HYROX {row['location'].title()}",
                "location": row['location'].title(),
                "date": "TBD", # The client often provides results; specific upcoming dates may need manual entry or updates
                "ticket_url": f"https://hyrox.com" 
            })
        return events
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "HYROX Data Gatherer is Active. Go to /events to see data."}

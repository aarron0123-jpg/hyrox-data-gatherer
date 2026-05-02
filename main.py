from fastapi import FastAPI
import pyrox
import pandas as pd

app = FastAPI()

@app.get("/events")
def get_hyrox_events():
    client = pyrox.PyroxClient()
    try:
        # Get races from the current season
        all_races = client.list_races()
        
        events = []
        for index, row in all_races.iterrows():
            events.append({
                "name": f"HYROX {str(row['location']).title()}",
                "location": str(row['location']).title(),
                "date": "Check Website", 
                "ticket_url": "https://hyrox.com" 
            })
        return events
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "HYROX Data Gatherer is Active. Go to /events to see data."}


from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from chatbot_model import chatbot


app = FastAPI()


origins = [
    "http://127.0.0.2:8080",
    "http://127.0.0.2", 
    "http://127.0.0.2:8080/index.html" # CHANGE to Wordpress url
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",

    ]

# Add CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # List of allowed origins
    allow_credentials=True,         # Allow cookies and authentication headers
    allow_methods=["POST"],         # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],            # Allow all headers
)



@app.post("/process")
async def process_request(data: dict, request: Request):
    try:
       
        origin = request.headers.get("Origin")
        print(f"Request received from Origin: {origin}")
        
        print(f"Request headers: {request.headers}")
        
        # Example processing logic
        print("data", data)
        chatbot_reply = interact_with_chatbot(data["message"]) 
        return {"status": "success", "chatbot_reply": chatbot_reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")
        
        
def interact_with_chatbot(input_message):
    response = chatbot.get_response(input_message)
    output_message = str(response)
    print(output_message)
    return output_message



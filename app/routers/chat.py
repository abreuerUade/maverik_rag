from fastapi import APIRouter, HTTPException
from app.services.agent import create_agent_executor
from app.models.chat import ChatRequest, ChatResponse

router = APIRouter()

# Crear el agente ejecutor


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    user_input = request.input
    user_profile = request.userProfile
    chat_history = request.chatHistory
    
    agent_executor = create_agent_executor(user_profile)
    print(agent_executor)
    prompt_values = {
        "input": user_input,
        "chat_history": chat_history
    }

    try:
        response = agent_executor.invoke(prompt_values)
        output = response["output"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    return ChatResponse(response=output)

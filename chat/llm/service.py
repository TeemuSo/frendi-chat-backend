from typing import Dict, Any, List
from openai import OpenAI
from ..config import get_settings
from ..knowledge.zep import ZepService

settings = get_settings()

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = "gpt-3.5-turbo"
        self.zep_service = ZepService()

    async def process_message(
        self,
        message: str,
        user_id: str,
        conversation_id: str = None,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Process a message using OpenAI's GPT model with ZepAI knowledge integration.
        """
        try:
            # Query ZepAI for relevant knowledge
            knowledge_results = await self.zep_service.query_knowledge_graph(message)
            knowledge_context = ""
            
            if knowledge_results:
                knowledge_context = "\nRelevant information from knowledge base:\n"
                for result in knowledge_results:
                    knowledge_context += f"- {result['content_snippet']}\n"

            # Create a system message that explains the agent's capabilities
            system_message = {
                "role": "system",
                "content": """You are a helpful AI assistant with access to a knowledge graph.
                You can:
                1. Answer general questions directly
                2. Use knowledge from the knowledge graph when relevant
                3. Provide detailed explanations
                
                Always be concise and accurate in your responses."""
            }

            # Create the user message with knowledge context
            user_message = {
                "role": "user",
                "content": f"{message}\n{knowledge_context}"
            }

            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[system_message, user_message],
                temperature=0.7,
                max_tokens=500
            )

            return {
                "response": response.choices[0].message.content,
                "metadata": {
                    "tokens_used": response.usage.total_tokens,
                    "knowledge_graph_accessed": bool(knowledge_results),
                    "processing_time": 0.0  # TODO: Add actual processing time
                }
            }

        except Exception as e:
            raise Exception(f"Error processing message: {str(e)}") 
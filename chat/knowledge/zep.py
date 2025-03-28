from typing import Dict, Any, List
from zep_cloud.client import Zep
from ..config import get_settings

settings = get_settings()

class ZepService:
    def __init__(self):
        self.client = Zep(
            api_key=settings.zep_api_key,
        )

    async def process_query(self, query: str, user_id: str) -> Dict[str, Any]:
        """
        Process a query using ZepAI knowledge graph.
        """
        try:
            # Create or get session
            session_id = f"session_{user_id}"
            
            # Search for relevant information
            search_results = await self.client.memory.search(
                session_id=session_id,
                query=query,
                limit=5
            )

            # Format response
            if search_results:
                response = "Based on the knowledge graph:\n"
                for result in search_results:
                    response += f"- {result.content}\n"
            else:
                response = "No relevant information found in the knowledge graph."

            return {
                "response": response,
                "metadata": {
                    "knowledge_graph_accessed": True,
                    "results_found": len(search_results)
                }
            }

        except Exception as e:
            raise Exception(f"Error querying knowledge graph: {str(e)}")

    async def create_session(self, user_id: str) -> str:
        """
        Create a new session for a user.
        """
        try:
            session_id = f"session_{user_id}_{int(time.time())}"
            await self.client.memory.add_session(
                session_id=session_id,
                user_id=user_id,
            )
            return session_id
        except Exception as e:
            raise Exception(f"Error creating Zep session: {str(e)}")

    async def query_knowledge_graph(self, query: str) -> List[Dict[str, str]]:
        """
        Query the ZepAI knowledge graph for relevant information.
        """
        try:
            # Basic search with minimal parameters
            search_results = await self.client.memory.search(
                message=query,  # Try using 'message' instead of 'query' or 'text'
                k=5  # Number of results to return
            )

            # Format results
            results = []
            for result in search_results:
                results.append({
                    "content_snippet": str(result),  # Convert result to string in case of different return type
                    "relevance_score": 1.0
                })

            return results

        except Exception as e:
            raise Exception(f"Error querying ZepAI knowledge graph: {str(e)}")

    async def add_to_knowledge_graph(
        self,
        content: str,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Add new information to the knowledge graph.
        """
        try:
            memory = Memory(
                content=content,
                metadata=metadata or {}
            )
            
            result = await self.client.memory.add(memory)
            return {"id": result.id, "status": "success"}

        except Exception as e:
            raise Exception(f"Error adding to ZepAI knowledge graph: {str(e)}") 
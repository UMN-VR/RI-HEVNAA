from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)
import dotenv

dotenv.load_dotenv('creds.env')


from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
resp = chat([HumanMessage(content="Write me a song about sparkling water.")])
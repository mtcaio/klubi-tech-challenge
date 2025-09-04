from openai import OpenAI
import streamlit as st

import json

from helpers.data_context import DataContext
from helpers.logger import Logger
from settings.openai_settings import OpenAISettings

_logger = Logger(logger_name=__name__).logger


class CarChatbot:
    def __init__(self, data_path: str):
        self.settings = OpenAISettings()
        self.client = OpenAI(api_key=self.settings.OPENAI_API_KEY)

        self.data_context = DataContext(data_path=data_path)
        self.car_data = self.data_context.load_data()

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "system", "content": self.get_system_prompt()}
            ]

    def get_system_prompt(self) -> str:
        return (
            f"You are a helpful assistant that ONLY provides information "
            f"about the following cars:\n\n{json.dumps(self.car_data, indent=2)}\n\n"
            f"If a user asks about a car not listed, politely say it’s not available. "
            f"If they ask about a listed car, give a short description and say that "
            f"you’ll display its details above your answer. "
            f"Always respond ONLY in Portuguese. "
            f"Talk like a friendly car salesman."
        )

    def render_car_card(self, prompt: str) -> bool:
        for car in self.car_data:
            if car["Model"].lower() in prompt.lower() or car["Name"].lower() in prompt.lower():
                with st.container():
                    st.subheader(f"{car['Name']} {car['Model']}")
                    st.image(car["Image"], width=300)
                    st.write(f"Preço: R$ {car['Price']:,}".replace(",", "."))
                    st.write(f"Localização: {car['Location']}")
                _logger.info(f"Exibindo informações do carro: {car['Name']} {car['Model']}")
                return True
        return False

    def display_chat_history(self):
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

    def handle_user_input(self, prompt: str):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        self.render_car_card(prompt)

        stream = self.client.chat.completions.create(
            model=self.settings.MODEL,
            messages=st.session_state.messages,
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)

        st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    _logger.info("Iniciando a aplicação Streamlit.")
    st.title("Buscador de Carros")
    st.write("Encontre o carro dos seus sonhos!")

    chatbot = CarChatbot(data_path="data/cars.json")
    chatbot.display_chat_history()

    if prompt := st.chat_input("Me diga qual modelo você está procurando..."):
        chatbot.handle_user_input(prompt)


if __name__ == "__main__":
    main()

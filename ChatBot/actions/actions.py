# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionRecommendDoctor(Action):
    def name(self):
        return "action_recommend_doctor"

    def run(self, dispatcher, tracker, domain):
        symptoms = tracker.get_slot('symptom')


        doctor_mapping = {
            "internisty": ["kaszel", "gorączka"],
            "neurologa": ["ból głowy", "zawroty"],
            "gastrologa": ["ból brzucha", "nudności"],

        }


        recommended_doctor = "lekarza ogólnego"
        for doctor, doctor_symptoms in doctor_mapping.items():
            if any(symptom in symptoms for symptom in doctor_symptoms):
                recommended_doctor = doctor
                break

        dispatcher.utter_message(text=f"Ojej, wygląda na to, że powinieneś zapisać się do {recommended_doctor}")
        return []

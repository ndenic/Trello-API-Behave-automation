from dataclasses import dataclass

@dataclass
class TrelloBoard:
    id: str
    name: str
    desc: str

@dataclass
class TrelloList:
    id: str
    name: str

@dataclass
class TrelloCard:
    id: str
    name: str
    desc: str
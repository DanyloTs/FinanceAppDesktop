from abc import ABC, abstractmethod

class RepositoryInterface(ABC):
    @abstractmethod
    def add(self, entity): raise NotImplementedError("Add method must be implemented")

    @abstractmethod
    def get_all(self): raise NotImplementedError("get_all method must be implemented")

    @abstractmethod
    def update(self, entity_id, **kwargs): raise NotImplementedError("update method must be implemented")

    @abstractmethod
    def delete(self, entity_id): raise NotImplementedError("delete method must be implemented")
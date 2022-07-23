from ConfigMQTT import *

class OnChangeClass:
    def __init__(self, name, client):
        self._name = name
        self._value = None
        self._status = None
        self._client = client

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value and self._client != None:
            self._value = new_value
            message = self._name + " -> value -> " + str(self._value)
            self._client.publish(TOPIC_FOR_INVIEW[self._name] + "/Value", self._value)
            #self._client.publish(TOPIC_FOR_INVIEW[self._name] + "/Value", self._value)
            #self._notify_observers(new_value)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if self._status != new_status and self._client != None:
            self._status = new_status
            message = self._name + " -> status -> " + str(self._status)
            self._client.publish(TOPIC_FOR_INVIEW[self._name] + "/Status", message)
            #self._client.publish(TOPIC_FOR_INVIEW[self._name] + "/Status", self._status)

    # def _notify_observers(self, new_value):
    #     for callback in self._callbacks:
    #         callback(new_value)

    # def register_callback(self, callback):
    #     self._callbacks.append(callback)

from django.apps import AppConfig


class CounterConfig(AppConfig):
    name = 'calorie_counter.counter'

    def ready(self):
        import calorie_counter.counter.signals

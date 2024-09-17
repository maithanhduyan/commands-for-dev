class AIPlayer:
    def __init__(self, model):
        self.model = model

    def make_decision(self, hand):
        # Use model to decide whether to hit or stand
        decision = self.model.predict(hand)
        return 'hit' if decision > 0.5 else 'stand'
        pass

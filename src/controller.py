from exceptions import InputError

class Controller:
    def __init__(self):
        pass

    def getPrompt(self, options):
        prompt = ''
        for i, option in enumerate(options):
            prompt += str(i) + ': ' + option + '\n'
        return prompt

    def getResponse(self, prompt):
        return input(prompt)

class HumanController(Controller):
    def decide(self, options):
        prompt = self.getPrompt(options)
        result = self.getResponse(prompt)
        return result

class AIController(Controller):
    def decide(self, options):
        return 'grow'
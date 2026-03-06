from rules import NumberRule, TextRule, MixedRule


class RuleFactory:

    @staticmethod
    def create_rules():
        return {
            NumberRule(): "NUMBER",
            TextRule(): "TEXT",
            MixedRule(): "MIXED"
        }
from classes.connective import ConnectiveOr
from classes.proposition import PropositionAtomic, PropositionConnected, PropositionNegated
from formation_sequence import FormationSequence

prop_1 = PropositionAtomic("p", 2)
prop_2 = PropositionAtomic("p", 3)

connective_or = ConnectiveOr()

prop_3 = PropositionConnected(prop_1, prop_2, connective_or)

prop_4 = PropositionNegated(prop_1)

# print(prop_3.display())

prop_5 = PropositionConnected(prop_2, prop_1, connective_or)

prop_6 = PropositionConnected(prop_3, prop_5, connective_or)

prop_7 = PropositionAtomic("p", 4)
prop_8 = PropositionConnected(prop_6, prop_7, connective_or)

prop_9 = PropositionAtomic("a", 1)
prop_10 = PropositionConnected(prop_9, prop_8, connective_or)


# FormationSequence(prop_3).get()
# FormationSequence(prop_5).get()
# FormationSequence(prop_8).get()
FormationSequence(prop_10).get()


# NumberOfBrackets(prop_10).count()
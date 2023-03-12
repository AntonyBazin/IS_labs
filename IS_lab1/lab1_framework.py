from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Defining the network structure
model = BayesianNetwork([("debtsToIncomeRatio", "creditWorthiness"), ("reliability", "creditWorthiness")])

# Defining the CPDs:
cpd_dti = TabularCPD("debtsToIncomeRatio", 2, [[0.3], [0.7]])
cpd_r = TabularCPD("reliability", 2, [[0.6664], [0.3336]])
cpd_cw = TabularCPD(
    "creditWorthiness",
    2,
    [
        [0.2, 0.3, 0.4, 0.5],
        [0.8, 0.7, 0.6, 0.5],
    ],
    evidence=["debtsToIncomeRatio", "reliability"],
    evidence_card=[2, 2],
)

# Associating the CPDs with the network structure.
model.add_cpds(cpd_dti, cpd_r, cpd_cw)

# Some other methods
model.get_cpds()

if __name__ == "__main__":
    print(model.simulate())

lo  = "La densité des noeuds est faible"
med = "La densité des noeuds est moyenne"
hgh = "La densité des noeuds est élevée"

lw  = "L'énergie restante du noeud est faible"
mdm = "L'énergie restante du noeud est moyenne"
hi  = "L'énergie restante du noeud est élevéé"

ne  = "Le noeud est proche de l'évènement"
me  = "Le noeud est à une distance moyenne de l'évènement"
fr  = "Le noeud est éloigné de l'évènement"


vlsp = "La probabilité de sélection du noeud est très faible"
lsp  = "La probabilité de sélection du noeud est faible"
msp = "La probabilité de sélection du noeud est moyenne"
hsp  = "La probabilité de sélection du noeud est grande"
vhsp = "La probabilité de sélection du noeud est très grande"

"""IND = ["Lo", "Med", "hgh"]
INRE = ["Lw", "Mdm", "Hi"]
INDE = ["Ne", "Me", "Fr"]
#--------------------------
IASD = ["VLSP", "LSP", "MSP", "HSP", "VHSP"]"""

IND = [lo, med, hgh]
INRE = [lw, mdm, hi]
INDE = [ne, me, fr]
IASD = [vlsp, lsp, msp, hsp, vhsp]

with open("ALLRules.txt","w") as fichier:
    for i in IND:
        for j in INRE:
            for k in INDE:
                for l in IASD:
                    fichier.write(f"SI {i} ET {j} ET {k} ALORS {l}\n")

x = ""
for i in range(1,28):
    re = "rule_" + str(i)
    x +=  re + ", "
print(x)


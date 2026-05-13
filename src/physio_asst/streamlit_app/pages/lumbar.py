from body_region_app import run_body_region_app

from region_configs.lumbar_config import (
    LUMBAR_SYSTEM_PROMPT,
    COMPARE_PROMPT,
    QA_SYSTEM_PROMPT,
    LUMBAR_REHAB_LINKS,
)


LUMBAR_PREFILLED_EXAMPLE = """IRM COLONNE LOMBO-SACRÉE C-

Renseignements cliniques : lombalgie chronique, douleur para-vertébrale basse droite qui empire, engourdissement jambe droite on/off.

Premier examen de ce genre pour ce patient dans notre service.

Technique :

Selon la technique standard sans injection du Gadolinium.

Trouvailles :

On présume qu'il y a cinq (5) corps vertébraux lombaires. Le conus medullaris se termine normalement à D12-L1.
La partie de la moelle rachidienne visualisée conserve une intensité normale.

Les niveaux étudiés sont D12 à S1.

D12-L1, L1-L2, L2-L3, L3-L4 : Il n'y a pas de hernie discale centrale ni de sténose spinale.

L3-L4 : Minime bombement du disque qui cause une diminution minime à modérée du foramen neural à droite. Ces changements peuvent avoir effet sur les racines émergentes à ce niveau. Il n'y a pas de sténose spinale. Il n'y a pas de protrusion discale centrale.

L4-L5 : Protrusion discale centrale/paracentrale gauche, associée avec un hypersignal. Ceci est discret d'à peine 1 à 2mm d'épaisseur antéropostérieure. Ces changements causent une très légère diminution du foramen neural à gauche et peuvent avoir effet sur les racines émergentes à ce niveau, surtout à gauche. Il n'y a pas de sténose spinale.

L5-S1 : Il n'y a pas de hernie discale centrale ni de sténose spinale ni d'atteinte foraminale significative.
"""


run_body_region_app(
    region_name="Lumbar (lower back)",
    system_prompt=LUMBAR_SYSTEM_PROMPT,
    compare_prompt=COMPARE_PROMPT,
    qa_prompt=QA_SYSTEM_PROMPT,
    rehab_links=LUMBAR_REHAB_LINKS, 
    prefilled_example=LUMBAR_PREFILLED_EXAMPLE,
)

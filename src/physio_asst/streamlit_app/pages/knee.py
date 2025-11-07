from body_region_app import run_body_region_app

from region_configs.knee_config import (
    KNEE_SYSTEM_PROMPT,
    COMPARE_PROMPT,
    QA_SYSTEM_PROMPT,
    KNEE_REHAB_LINKS,
)


run_body_region_app(
    region_name="Knee",
    system_prompt=KNEE_SYSTEM_PROMPT,
    compare_prompt=COMPARE_PROMPT,
    qa_prompt=QA_SYSTEM_PROMPT,
    rehab_links=KNEE_REHAB_LINKS, 
)

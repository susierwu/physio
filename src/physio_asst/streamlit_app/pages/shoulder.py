from body_region_app import run_body_region_app

from region_configs.shoulder_config import (
    SHOULDER_SYSTEM_PROMPT,
    COMPARE_PROMPT,
    QA_SYSTEM_PROMPT,
    SHOULDER_REHAB_LINKS,
)


run_body_region_app(
    region_name="Shoulder",
    system_prompt=SHOULDER_SYSTEM_PROMPT,
    compare_prompt=COMPARE_PROMPT,
    qa_prompt=QA_SYSTEM_PROMPT,
    rehab_links=SHOULDER_REHAB_LINKS, 
)


